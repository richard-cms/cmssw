/*
  Based on the jet response analyzer
  Modified by Matt Nguyen, November 2010

*/

#include "HeavyIonsAnalysis/JetAnalysis/interface/HiInclusiveJetAnalyzer.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include <Math/DistFunc.h>
#include "TMath.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "DataFormats/HeavyIonEvent/interface/CentralityBins.h"
#include "DataFormats/HeavyIonEvent/interface/Centrality.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "DataFormats/CaloTowers/interface/CaloTowerCollection.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "SimDataFormats/HiGenData/interface/GenHIEvent.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutSetup.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMapRecord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerObjectMap.h"
#include "L1Trigger/GlobalTrigger/interface/L1GlobalTrigger.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

using namespace std;
using namespace edm;
using namespace reco;

HiInclusiveJetAnalyzer::HiInclusiveJetAnalyzer(const edm::ParameterSet& iConfig) :
  geo(0)
{

  doMatch_ = iConfig.getUntrackedParameter<bool>("matchJets",false);
  jetTag_ = iConfig.getParameter<InputTag>("jetTag");
  matchTag_ = iConfig.getUntrackedParameter<InputTag>("matchTag",jetTag_);

  vtxTag_ = iConfig.getUntrackedParameter<edm::InputTag>("vtxTag",edm::InputTag("hiSelectedVertex"));
  trackTag_ = iConfig.getParameter<InputTag>("trackTag");
  useQuality_ = iConfig.getUntrackedParameter<bool>("useQuality",1);
  trackQuality_ = iConfig.getUntrackedParameter<string>("trackQuality","highPurity");

  isMC_ = iConfig.getUntrackedParameter<bool>("isMC",false);
  fillGenJets_ = iConfig.getUntrackedParameter<bool>("fillGenJets",false);

  doTrigger_ = iConfig.getUntrackedParameter<bool>("doTrigger",false);
  doHiJetID_ = iConfig.getUntrackedParameter<bool>("doHiJetID",false);
  doStandardJetID_ = iConfig.getUntrackedParameter<bool>("doStandardJetID",false);

  rParam = iConfig.getParameter<double>("rParam");
  hardPtMin_ = iConfig.getUntrackedParameter<double>("hardPtMin",4);
  jetPtMin_ = iConfig.getUntrackedParameter<double>("jetPtMin",10);

  if(isMC_){
    genjetTag_ = iConfig.getParameter<InputTag>("genjetTag");
    eventInfoTag_ = iConfig.getParameter<InputTag>("eventInfoTag");
  }
  verbose_ = iConfig.getUntrackedParameter<bool>("verbose",false);

  useCentrality_ = iConfig.getUntrackedParameter<bool>("useCentrality",false);
  useVtx_ = iConfig.getUntrackedParameter<bool>("useVtx",false);
  useJEC_ = iConfig.getUntrackedParameter<bool>("useJEC",true);
  usePat_ = iConfig.getUntrackedParameter<bool>("usePAT",true);

  doLifeTimeTagging_ = iConfig.getUntrackedParameter<bool>("doLifeTimeTagging",false);
  doLifeTimeTaggingExtras_ = iConfig.getUntrackedParameter<bool>("doLifeTimeTaggingExtras",true);
  saveBfragments_  = iConfig.getUntrackedParameter<bool>("saveBfragments",false);
  skipCorrections_  = iConfig.getUntrackedParameter<bool>("skipCorrections",false);

  pfCandidateLabel_ = iConfig.getUntrackedParameter<edm::InputTag>("pfCandidateLabel",edm::InputTag("particleFlowTmp"));

  EBSrc_ = iConfig.getUntrackedParameter<edm::InputTag>("EBRecHitSrc",edm::InputTag("ecalRecHit","EcalRecHitsEB"));
  EESrc_ = iConfig.getUntrackedParameter<edm::InputTag>("EERecHitSrc",edm::InputTag("ecalRecHit","EcalRecHitsEE"));
  HcalRecHitHFSrc_ = iConfig.getUntrackedParameter<edm::InputTag>("hcalHFRecHitSrc",edm::InputTag("hfreco"));
  HcalRecHitHBHESrc_ = iConfig.getUntrackedParameter<edm::InputTag>("hcalHBHERecHitSrc",edm::InputTag("hbhereco"));

  genParticleSrc_ = iConfig.getUntrackedParameter<edm::InputTag>("genParticles",edm::InputTag("hiGenParticles"));

  if(doTrigger_){
    L1gtReadout_ = iConfig.getParameter<edm::InputTag>("L1gtReadout");
    hltResName_ = iConfig.getUntrackedParameter<string>("hltTrgResults","TriggerResults::HLT");


    if (iConfig.exists("hltTrgNames"))
      hltTrgNames_ = iConfig.getUntrackedParameter<vector<string> >("hltTrgNames");

    if (iConfig.exists("hltProcNames"))
      hltProcNames_ = iConfig.getUntrackedParameter<vector<string> >("hltProcNames");
    else {
      hltProcNames_.push_back("FU");
      hltProcNames_.push_back("HLT");
    }
  }
  if(doLifeTimeTagging_){
    bTagJetName_ = iConfig.getUntrackedParameter<string>("bTagJetName");
    ImpactParameterTagInfos_ = iConfig.getUntrackedParameter<string>("ImpactParameterTagInfos",(bTagJetName_+"ImpactParameterTagInfos"));
    TrackCountingHighEffBJetTags_ = iConfig.getUntrackedParameter<string>("TrackCountingHighEffBJetTags",(bTagJetName_+"TrackCountingHighEffBJetTags"));
    NegativeTrackCountingHighEffJetTags_ = iConfig.getUntrackedParameter<string>("NegativeTrackCountingHighEffJetTags",bTagJetName_+("NegativeTrackCountingHighEffJetTags"));
    TrackCountingHighPurBJetTags_ = iConfig.getUntrackedParameter<string>("TrackCountingHighPurBJetTags",(bTagJetName_+"TrackCountingHighPurBJetTags"));
    NegativeTrackCountingHighPur_ = iConfig.getUntrackedParameter<string>("NegativeTrackCountingHighPur",(bTagJetName_+"NegativeTrackCountingHighPur"));
    JetProbabilityBJetTags_ = iConfig.getUntrackedParameter<string>("JetProbabilityBJetTags",(bTagJetName_+"JetProbabilityBJetTags"));
    PositiveOnlyJetProbabilityJetTags_ = iConfig.getUntrackedParameter<string>("PositiveOnlyJetProbabilityJetTags",(bTagJetName_+"PositiveOnlyJetProbabilityJetTags"));
    NegativeOnlyJetProbabilityJetTags_ = iConfig.getUntrackedParameter<string>("NegativeOnlyJetProbabilityJetTags",(bTagJetName_+"NegativeOnlyJetProbabilityJetTags"));
    JetBProbabilityBJetTags_ = iConfig.getUntrackedParameter<string>("JetBProbabilityBJetTags",(bTagJetName_+"JetBProbabilityBJetTags"));
    NegativeOnlyJetBProbabilityJetTags_ = iConfig.getUntrackedParameter<string>("NegativeOnlyJetBProbabilityJetTags",(bTagJetName_+"NegativeOnlyJetBProbabilityJetTags"));
    PositiveOnlyJetBProbabilityJetTags_ = iConfig.getUntrackedParameter<string>("PositiveOnlyJetBProbabilityJetTags",(bTagJetName_+"PositiveOnlyJetBProbabilityJetTags"));
    SecondaryVertexTagInfos_ = iConfig.getUntrackedParameter<string>("SecondaryVertexTagInfos",(bTagJetName_+"SecondaryVertexTagInfos"));
    SecondaryVertexNegativeTagInfos_ = iConfig.getUntrackedParameter<string>("SecondaryVertexNegativeTagInfos",(bTagJetName_+"SecondaryVertexNegativeTagInfos"));
    SimpleSecondaryVertexHighEffBJetTags_ = iConfig.getUntrackedParameter<string>("SimpleSecondaryVertexHighEffBJetTags",(bTagJetName_+"SimpleSecondaryVertexHighEffBJetTags"));
    SimpleSecondaryVertexNegativeHighEffBJetTags_ = iConfig.getUntrackedParameter<string>("SimpleSecondaryVertexNegativeHighEffBJetTags",(bTagJetName_+"SimpleSecondaryVertexNegativeHighEffBJetTags"));
    SimpleSecondaryVertexHighPurBJetTags_ = iConfig.getUntrackedParameter<string>("SimpleSecondaryVertexHighPurBJetTags",(bTagJetName_+"SimpleSecondaryVertexHighPurBJetTags"));
    SimpleSecondaryVertexNegativeHighPurBJetTags_ = iConfig.getUntrackedParameter<string>("SimpleSecondaryVertexNegativeHighPurBJetTags",(bTagJetName_+"SimpleSecondaryVertexNegativeHighPurBJetTags"));
    CombinedSecondaryVertexBJetTags_ = iConfig.getUntrackedParameter<string>("CombinedSecondaryVertexBJetTags",(bTagJetName_+"CombinedSecondaryVertexBJetTags"));
    CombinedSecondaryVertexNegativeBJetTags_ = iConfig.getUntrackedParameter<string>("CombinedSecondaryVertexNegativeBJetTags",(bTagJetName_+"CombinedSecondaryVertexNegativeBJetTags"));
    CombinedSecondaryVertexPositiveBJetTags_ = iConfig.getUntrackedParameter<string>("CombinedSecondaryVertexPositiveBJetTags",(bTagJetName_+"CombinedSecondaryVertexPositiveBJetTags"));
    NegativeSoftMuonByPtBJetTags_ = iConfig.getUntrackedParameter<string>("NegativeSoftMuonByPtBJetTags",(bTagJetName_+"NegativeSoftMuonByPtBJetTags"));
    PositiveSoftMuonByPtBJetTags_ = iConfig.getUntrackedParameter<string>("PositiveSoftMuonByPtBJetTags",(bTagJetName_+"PositiveSoftMuonByPtBJetTags"));
  }

  //  cout<<" jet collection : "<<jetTag_<<endl;
  doSubEvent_ = 0;

  if(isMC_){
    //     cout<<" genjet collection : "<<genjetTag_<<endl;
    genPtMin_ = iConfig.getUntrackedParameter<double>("genPtMin",10);
    doSubEvent_ = iConfig.getUntrackedParameter<bool>("doSubEvent",1);
  }


  //produces<TTree>("myjets");
  produces<int>("nref");
  produces<int>("run");
  produces<int>("evt");
  produces<int>("lumi");
  produces<int>("bin");
  produces<float>("vx");
  produces<float>("vy");
  produces<float>("vz");
  produces<float>("b");
  produces<float>("hf");

  produces<std::vector<float> > ("rawpt");
  produces<std::vector<float> > ("jtpt");
  produces<std::vector<float> > ("jteta");
  produces<std::vector<float> > ("jtphi");
  produces<std::vector<float> > ("jty");
  produces<std::vector<float> > ("jtpu");
  produces<std::vector<float> > ("jtm");

  produces<std::vector<float> > ("trackMax");
  produces<std::vector<float> > ("trackSum");
  produces<std::vector<int> > ("trackN");

  produces<std::vector<float> > ("chargedMax");
  produces<std::vector<float> > ("chargedSum");
  produces<std::vector<int> > ("chargedN");

  produces<std::vector<float> > ("photonMax");
  produces<std::vector<float> > ("photonSum");
  produces<std::vector<int> > ("photonN");

  produces<std::vector<float> > ("trackHardSum");
  produces<std::vector<float> > ("chargedHardSum");
  produces<std::vector<float> > ("photonHardSum");

  produces<std::vector<int> > ("trackHardN");
  produces<std::vector<int> > ("chargedHardN");
  produces<std::vector<int> > ("photonHardN");

  produces<std::vector<float> > ("neutralMax");
  produces<std::vector<float> > ("neutralSum");
  produces<std::vector<int> > ("neutralN");

  produces<std::vector<float> > ("eMax");
  produces<std::vector<float> > ("eSum");
  produces<std::vector<int> > ("eN");

  produces<std::vector<float> > ("muMax");
  produces<std::vector<float> > ("muSum");
  produces<std::vector<int> > ("muN");

  produces<std::vector<float> > ("genChargedSum");
  produces<std::vector<float> > ("genHardSum");
  produces<std::vector<float> > ("signalChargedSum");
  produces<std::vector<float> > ("signalHardSum");

  produces<std::vector<float> > ("hcalSum");
  produces<std::vector<float> > ("ecalSum");


  produces<std::vector<float> > ("fHPD");
  produces<std::vector<float> > ("fRBX");
  produces<std::vector<int> > ("n90");
  produces<std::vector<float> > ("fSubDet1");
  produces<std::vector<float> > ("fSubDet2");
  produces<std::vector<float> > ("fSubDet3");
  produces<std::vector<float> > ("fSubDet4");
  produces<std::vector<float> > ("restrictedEMF");
  produces<std::vector<int> > ("nHCAL");
  produces<std::vector<int> > ("nECAL");
  produces<std::vector<float> > ("apprHPD");
  produces<std::vector<float> > ("apprRBX");

    //    std::auto_ptr<std::vector<int> > n90;
  produces<std::vector<int> > ("n2RPC");
  produces<std::vector<int> > ("n3RPC");
  produces<std::vector<int> > ("nRPC");

  produces<std::vector<float> > ("fEB");
  produces<std::vector<float> > ("fEE");
  produces<std::vector<float> > ("fHB");
  produces<std::vector<float> > ("fHE");
  produces<std::vector<float> > ("fHO");
  produces<std::vector<float> > ("fLong");
  produces<std::vector<float> > ("fShort");
  produces<std::vector<float> > ("fLS");
  produces<std::vector<float> > ("fHFOOT");


  produces<std::vector<int> > ("subid");

  produces<std::vector<float> > ("matchedPt");
  produces<std::vector<float> > ("matchedRawPt");
  produces<std::vector<float> > ("matchedR");
  produces<std::vector<float> > ("matchedPu");

  produces<std::vector<float> > ("discrcsvMva");
  produces<std::vector<float> > ("discrcsvSimple");
  produces<std::vector<float> > ("discrmuByIp3");
  produces<std::vector<float> > ("discrmuByPt");
  produces<std::vector<float> > ("discrprob");
  produces<std::vector<float> > ("discrprobb");
  produces<std::vector<float> > ("discrtcHighEff");
  produces<std::vector<float> > ("discrtcHighPur");
  produces<std::vector<float> > ("discrssvHighEff");
  produces<std::vector<float> > ("discrssvHighPur");

  produces<std::vector<float> > ("ndiscrssvHighEff");
  produces<std::vector<float> > ("ndiscrssvHighPur");
  produces<std::vector<float> > ("ndiscrcsvSimple");
  produces<std::vector<float> > ("ndiscrmuByPt");
  produces<std::vector<float> > ("ndiscrprob");
  produces<std::vector<float> > ("ndiscrprobb");
  produces<std::vector<float> > ("ndiscrtcHighEff");
  produces<std::vector<float> > ("ndiscrtcHighPur");

  produces<std::vector<float> > ("pdiscrcsvSimple");
  produces<std::vector<float> > ("pdiscrprob");
  produces<std::vector<float> > ("pdiscrprobb");

  produces<std::vector<int> > ("nsvtx");
  produces<std::vector<int> > ("svtxntrk");
  produces<std::vector<float> > ("svtxdl");
  produces<std::vector<float> > ("svtxdls");
  produces<std::vector<float> > ("svtxm");
  produces<std::vector<float> > ("svtxpt");
  produces<std::vector<float> > ("svtxnormchi2");

  produces<std::vector<int> > ("nIPtrk");
  produces<std::vector<int> > ("nselIPtrk");

  produces<int> ("nIP");
  produces<std::vector<int> > ("ipJetIndex");
  produces<std::vector<float> > ("ipPt");
  produces<std::vector<float> > ("ipEta");
  produces<std::vector<float> > ("ipDxy");
  produces<std::vector<float> > ("ipDz");
  produces<std::vector<float> > ("ipChi2");
  produces<std::vector<int> > ("ipNHit");
  produces<std::vector<int> > ("ipNHitPixel");
  produces<std::vector<int> > ("ipNHitStrip");
  produces<std::vector<bool> > ("ipIsHitL1");
  produces<std::vector<float> > ("ipProb0");
  produces<std::vector<float> > ("ipProb1");
  produces<std::vector<float> > ("ip2d");
  produces<std::vector<float> > ("ip2dSig");
  produces<std::vector<float> > ("ip3d");
  produces<std::vector<float> > ("ip3dSig");
  produces<std::vector<float> > ("ipDist2Jet");
  produces<std::vector<float> > ("ipDist2JetSig");
  produces<std::vector<float> > ("ipClosest2Jet");

  produces<std::vector<float> > ("mue");
  produces<std::vector<float> > ("mupt");
  produces<std::vector<float> > ("mueta");
  produces<std::vector<float> > ("muphi");
  produces<std::vector<float> > ("mudr");
  produces<std::vector<float> > ("muptrel");
  produces<std::vector<int> > ("muchg");

  produces<std::vector<float> > ("discrfr01");

  produces<std::vector<float> > ("refpt");
  produces<std::vector<float> > ("refeta");
  produces<std::vector<float> > ("refphi");
  produces<std::vector<float> > ("refy");
  produces<std::vector<float> > ("refdphijt");
  produces<std::vector<float> > ("refdrjt");
  produces<std::vector<float> > ("refpartonpt");
  produces<std::vector<int> > ("refpartonflavor");
  produces<std::vector<int> > ("refpartonflavorForB");
  produces<float> ("pthat");

  produces<int> ("beamId1");
  produces<int> ("beamId2");
  produces<int> ("ngen");
  produces<std::vector<int> > ("genmatchindex");
  produces<std::vector<float> > ("genpt");
  produces<std::vector<float> > ("geneta");
  produces<std::vector<float> > ("genphi");
  produces<std::vector<float> > ("geny");
  produces<std::vector<float> > ("gendphijt");
  produces<std::vector<float> > ("gendrjt");
  produces<std::vector<int> > ("gensubid");

  // hlt
  produces<int> ("nHLTBit");
  produces<std::vector<bool> > ("hltBit");

  // l1
  produces<int> ("nL1TBit");
  produces<std::vector<bool> > ("l1TBit");
  produces<int> ("nL1ABit");
  produces<std::vector<bool> > ("l1ABit");

  produces<int> ("bMult");
  produces<std::vector<int> > ("bJetIndex");
  produces<std::vector<int> > ("bStatus");
  produces<std::vector<int> > ("bPdg");
  produces<std::vector<int> > ("bChg");
  produces<std::vector<float> > ("bVx");
  produces<std::vector<float> > ("bVy");
  produces<std::vector<float> > ("bVz");
  produces<std::vector<float> > ("bPt");
  produces<std::vector<float> > ("bEta");
  produces<std::vector<float> > ("bPhi");
}



HiInclusiveJetAnalyzer::~HiInclusiveJetAnalyzer() { }



void
HiInclusiveJetAnalyzer::beginRun(const edm::Run& run,
				 const edm::EventSetup & es) {}

void
HiInclusiveJetAnalyzer::beginJob() {
  centrality_ = 0;
  TH1D::SetDefaultSumw2();
}


void
HiInclusiveJetAnalyzer::produce(Event& iEvent,
				const EventSetup& iSetup) {

  jets_.nref = std::auto_ptr<int>( new int);
  jets_.run = std::auto_ptr<int>(new int);
  jets_.evt = std::auto_ptr<int>(new int);
  jets_.lumi = std::auto_ptr<int>(new int);
  jets_.bin = std::auto_ptr<int>(new int);
  jets_.vx = std::auto_ptr<float>(new float);
  jets_.vy = std::auto_ptr<float>(new float);
  jets_.vz = std::auto_ptr<float>(new float);
  jets_.b = std::auto_ptr<float>(new float);
  jets_.hf = std::auto_ptr<float>(new float);

  jets_.rawpt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jtpt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jteta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jtphi = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jty = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jtpu = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.jtm = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.trackMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.trackSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.trackN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.chargedMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.chargedSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.chargedN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.photonMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.photonSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.photonN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.trackHardSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.chargedHardSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.photonHardSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.trackHardN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.chargedHardN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.photonHardN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.neutralMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.neutralSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.neutralN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.eMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.eSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.eN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.muMax = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.muSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.muN = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.genChargedSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.genHardSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.signalChargedSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.signalHardSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.hcalSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ecalSum = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));


  jets_.fHPD = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fRBX = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.n90 = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.fSubDet1 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fSubDet2 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fSubDet3 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fSubDet4 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.restrictedEMF = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.nHCAL = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.nECAL = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.apprHPD = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.apprRBX = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  //    std::auto_ptr<std::vector<int> > n90;
  jets_.n2RPC = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.n3RPC = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.nRPC = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.fEB = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fEE = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fHB = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fHE = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fHO = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fLong = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fShort = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fLS = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.fHFOOT = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));


  jets_.subid = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.matchedPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.matchedRawPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.matchedR = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.matchedPu = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.discr_csvMva = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_csvSimple = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_muByIp3 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_muByPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_prob = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_probb = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_tcHighEff = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_tcHighPur = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_ssvHighEff = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.discr_ssvHighPur = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.ndiscr_ssvHighEff = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_ssvHighPur = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_csvSimple = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_muByPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_prob = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_probb = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_tcHighEff = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.ndiscr_tcHighPur = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.pdiscr_csvSimple = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.pdiscr_prob = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.pdiscr_probb = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.nsvtx = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.svtxntrk = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.svtxdl = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.svtxdls = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.svtxm = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.svtxpt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.svtxnormchi2 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.nIPtrk = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.nselIPtrk = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.nIP = std::auto_ptr<int>(new int);
  jets_.ipJetIndex = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXTRACKS));
  jets_.ipPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipEta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipDxy = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipDz = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipChi2 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipNHit = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXTRACKS));
  jets_.ipNHitPixel = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXTRACKS));
  jets_.ipNHitStrip = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXTRACKS));
  jets_.ipIsHitL1 = std::auto_ptr<std::vector<bool> > (new std::vector<bool>(MAXTRACKS));
  jets_.ipProb0 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipProb1 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ip2d = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ip2dSig = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ip3d = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ip3dSig = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipDist2Jet = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipDist2JetSig = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));
  jets_.ipClosest2Jet = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXTRACKS));

  jets_.mue = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.mupt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.mueta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.muphi = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.mudr = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.muptrel = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.muchg = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.discr_fr01 = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  jets_.refpt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refeta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refphi = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refy = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refdphijt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refdrjt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refparton_pt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.refparton_flavor = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.refparton_flavorForB = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  jets_.pthat = std::auto_ptr<float>(new float);
  jets_.beamId1 = std::auto_ptr<int>(new int);
  jets_.beamId2 = std::auto_ptr<int>(new int);
  jets_.ngen = std::auto_ptr<int>(new int);
  jets_.genmatchindex = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.genpt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.geneta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.genphi = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.geny = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.gendphijt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.gendrjt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.gensubid = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));

  // hlt
  jets_.nHLTBit = std::auto_ptr<int>(new int);
  jets_.hltBit = std::auto_ptr<std::vector<bool> > (new std::vector<bool>(MAXHLTBITS));

  // l1
  jets_.nL1TBit = std::auto_ptr<int>(new int);
  jets_.l1TBit = std::auto_ptr<std::vector<bool> > (new std::vector<bool>(MAXHLTBITS));
  jets_.nL1ABit = std::auto_ptr<int>(new int);
  jets_.l1ABit = std::auto_ptr<std::vector<bool> > (new std::vector<bool>(MAXHLTBITS));

  jets_.bMult = std::auto_ptr<int>(new int);
  jets_.bJetIndex = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.bStatus = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.bPdg = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.bChg = std::auto_ptr<std::vector<int> > (new std::vector<int>(MAXJETS));
  jets_.bVx = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.bVy = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.bVz = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.bPt = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.bEta = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));
  jets_.bPhi = std::auto_ptr<std::vector<float> > (new std::vector<float>(MAXJETS));

  int event = iEvent.id().event();
  int run = iEvent.id().run();
  int lumi = iEvent.id().luminosityBlock();

  *jets_.run = run;
  *jets_.evt = event;
  *jets_.lumi = lumi;

  LogDebug("HiInclusiveJetAnalyzer")<<"START event: "<<event<<" in run "<<run<<endl;

  int bin = -1;
  double hf = 0.;
  double b = 999.;

  if(doHiJetID_ && !geo){
    edm::ESHandle<CaloGeometry> pGeo;
    iSetup.get<CaloGeometryRecord>().get(pGeo);
    geo = pGeo.product();
  }
  if(useCentrality_){
    if(!centrality_) centrality_ = new CentralityProvider(iSetup);
    centrality_->newEvent(iEvent,iSetup); // make sure you do this first in every event
    //double c = centrality_->centralityValue();
    const reco::Centrality *cent = centrality_->raw();

    hf = cent->EtHFhitSum();

    bin = centrality_->getBin();
    b = centrality_->bMean();
  }

  // loop the events

  *jets_.bin = bin;
  *jets_.hf = hf;

  reco::Vertex::Point vtx(0,0,0);
  if (useVtx_) {
    edm::Handle<vector<reco::Vertex> >vertex;
    iEvent.getByLabel(vtxTag_, vertex);

    if(vertex->size()>0) {
      *jets_.vx=vertex->begin()->x();
      *jets_.vy=vertex->begin()->y();
      *jets_.vz=vertex->begin()->z();
      vtx = vertex->begin()->position();
    }
  }

  edm::Handle<pat::JetCollection> patjets;
  if(usePat_)iEvent.getByLabel(jetTag_, patjets);

  edm::Handle<pat::JetCollection> patmatchedjets;
  iEvent.getByLabel(matchTag_, patmatchedjets);

  edm::Handle<reco::JetView> matchedjets;
  iEvent.getByLabel(matchTag_, matchedjets);

  edm::Handle<reco::JetView> jets;
  iEvent.getByLabel(jetTag_, jets);

  edm::Handle<reco::PFCandidateCollection> pfCandidates;
  iEvent.getByLabel(pfCandidateLabel_,pfCandidates);

  edm::Handle<reco::TrackCollection> tracks;
  iEvent.getByLabel(trackTag_,tracks);

  edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > ebHits;
  edm::Handle<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > > eeHits;

  edm::Handle<HFRecHitCollection> hfHits;
  edm::Handle<HBHERecHitCollection> hbheHits;

  iEvent.getByLabel(HcalRecHitHBHESrc_,hbheHits);
  iEvent.getByLabel(HcalRecHitHFSrc_,hfHits);
  iEvent.getByLabel(EBSrc_,ebHits);
  iEvent.getByLabel(EESrc_,eeHits);

  edm::Handle<reco::GenParticleCollection> genparts;
  iEvent.getByLabel(genParticleSrc_,genparts);

  //Get all the b-tagging handles
  // Track Counting Taggers
  //------------------------------------------------------
  Handle<JetTagCollection> jetTags_TCHighEff;
  Handle<JetTagCollection> jetTags_NegTCHighEff;
  Handle<JetTagCollection> jetTags_TCHighPur;
  Handle<JetTagCollection> jetTags_NegTCHighPur;

  //------------------------------------------------------
  // Jet Probability tagger
  //------------------------------------------------------
  Handle<vector<TrackIPTagInfo> > tagInfo;
  Handle<JetTagCollection> jetTags_JP;
  Handle<JetTagCollection> jetTags_PosJP;
  Handle<JetTagCollection> jetTags_NegJP;
  Handle<JetTagCollection> jetTags_JB;
  Handle<JetTagCollection> jetTags_NegJB;
  Handle<JetTagCollection> jetTags_PosJB;

  //------------------------------------------------------
  // Secondary vertex taggers
  //------------------------------------------------------
  Handle<vector<SecondaryVertexTagInfo> > tagInfoSVx;
  Handle<vector<SecondaryVertexTagInfo> > tagInfoNegSVx;
  Handle<JetTagCollection> jetTags_SvtxHighEff;
  Handle<JetTagCollection> jetTags_negSvtxHighEff;
  Handle<JetTagCollection> jetTags_SvtxHighPur;
  Handle<JetTagCollection> jetTags_negSvtxHighPur;
  Handle<JetTagCollection> jetTags_CombinedSvtx;
  Handle<JetTagCollection> jetTags_negCombinedSvtx;
  Handle<JetTagCollection> jetTags_posCombinedSvtx;

  //------------------------------------------------------
  // Soft muon tagger
  //------------------------------------------------------

  Handle<SoftLeptonTagInfoCollection> tagInos_softmuon;
  Handle<JetTagCollection> jetTags_softMu;
  Handle<JetTagCollection> jetTags_softMuneg;

  if(doLifeTimeTagging_){
    iEvent.getByLabel(ImpactParameterTagInfos_, tagInfo);
    iEvent.getByLabel(TrackCountingHighEffBJetTags_, jetTags_TCHighEff);
    iEvent.getByLabel(NegativeTrackCountingHighEffJetTags_, jetTags_NegTCHighEff);
    iEvent.getByLabel(TrackCountingHighPurBJetTags_, jetTags_TCHighPur);
    iEvent.getByLabel(NegativeTrackCountingHighPur_, jetTags_NegTCHighPur);
    iEvent.getByLabel(JetProbabilityBJetTags_, jetTags_JP);
    iEvent.getByLabel(PositiveOnlyJetProbabilityJetTags_, jetTags_PosJP);
    iEvent.getByLabel(NegativeOnlyJetProbabilityJetTags_, jetTags_NegJP);
    iEvent.getByLabel(JetBProbabilityBJetTags_, jetTags_JB);
    iEvent.getByLabel(NegativeOnlyJetBProbabilityJetTags_, jetTags_NegJB);
    iEvent.getByLabel(PositiveOnlyJetBProbabilityJetTags_, jetTags_PosJB);
    iEvent.getByLabel(SecondaryVertexTagInfos_, tagInfoSVx);
    iEvent.getByLabel(SecondaryVertexNegativeTagInfos_, tagInfoNegSVx);
    iEvent.getByLabel(SimpleSecondaryVertexHighEffBJetTags_, jetTags_SvtxHighEff);
    iEvent.getByLabel(SimpleSecondaryVertexNegativeHighEffBJetTags_, jetTags_negSvtxHighEff);
    iEvent.getByLabel(SimpleSecondaryVertexHighPurBJetTags_, jetTags_SvtxHighPur);
    iEvent.getByLabel(SimpleSecondaryVertexNegativeHighEffBJetTags_, jetTags_negSvtxHighPur);
    iEvent.getByLabel(CombinedSecondaryVertexBJetTags_, jetTags_CombinedSvtx);
    iEvent.getByLabel(CombinedSecondaryVertexNegativeBJetTags_, jetTags_negCombinedSvtx);
    iEvent.getByLabel(CombinedSecondaryVertexPositiveBJetTags_, jetTags_posCombinedSvtx);
    iEvent.getByLabel(NegativeSoftMuonByPtBJetTags_, jetTags_softMuneg);
    iEvent.getByLabel(PositiveSoftMuonByPtBJetTags_, jetTags_softMu);
  }


  // FILL JRA TREE
  *jets_.b = b;
  *jets_.nref = 0;


  if(doTrigger_){
    fillL1Bits(iEvent);
    fillHLTBits(iEvent);
  }

  for(unsigned int j = 0; j < jets->size(); ++j){
    const reco::Jet& jet = (*jets)[j];

    if(jet.pt() < jetPtMin_) continue;
    if (useJEC_ && usePat_){
      (*jets_.rawpt)[*jets_.nref]=(*patjets)[j].correctedJet("Uncorrected").pt();
    }

    if(doLifeTimeTagging_){
      int ith_tagged =    this->TaggedJet(jet,jetTags_SvtxHighEff);
      if(ith_tagged >= 0){
	(*jets_.discr_ssvHighEff)[*jets_.nref] = (*jetTags_SvtxHighEff)[ith_tagged].second;
	const SecondaryVertexTagInfo &tagInfoSV = (*tagInfoSVx)[ith_tagged];
	(*jets_.nsvtx)[*jets_.nref]     = tagInfoSV.nVertices();

	if ( (*jets_.nsvtx)[*jets_.nref] > 0) {

	  (*jets_.svtxntrk)[*jets_.nref]  = tagInfoSV.nVertexTracks(0);

	  // this is the 3d flight distance, for 2-D use (0,true)
	  Measurement1D m1D = tagInfoSV.flightDistance(0);
	  (*jets_.svtxdl)[*jets_.nref]    = m1D.value();
	  (*jets_.svtxdls)[*jets_.nref]   = m1D.significance();
	  const Vertex& svtx = tagInfoSV.secondaryVertex(0);
	  (*jets_.svtxm)[*jets_.nref]    = svtx.p4().mass();
	  (*jets_.svtxpt)[*jets_.nref]   = svtx.p4().pt();
	  if(svtx.ndof()>0)(*jets_.svtxnormchi2)[*jets_.nref]  = svtx.chi2()/svtx.ndof();
	}
      }
      ith_tagged    = this->TaggedJet(jet,jetTags_negSvtxHighEff);
      if(ith_tagged >= 0) (*jets_.ndiscr_ssvHighEff)[*jets_.nref]   = (*jetTags_negSvtxHighEff)[ith_tagged].second;
      ith_tagged    = this->TaggedJet(jet,jetTags_SvtxHighPur);
      if(ith_tagged >= 0) (*jets_.discr_ssvHighPur)[*jets_.nref]  = (*jetTags_SvtxHighPur)[ith_tagged].second;
      ith_tagged    = this->TaggedJet(jet,jetTags_negSvtxHighPur);
      if(ith_tagged >= 0) (*jets_.ndiscr_ssvHighPur)[*jets_.nref] = (*jetTags_negSvtxHighPur)[ith_tagged].second;

      ith_tagged          = this->TaggedJet(jet,jetTags_CombinedSvtx);
      if(ith_tagged >= 0) (*jets_.discr_csvSimple)[*jets_.nref]  = (*jetTags_CombinedSvtx)[ith_tagged].second;
      ith_tagged          = this->TaggedJet(jet,jetTags_negCombinedSvtx);
      if(ith_tagged >= 0) (*jets_.ndiscr_csvSimple)[*jets_.nref] = (*jetTags_negCombinedSvtx)[ith_tagged].second;
      ith_tagged  = this->TaggedJet(jet,jetTags_posCombinedSvtx);
      if(ith_tagged >= 0) (*jets_.pdiscr_csvSimple)[*jets_.nref] = (*jetTags_posCombinedSvtx)[ith_tagged].second;

      if(ith_tagged >= 0){
	ith_tagged = this->TaggedJet(jet,jetTags_JP);
	(*jets_.discr_prob)[*jets_.nref]  = (*jetTags_JP)[ith_tagged].second;

	const TrackIPTagInfo& tagInfoIP= (*tagInfo)[ith_tagged];

	(*jets_.nIPtrk)[*jets_.nref] = tagInfoIP.tracks().size();
	(*jets_.nselIPtrk)[*jets_.nref] = tagInfoIP.selectedTracks().size();
	if (doLifeTimeTaggingExtras_) {

	  TrackRefVector selTracks=tagInfoIP.selectedTracks();

	  GlobalPoint pv(tagInfoIP.primaryVertex()->position().x(),tagInfoIP.primaryVertex()->position().y(),tagInfoIP.primaryVertex()->position().z());

	  for(int it=0;it<(*jets_.nselIPtrk)[*jets_.nref] ;it++)
	  {
	    (*jets_.ipJetIndex)[*jets_.nIP + it]= *jets_.nref;
	    TrackIPTagInfo::TrackIPData data = tagInfoIP.impactParameterData()[it];
	    (*jets_.ipPt)[*jets_.nIP + it] = selTracks[it]->pt();
	    (*jets_.ipEta)[*jets_.nIP + it] = selTracks[it]->eta();
	    (*jets_.ipDxy)[*jets_.nIP + it] = selTracks[it]->dxy(tagInfoIP.primaryVertex()->position());
	    (*jets_.ipDz)[*jets_.nIP + it] = selTracks[it]->dz(tagInfoIP.primaryVertex()->position());
	    (*jets_.ipChi2)[*jets_.nIP + it] = selTracks[it]->normalizedChi2();
	    (*jets_.ipNHit)[*jets_.nIP + it] = selTracks[it]->numberOfValidHits();
	    (*jets_.ipNHitPixel)[*jets_.nIP + it] = selTracks[it]->hitPattern().numberOfValidPixelHits();
	    (*jets_.ipNHitStrip)[*jets_.nIP + it] = selTracks[it]->hitPattern().numberOfValidStripHits();
	    (*jets_.ipIsHitL1)[*jets_.nIP + it]  = selTracks[it]->hitPattern().hasValidHitInFirstPixelBarrel();
	    (*jets_.ipProb0)[*jets_.nIP + it] = tagInfoIP.probabilities(0)[it];
	    (*jets_.ip2d)[*jets_.nIP + it] = data.ip2d.value();
	    (*jets_.ip2dSig)[*jets_.nIP + it] = data.ip2d.significance();
	    (*jets_.ip3d)[*jets_.nIP + it] = data.ip3d.value();
	    (*jets_.ip3dSig)[*jets_.nIP + it] = data.ip3d.significance();
	    (*jets_.ipDist2Jet)[*jets_.nIP + it] = data.distanceToJetAxis.value();
	    (*jets_.ipClosest2Jet)[*jets_.nIP + it] = (data.closestToJetAxis - pv).mag();  //decay length
	  }

	  *jets_.nIP += (*jets_.nselIPtrk)[*jets_.nref];

	}
      }
      ith_tagged = this->TaggedJet(jet,jetTags_PosJP);
      if(ith_tagged >= 0) (*jets_.pdiscr_prob)[*jets_.nref] = (*jetTags_PosJP)[ith_tagged].second;
      ith_tagged   = this->TaggedJet(jet,jetTags_NegJP);
      if(ith_tagged >= 0) (*jets_.ndiscr_prob)[*jets_.nref] = (*jetTags_NegJP)[ith_tagged].second;

      ith_tagged = this->TaggedJet(jet,jetTags_JB);
      if(ith_tagged >= 0) (*jets_.discr_probb)[*jets_.nref]  = (*jetTags_JB)[ith_tagged].second;
      ith_tagged = this->TaggedJet(jet,jetTags_NegJB);
      if(ith_tagged >= 0) (*jets_.ndiscr_probb)[*jets_.nref] = (*jetTags_NegJB)[ith_tagged].second;
      ith_tagged = this->TaggedJet(jet,jetTags_PosJB);
      if(ith_tagged >= 0) (*jets_.pdiscr_probb)[*jets_.nref] = (*jetTags_PosJB)[ith_tagged].second;

      ith_tagged    = this->TaggedJet(jet,jetTags_TCHighEff);
      if(ith_tagged >= 0) (*jets_.discr_tcHighEff)[*jets_.nref]   = (*jetTags_TCHighEff)[ith_tagged].second;
      ith_tagged    = this->TaggedJet(jet,jetTags_TCHighPur);
      if(ith_tagged >= 0) (*jets_.discr_tcHighPur)[*jets_.nref]   = (*jetTags_TCHighPur)[ith_tagged].second;
      ith_tagged    = this->TaggedJet(jet,jetTags_NegTCHighEff);
      if(ith_tagged >= 0) (*jets_.ndiscr_tcHighEff)[*jets_.nref]   = (*jetTags_NegTCHighEff)[ith_tagged].second;
      ith_tagged    = this->TaggedJet(jet,jetTags_NegTCHighPur);
      if(ith_tagged >= 0) (*jets_.ndiscr_tcHighPur)[*jets_.nref]   = (*jetTags_NegTCHighPur)[ith_tagged].second;


      ith_tagged = this->TaggedJet(jet,jetTags_softMu);
      if(ith_tagged >= 0){
	if ( (*jetTags_softMu)[ith_tagged].second     > -100000 )
	  (*jets_.discr_muByPt)[*jets_.nref]  = (*jetTags_softMu)[ith_tagged].second;
      }
      ith_tagged = this->TaggedJet(jet,jetTags_softMuneg);
      if(ith_tagged >= 0){
	float SoftMN = 0;
	if ( (*jetTags_softMuneg)[ith_tagged].second  > -100000 )
	  SoftMN = ((*jetTags_softMuneg)[ith_tagged].second);
	if ( SoftMN > 0 ) SoftMN = -SoftMN;
	(*jets_.ndiscr_muByPt)[*jets_.nref] = SoftMN;
      }
      const PFCandidateCollection *pfCandidateColl = &(*pfCandidates);
      int pfMuonIndex = getPFJetMuon(jet, pfCandidateColl);


      if(pfMuonIndex >=0){
	const reco::PFCandidate muon = pfCandidateColl->at(pfMuonIndex);
	(*jets_.mupt)[*jets_.nref]    =  muon.pt();
	(*jets_.mueta)[*jets_.nref]   =  muon.eta();
	(*jets_.muphi)[*jets_.nref]   =  muon.phi();
	(*jets_.mue)[*jets_.nref]     =  muon.energy();
	(*jets_.mudr)[*jets_.nref]    =  reco::deltaR(jet,muon);
	(*jets_.muptrel)[*jets_.nref] =  getPtRel(muon, jet);
	(*jets_.muchg)[*jets_.nref]   =  muon.charge();
      }else{
	(*jets_.mupt)[*jets_.nref]    =  0.0;
	(*jets_.mueta)[*jets_.nref]   =  0.0;
	(*jets_.muphi)[*jets_.nref]   =  0.0;
	(*jets_.mue)[*jets_.nref]     =  0.0;
	(*jets_.mudr)[*jets_.nref]    =  9.9;
	(*jets_.muptrel)[*jets_.nref] =  0.0;
	(*jets_.muchg)[*jets_.nref]   = 0;
      }
    }

    if(doHiJetID_){
      // Jet ID variables

      (*jets_.muMax)[*jets_.nref] = 0;
      (*jets_.muSum)[*jets_.nref] = 0;
      (*jets_.muN)[*jets_.nref] = 0;

      (*jets_.eMax)[*jets_.nref] = 0;
      (*jets_.eSum)[*jets_.nref] = 0;
      (*jets_.eN)[*jets_.nref] = 0;

      (*jets_.neutralMax)[*jets_.nref] = 0;
      (*jets_.neutralSum)[*jets_.nref] = 0;
      (*jets_.neutralN)[*jets_.nref] = 0;

      (*jets_.photonMax)[*jets_.nref] = 0;
      (*jets_.photonSum)[*jets_.nref] = 0;
      (*jets_.photonN)[*jets_.nref] = 0;
      (*jets_.photonHardSum)[*jets_.nref] = 0;
      (*jets_.photonHardN)[*jets_.nref] = 0;

      (*jets_.chargedMax)[*jets_.nref] = 0;
      (*jets_.chargedSum)[*jets_.nref] = 0;
      (*jets_.chargedN)[*jets_.nref] = 0;
      (*jets_.chargedHardSum)[*jets_.nref] = 0;
      (*jets_.chargedHardN)[*jets_.nref] = 0;

      (*jets_.trackMax)[*jets_.nref] = 0;
      (*jets_.trackSum)[*jets_.nref] = 0;
      (*jets_.trackN)[*jets_.nref] = 0;
      (*jets_.trackHardSum)[*jets_.nref] = 0;
      (*jets_.trackHardN)[*jets_.nref] = 0;

      (*jets_.hcalSum)[*jets_.nref] = 0;
      (*jets_.ecalSum)[*jets_.nref] = 0;

      (*jets_.genChargedSum)[*jets_.nref] = 0;
      (*jets_.genHardSum)[*jets_.nref] = 0;

      (*jets_.signalChargedSum)[*jets_.nref] = 0;
      (*jets_.signalHardSum)[*jets_.nref] = 0;

      (*jets_.subid)[*jets_.nref] = -1;

      for(unsigned int icand = 0; icand < tracks->size(); ++icand){
	const reco::Track& track = (*tracks)[icand];
	if(useQuality_ ){
	  bool goodtrack = track.quality(reco::TrackBase::qualityByName(trackQuality_));
	  if(!goodtrack) continue;
	}

	double dr = deltaR(jet,track);
	if(dr < rParam){
	  double ptcand = track.pt();
	  (*jets_.trackSum)[*jets_.nref] += ptcand;
	  (*jets_.trackN)[*jets_.nref] += 1;

	  if(ptcand > hardPtMin_){
	    (*jets_.trackHardSum)[*jets_.nref] += ptcand;
	    (*jets_.trackHardN)[*jets_.nref] += 1;

	  }
	  if(ptcand > (*jets_.trackMax)[*jets_.nref]) (*jets_.trackMax)[*jets_.nref] = ptcand;

	}
      }

      for(unsigned int icand = 0; icand < pfCandidates->size(); ++icand){
        const reco::PFCandidate& track = (*pfCandidates)[icand];
        double dr = deltaR(jet,track);
        if(dr < rParam){
	  double ptcand = track.pt();
	  int pfid = track.particleId();

	  switch(pfid){

	  case 1:
	    (*jets_.chargedSum)[*jets_.nref] += ptcand;
	    (*jets_.chargedN)[*jets_.nref] += 1;
	    if(ptcand > hardPtMin_){
	      (*jets_.chargedHardSum)[*jets_.nref] += ptcand;
	      (*jets_.chargedHardN)[*jets_.nref] += 1;
	    }
	    if(ptcand > (*jets_.chargedMax)[*jets_.nref]) (*jets_.chargedMax)[*jets_.nref] = ptcand;
	    break;

	  case 2:
	    (*jets_.eSum)[*jets_.nref] += ptcand;
	    (*jets_.eN)[*jets_.nref] += 1;
	    if(ptcand > (*jets_.eMax)[*jets_.nref]) (*jets_.eMax)[*jets_.nref] = ptcand;
	    break;

	  case 3:
	    (*jets_.muSum)[*jets_.nref] += ptcand;
	    (*jets_.muN)[*jets_.nref] += 1;
	    if(ptcand > (*jets_.muMax)[*jets_.nref]) (*jets_.muMax)[*jets_.nref] = ptcand;
	    break;

	  case 4:
	    (*jets_.photonSum)[*jets_.nref] += ptcand;
	    (*jets_.photonN)[*jets_.nref] += 1;
	    if(ptcand > hardPtMin_){
	      (*jets_.photonHardSum)[*jets_.nref] += ptcand;
	      (*jets_.photonHardN)[*jets_.nref] += 1;
	    }
	    if(ptcand > (*jets_.photonMax)[*jets_.nref]) (*jets_.photonMax)[*jets_.nref] = ptcand;
	    break;

	  case 5:
	    (*jets_.neutralSum)[*jets_.nref] += ptcand;
	    (*jets_.neutralN)[*jets_.nref] += 1;
	    if(ptcand > (*jets_.neutralMax)[*jets_.nref]) (*jets_.neutralMax)[*jets_.nref] = ptcand;
	    break;

	  default:
	    break;

	  }
	}
      }

      // Calorimeter fractions

      for(unsigned int i = 0; i < hbheHits->size(); ++i){
	const HBHERecHit & hit= (*hbheHits)[i];
	math::XYZPoint pos = getPosition(hit.id(),vtx);
	double dr = deltaR(jet.eta(),jet.phi(),pos.eta(),pos.phi());
	if(dr < rParam){
	  (*jets_.hcalSum)[*jets_.nref] += getEt(pos,hit.energy());
	}
      }

      for(unsigned int i = 0; i < hfHits->size(); ++i){
	const HFRecHit & hit= (*hfHits)[i];
	math::XYZPoint pos = getPosition(hit.id(),vtx);
	double dr = deltaR(jet.eta(),jet.phi(),pos.eta(),pos.phi());
	if(dr < rParam){
	  (*jets_.hcalSum)[*jets_.nref] += getEt(pos,hit.energy());
	}
      }


      for(unsigned int i = 0; i < ebHits->size(); ++i){
	const EcalRecHit & hit= (*ebHits)[i];
	math::XYZPoint pos = getPosition(hit.id(),vtx);
	double dr = deltaR(jet.eta(),jet.phi(),pos.eta(),pos.phi());
	if(dr < rParam){
	  (*jets_.ecalSum)[*jets_.nref] += getEt(pos,hit.energy());
	}
      }

      for(unsigned int i = 0; i < eeHits->size(); ++i){
	const EcalRecHit & hit= (*eeHits)[i];
	math::XYZPoint pos = getPosition(hit.id(),vtx);
	double dr = deltaR(jet.eta(),jet.phi(),pos.eta(),pos.phi());
	if(dr < rParam){
	  (*jets_.ecalSum)[*jets_.nref] += getEt(pos,hit.energy());
	}
      }

    }
    // Jet ID for CaloJets



    if(doMatch_){

      // Alternative reconstruction matching (PF for calo, calo for PF)

      double drMin = 100;
      for(unsigned int imatch = 0 ; imatch < matchedjets->size(); ++imatch){
	const reco::Jet& mjet = (*matchedjets)[imatch];

	double dr = deltaR(jet,mjet);
	if(dr < drMin){
	  (*jets_.matchedPt)[*jets_.nref] = mjet.pt();

	  if(usePat_){
	    const pat::Jet& mpatjet = (*patmatchedjets)[imatch];
	    (*jets_.matchedRawPt)[*jets_.nref] = mpatjet.correctedJet("Uncorrected").pt();
	    (*jets_.matchedPu)[*jets_.nref] = mpatjet.pileup();
	  }
	  (*jets_.matchedR)[*jets_.nref] = dr;
	  drMin = dr;
	}
      }

    }
    //     if(etrk.quality(reco::TrackBase::qualityByName(qualityString_))) pev_.trkQual[pev_.nTrk]=1;


    if(doHiJetID_){

      /////////////////////////////////////////////////////////////////
      // Jet core pt^2 discriminant for fake jets
      // Edited by Yue Shi Lai <ylai@mit.edu>

      // Initial value is 0
      (*jets_.discr_fr01)[*jets_.nref] = 0;
      // Start with no directional adaption, i.e. the fake rejection
      // axis is the jet axis
      float pseudorapidity_adapt = (*jets_.jteta)[*jets_.nref];
      float azimuth_adapt = (*jets_.jtphi)[*jets_.nref];

      // Unadapted discriminant with adaption search
      for (size_t iteration = 0; iteration < 2; iteration++) {
	float pseudorapidity_adapt_new = pseudorapidity_adapt;
	float azimuth_adapt_new = azimuth_adapt;
	float max_weighted_perp = 0;
	float perp_square_sum = 0;

	for (size_t index_pf_candidate = 0;
	     index_pf_candidate < pfCandidates->size();
	     index_pf_candidate++) {
	  const reco::PFCandidate &p =
	    (*pfCandidates)[index_pf_candidate];

	  switch (p.particleId()) {
	    //case 1:	// Charged hadron
	    //case 3:	// Muon
	  case 4:	// Photon
	  {
	    const float dpseudorapidity =
	      p.eta() - pseudorapidity_adapt;
	    const float dazimuth =
	      reco::deltaPhi(p.phi(), azimuth_adapt);
	    // The Gaussian scale factor is 0.5 / (0.1 * 0.1)
	    // = 50
	    const float angular_weight =
	      exp(-50.0F * (dpseudorapidity * dpseudorapidity +
			    dazimuth * dazimuth));
	    const float weighted_perp =
	      angular_weight * p.pt() * p.pt();
	    const float weighted_perp_square =
	      weighted_perp * p.pt();

	    perp_square_sum += weighted_perp_square;
	    if (weighted_perp >= max_weighted_perp) {
	      pseudorapidity_adapt_new = p.eta();
	      azimuth_adapt_new = p.phi();
	      max_weighted_perp = weighted_perp;
	    }
	  }
	  default:
	    break;
	  }
	}
	// Update the fake rejection value
	(*jets_.discr_fr01)[*jets_.nref] = std::max(
	  (*jets_.discr_fr01)[*jets_.nref], perp_square_sum);
	// Update the directional adaption
	pseudorapidity_adapt = pseudorapidity_adapt_new;
	azimuth_adapt = azimuth_adapt_new;
      }
    }

    (*jets_.jtpt)[*jets_.nref] = jet.pt();
    (*jets_.jteta)[*jets_.nref] = jet.eta();
    (*jets_.jtphi)[*jets_.nref] = jet.phi();
    (*jets_.jty)[*jets_.nref] = jet.eta();
    (*jets_.jtpu)[*jets_.nref] = jet.pileup();
    (*jets_.jtm)[*jets_.nref] = jet.mass();

    if(usePat_){

      if(doStandardJetID_){
	(*jets_.fHPD)[*jets_.nref] = (*patjets)[j].jetID().fHPD;
	(*jets_.fRBX)[*jets_.nref] = (*patjets)[j].jetID().fRBX;
	(*jets_.n90)[*jets_.nref] = (*patjets)[j].n90();

	(*jets_.fSubDet1)[*jets_.nref] = (*patjets)[j].jetID().fSubDetector1;
	(*jets_.fSubDet2)[*jets_.nref] = (*patjets)[j].jetID().fSubDetector2;
	(*jets_.fSubDet3)[*jets_.nref] = (*patjets)[j].jetID().fSubDetector3;
	(*jets_.fSubDet4)[*jets_.nref] = (*patjets)[j].jetID().fSubDetector4;
	(*jets_.restrictedEMF)[*jets_.nref] = (*patjets)[j].jetID().restrictedEMF;
	(*jets_.nHCAL)[*jets_.nref] = (*patjets)[j].jetID().nHCALTowers;
	(*jets_.nECAL)[*jets_.nref] = (*patjets)[j].jetID().nECALTowers;
	(*jets_.apprHPD)[*jets_.nref] = (*patjets)[j].jetID().approximatefHPD;
	(*jets_.apprRBX)[*jets_.nref] = (*patjets)[j].jetID().approximatefRBX;

	//       (*jets_.n90)[*jets_.nref] = (*patjets)[j].jetID().hitsInN90;
	(*jets_.n2RPC)[*jets_.nref] = (*patjets)[j].jetID().numberOfHits2RPC;
	(*jets_.n3RPC)[*jets_.nref] = (*patjets)[j].jetID().numberOfHits3RPC;
	(*jets_.nRPC)[*jets_.nref] = (*patjets)[j].jetID().numberOfHitsRPC;

	(*jets_.fEB)[*jets_.nref] = (*patjets)[j].jetID().fEB;
	(*jets_.fEE)[*jets_.nref] = (*patjets)[j].jetID().fEE;
	(*jets_.fHB)[*jets_.nref] = (*patjets)[j].jetID().fHB;
	(*jets_.fHE)[*jets_.nref] = (*patjets)[j].jetID().fHE;
	(*jets_.fHO)[*jets_.nref] = (*patjets)[j].jetID().fHO;
	(*jets_.fLong)[*jets_.nref] = (*patjets)[j].jetID().fLong;
	(*jets_.fShort)[*jets_.nref] = (*patjets)[j].jetID().fShort;
	(*jets_.fLS)[*jets_.nref] = (*patjets)[j].jetID().fLS;
	(*jets_.fHFOOT)[*jets_.nref] = (*patjets)[j].jetID().fHFOOT;
      }

    }

    if(isMC_){

      for(UInt_t i = 0; i < genparts->size(); ++i){
	const reco::GenParticle& p = (*genparts)[i];
	if (p.status()!=1) continue;
	if (p.charge()==0) continue;
	double dr = deltaR(jet,p);
	if(dr < rParam){
	  double ppt = p.pt();
	  (*jets_.genChargedSum)[*jets_.nref] += ppt;
	  if(ppt > hardPtMin_) (*jets_.genHardSum)[*jets_.nref] += ppt;
	  if(p.collisionId() == 0){
	    (*jets_.signalChargedSum)[*jets_.nref] += ppt;
	    if(ppt > hardPtMin_) (*jets_.signalHardSum)[*jets_.nref] += ppt;
	  }

	}
      }

    }

    if(isMC_ && usePat_){


      const reco::GenJet * genjet = (*patjets)[j].genJet();

      if(genjet){
	(*jets_.refpt)[*jets_.nref] = genjet->pt();
	(*jets_.refeta)[*jets_.nref] = genjet->eta();
	(*jets_.refphi)[*jets_.nref] = genjet->phi();
	(*jets_.refy)[*jets_.nref] = genjet->eta();
	(*jets_.refdphijt)[*jets_.nref] = reco::deltaPhi(jet.phi(), genjet->phi());
	(*jets_.refdrjt)[*jets_.nref] = reco::deltaR(jet.eta(),jet.phi(),genjet->eta(),genjet->phi());

	if(doSubEvent_){
	  const GenParticle* gencon = genjet->getGenConstituent(0);
	  (*jets_.subid)[*jets_.nref] = gencon->collisionId();
	}

      }else{
	(*jets_.refpt)[*jets_.nref] = -999.;
	(*jets_.refeta)[*jets_.nref] = -999.;
	(*jets_.refphi)[*jets_.nref] = -999.;
	(*jets_.refy)[*jets_.nref] = -999.;
	(*jets_.refdphijt)[*jets_.nref] = -999.;
	(*jets_.refdrjt)[*jets_.nref] = -999.;
      }

      (*jets_.refparton_flavorForB)[*jets_.nref] = (*patjets)[j].partonFlavour();

      // matched partons
      const reco::GenParticle & parton = *(*patjets)[j].genParton();

      if((*patjets)[j].genParton()){
	(*jets_.refparton_pt)[*jets_.nref] = parton.pt();
	(*jets_.refparton_flavor)[*jets_.nref] = parton.pdgId();

	if(saveBfragments_ && abs((*jets_.refparton_flavorForB)[*jets_.nref])==5){

	  usedStringPts.clear();

	  // uncomment this if you want to know the ugly truth about parton matching -matt
	  //if(jet.pt() > 50 &&abs(parton.pdgId())!=5 && parton.pdgId()!=21)
	  // cout<<" Identified as a b, but doesn't match b or gluon, id = "<<parton.pdgId()<<endl;

	  (*jets_.bJetIndex)[*jets_.bMult] = *jets_.nref;
	  (*jets_.bStatus)[*jets_.bMult] = parton.status();
	  (*jets_.bVx)[*jets_.bMult] = parton.vx();
	  (*jets_.bVy)[*jets_.bMult] = parton.vy();
	  (*jets_.bVz)[*jets_.bMult] = parton.vz();
	  (*jets_.bPt)[*jets_.bMult] = parton.pt();
	  (*jets_.bEta)[*jets_.bMult] = parton.eta();
	  (*jets_.bPhi)[*jets_.bMult] = parton.phi();
	  (*jets_.bPdg)[*jets_.bMult] = parton.pdgId();
	  (*jets_.bChg)[*jets_.bMult] = parton.charge();
	  (*jets_.bMult)++;
	  saveDaughters(parton);
	}


      } else {
	(*jets_.refparton_pt)[*jets_.nref] = -999;
	(*jets_.refparton_flavor)[*jets_.nref] = -999;
      }


    }

    (*jets_.nref)++;


  }


  if(isMC_){

    edm::Handle<HepMCProduct> hepMCProduct;
    iEvent.getByLabel(eventInfoTag_,hepMCProduct);
    const HepMC::GenEvent* MCEvt = hepMCProduct->GetEvent();

    std::pair<HepMC::GenParticle*,HepMC::GenParticle*> beamParticles = MCEvt->beam_particles();
    if(beamParticles.first != 0)*jets_.beamId1 = beamParticles.first->pdg_id();
    if(beamParticles.second != 0)*jets_.beamId2 = beamParticles.second->pdg_id();

    edm::Handle<GenEventInfoProduct> hEventInfo;
    iEvent.getByLabel(eventInfoTag_,hEventInfo);
    //*jets_.pthat = hEventInfo->binningValues()[0];

    // binning values and qscale appear to be equivalent, but binning values not always present
    *jets_.pthat = hEventInfo->qScale();

    edm::Handle<vector<reco::GenJet> >genjets;
    iEvent.getByLabel(genjetTag_, genjets);

    *jets_.ngen = 0;
    for(unsigned int igen = 0 ; igen < genjets->size(); ++igen){
      const reco::GenJet & genjet = (*genjets)[igen];

      float genjet_pt = genjet.pt();

      // threshold to reduce size of output in minbias PbPb
      if(genjet_pt>genPtMin_){


	(*jets_.genpt)[*jets_.ngen] = genjet_pt;
	(*jets_.geneta)[*jets_.ngen] = genjet.eta();
	(*jets_.genphi)[*jets_.ngen] = genjet.phi();
	(*jets_.geny)[*jets_.ngen] = genjet.eta();

	if(doSubEvent_){
	  const GenParticle* gencon = genjet.getGenConstituent(0);
	  (*jets_.gensubid)[*jets_.ngen] = gencon->collisionId();
	}

	// find matching patJet if there is one

	(*jets_.gendrjt)[*jets_.ngen] = -1.0;
	(*jets_.genmatchindex)[*jets_.ngen] = -1;

	for(int ijet = 0 ; ijet < *jets_.nref; ++ijet){
	  // poor man's matching, someone fix please
	  if(fabs(genjet.pt()-(*jets_.refpt)[ijet])<0.00001 &&
	     fabs(genjet.eta()-(*jets_.refeta)[ijet])<0.00001){

	    (*jets_.genmatchindex)[*jets_.ngen] = (int)ijet;
	    (*jets_.gendphijt)[*jets_.ngen] = reco::deltaPhi((*jets_.refphi)[ijet],genjet.phi());
	    (*jets_.gendrjt)[*jets_.ngen] = sqrt(pow((*jets_.gendphijt)[*jets_.ngen],2)+pow(fabs(genjet.eta()-(*jets_.refeta)[ijet]),2));

	    break;
	  }
	}
      }

      (*jets_.ngen)++;
    }

  }


  iEvent.put(jets_.evt,"evt");
  iEvent.put(jets_.lumi,"lumi");
  iEvent.put(jets_.b,"b");
  if (useVtx_) {
    iEvent.put(jets_.vx,"vx");
    iEvent.put(jets_.vy,"vy");
    iEvent.put(jets_.vz,"vz");
  }
  if (useCentrality_) {
    iEvent.put(jets_.hf,"hf");
    iEvent.put(jets_.bin,"bin");
  }

  iEvent.put(jets_.nref,"nref");
  iEvent.put(jets_.rawpt,"rawpt");
  if(!skipCorrections_) iEvent.put(jets_.jtpt,"jtpt");
  iEvent.put(jets_.jteta,"jteta");
  iEvent.put(jets_.jty,"jty");
  iEvent.put(jets_.jtphi,"jtphi");
  iEvent.put(jets_.jtpu,"jtpu");
  iEvent.put(jets_.jtm,"jtm");

  // jet ID information jet composition
  if(doHiJetID_){
    iEvent.put( jets_.discr_fr01,"discrfr01");

    iEvent.put( jets_.trackMax,"trackMax");
    iEvent.put( jets_.trackSum,"trackSum");
    iEvent.put( jets_.trackN,"trackN");
    iEvent.put( jets_.trackHardSum,"trackHardSum");
    iEvent.put( jets_.trackHardN,"trackHardN");

    iEvent.put( jets_.chargedMax,"chargedMax");
    iEvent.put( jets_.chargedSum,"chargedSum");
    iEvent.put( jets_.chargedN,"chargedN");
    iEvent.put( jets_.chargedHardSum,"chargedHardSum");
    iEvent.put( jets_.chargedHardN,"chargedHardN");

    iEvent.put( jets_.photonMax,"photonMax");
    iEvent.put( jets_.photonSum,"photonSum");
    iEvent.put( jets_.photonN,"photonN");
    iEvent.put( jets_.photonHardSum,"photonHardSum");
    iEvent.put( jets_.photonHardN,"photonHardN");

    iEvent.put( jets_.neutralMax,"neutralMax");
    iEvent.put( jets_.neutralSum,"neutralSum");
    iEvent.put( jets_.neutralN,"neutralN");

    iEvent.put( jets_.hcalSum,"hcalSum");
    iEvent.put( jets_.ecalSum,"ecalSum");

    iEvent.put( jets_.eMax,"eMax");
    iEvent.put( jets_.eSum,"eSum");
    iEvent.put( jets_.eN,"eN");

    iEvent.put( jets_.muMax,"muMax");
    iEvent.put( jets_.muSum,"muSum");
    iEvent.put( jets_.muN,"muN");
  }

  if(doStandardJetID_){
    iEvent.put(jets_.fHPD,"fHPD");
    iEvent.put(jets_.fRBX,"fRBX");
    iEvent.put(jets_.n90,"n90");
    iEvent.put(jets_.fSubDet1,"fSubDet1");
    iEvent.put(jets_.fSubDet2,"fSubDet2");
    iEvent.put(jets_.fSubDet3,"fSubDet3");
    iEvent.put(jets_.fSubDet4,"fSubDet4");
    iEvent.put(jets_.restrictedEMF,"restrictedEMF");
    iEvent.put(jets_.nHCAL,"nHCAL");
    iEvent.put(jets_.nECAL,"nECAL");
    iEvent.put(jets_.apprHPD,"apprHPD");
    iEvent.put(jets_.apprRBX,"apprRBX");

    //  iEvent.put(jets_.n90);
    iEvent.put(jets_.n2RPC,"n2RPC");
    iEvent.put(jets_.n3RPC,"n3RPC");
    iEvent.put(jets_.nRPC,"nRPC");

    iEvent.put(jets_.fEB,"fEB");
    iEvent.put(jets_.fEE,"fEE");
    iEvent.put(jets_.fHB,"fHB");
    iEvent.put(jets_.fHE,"fHE");
    iEvent.put(jets_.fHO,"fHO");
    iEvent.put(jets_.fLong,"fLong");
    iEvent.put(jets_.fShort,"fShort");
    iEvent.put(jets_.fLS,"fLS");
    iEvent.put(jets_.fHFOOT,"fHFOOT");
  }

  // Jet ID
  if(doMatch_){
    if(!skipCorrections_) iEvent.put( jets_.matchedPt,"matchedPt");
    iEvent.put( jets_.matchedRawPt,"matchedRawPt");
    iEvent.put( jets_.matchedPu,"matchedPu");
    iEvent.put( jets_.matchedR,"matchedR");
  }

  // b-jet discriminators
  if (doLifeTimeTagging_) {

    iEvent.put(jets_.discr_ssvHighEff,"discrssvHighEff");
    iEvent.put(jets_.discr_ssvHighPur,"discrssvHighPur");

    iEvent.put(jets_.discr_csvMva,"discrcsvMva");
    iEvent.put(jets_.discr_csvSimple,"discrcsvSimple");
    iEvent.put(jets_.discr_muByIp3,"discrmuByIp3");
    iEvent.put(jets_.discr_muByPt,"discrmuByPt");
    iEvent.put(jets_.discr_prob,"discrprob");
    iEvent.put(jets_.discr_probb,"discrprobb");
    iEvent.put(jets_.discr_tcHighEff,"discrtcHighEff");
    iEvent.put(jets_.discr_tcHighPur,"discrtcHighPur");

    iEvent.put(jets_.ndiscr_ssvHighEff,"ndiscrssvHighEff");
    iEvent.put(jets_.ndiscr_ssvHighPur,"ndiscrssvHighPur");
    iEvent.put(jets_.ndiscr_csvSimple,"ndiscrcsvSimple");
    iEvent.put(jets_.ndiscr_muByPt,"ndiscrmuByPt");
    iEvent.put(jets_.ndiscr_prob,"ndiscrprob");
    iEvent.put(jets_.ndiscr_probb,"ndiscrprobb");
    iEvent.put(jets_.ndiscr_tcHighEff,"ndiscrtcHighEff");
    iEvent.put(jets_.ndiscr_tcHighPur,"ndiscrtcHighPur");

    iEvent.put(jets_.pdiscr_csvSimple,"pdiscrcsvSimple");
    iEvent.put(jets_.pdiscr_prob,"pdiscrprob");
    iEvent.put(jets_.pdiscr_probb,"pdiscrprobb");

    iEvent.put(    jets_.nsvtx,"nsvtx"    );
    iEvent.put( jets_.svtxntrk,"svtxntrk" );
    iEvent.put(   jets_.svtxdl,"svtxdl"   );
    iEvent.put(  jets_.svtxdls,"svtxdls"  );
    iEvent.put(    jets_.svtxm,"svtxm"    );
    iEvent.put(   jets_.svtxpt,"svtxpt"   );

    iEvent.put(jets_.nIPtrk,"nIPtrk");
    iEvent.put(jets_.nselIPtrk,"nselIPtrk");

    if (doLifeTimeTaggingExtras_) {
      iEvent.put(jets_.nIP,"nIP");
      iEvent.put(jets_.ipJetIndex,"ipJetIndex");
      iEvent.put(jets_.ipPt,"ipPt");
      iEvent.put(jets_.ipProb0,"ipProb0");
      iEvent.put(jets_.ipProb1,"ipProb1");
      iEvent.put(jets_.ip2d,"ip2d");
      iEvent.put(jets_.ip2dSig,"ip2dSig");
      iEvent.put(jets_.ip3d,"ip3d");
      iEvent.put(jets_.ip3dSig,"ip3dSig");
      iEvent.put(jets_.ipDist2Jet,"ipDist2Jet");
      iEvent.put(jets_.ipDist2JetSig,"ipDist2JetSig");
      iEvent.put(jets_.ipClosest2Jet,"ipClosest2Jet");

    }

    iEvent.put(     jets_.mue,"mue"     );
    iEvent.put(    jets_.mupt,"mupt"    );
    iEvent.put(   jets_.mueta,"mueta"   );
    iEvent.put(   jets_.muphi,"muphi"   );
    iEvent.put(    jets_.mudr,"mudr"    );
    iEvent.put( jets_.muptrel,"muptrel" );
    iEvent.put(   jets_.muchg,"muchg"   );
  }


  if(isMC_){
    iEvent.put(jets_.beamId1,"beamId1");
    iEvent.put(jets_.beamId2,"beamId2");

    iEvent.put(jets_.pthat,"pthat");

    // Only matched gen jets
    iEvent.put(jets_.refpt,"refpt");
    iEvent.put(jets_.refeta,"refeta");
    iEvent.put(jets_.refy,"refy");
    iEvent.put(jets_.refphi,"refphi");
    iEvent.put(jets_.refdphijt,"refdphijt");
    iEvent.put(jets_.refdrjt,"refdrjt");
    // matched parton
    iEvent.put(jets_.refparton_pt,"refpartonpt");
    iEvent.put(jets_.refparton_flavor,"refpartonflavor");
    iEvent.put(jets_.refparton_flavorForB,"refpartonflavorForB");

    iEvent.put( jets_.genChargedSum,"genChargedSum");
    iEvent.put( jets_.genHardSum,"genHardSum");
    iEvent.put( jets_.signalChargedSum,"signalChargedSum");
    iEvent.put( jets_.signalHardSum,"signalHardSum");

    if(doSubEvent_){
      iEvent.put(jets_.subid,"subid");
    }

    if(fillGenJets_){
      // For all gen jets matched or unmatched
      iEvent.put(jets_.ngen,"ngen");
      iEvent.put(jets_.genmatchindex,"genmatchindex");
      iEvent.put(jets_.genpt,"genpt");
      iEvent.put(jets_.geneta,"geneta");
      iEvent.put(jets_.geny,"geny");
      iEvent.put(jets_.genphi,"genphi");
      iEvent.put(jets_.gendphijt,"gendphijt");
      iEvent.put(jets_.gendrjt,"gendrjt");

      if(doSubEvent_){
	iEvent.put(jets_.gensubid,"gensubid");
      }
    }

    if(saveBfragments_  ) {
      iEvent.put(jets_.bMult,"bMult");
      iEvent.put(jets_.bJetIndex,"bJetIndex");
      iEvent.put(jets_.bStatus,"bStatus");
      iEvent.put(jets_.bVx,"bVx");
      iEvent.put(jets_.bVy,"bVy");
      iEvent.put(jets_.bVz,"bVz");
      iEvent.put(jets_.bPt,"bPt");
      iEvent.put(jets_.bEta,"bEta");
      iEvent.put(jets_.bPhi,"bPhi");
      iEvent.put(jets_.bPdg,"bPdg");
      iEvent.put(jets_.bChg,"bChg");
    }

  }

  //memset(&jets_,0,sizeof jets_);

}




//--------------------------------------------------------------------------------------------------
void HiInclusiveJetAnalyzer::fillL1Bits(const edm::Event &iEvent)
{
  edm::Handle< L1GlobalTriggerReadoutRecord >  L1GlobalTrigger;

  iEvent.getByLabel(L1gtReadout_, L1GlobalTrigger);
  const TechnicalTriggerWord&  technicalTriggerWordBeforeMask = L1GlobalTrigger->technicalTriggerWord();

  for (int i=0; i<64;i++)
  {
    (*jets_.l1TBit)[i] = technicalTriggerWordBeforeMask.at(i);
  }
  *jets_.nL1TBit = 64;

  int ntrigs = L1GlobalTrigger->decisionWord().size();
  *jets_.nL1ABit = ntrigs;

  for (int i=0; i != ntrigs; i++) {
    bool accept = L1GlobalTrigger->decisionWord()[i];
    //jets_.l1ABit[i] = (accept == true)? 1:0;
    if(accept== true){
      (*jets_.l1ABit)[i] = 1;
    }
    else{
      (*jets_.l1ABit)[i] = 0;
    }

  }
}

//--------------------------------------------------------------------------------------------------
void HiInclusiveJetAnalyzer::fillHLTBits(const edm::Event &iEvent)
{
  // Fill HLT trigger bits.
  Handle<TriggerResults> triggerResultsHLT;
  getProduct(hltResName_, triggerResultsHLT, iEvent);

  const TriggerResults *hltResults = triggerResultsHLT.product();
  const TriggerNames & triggerNames = iEvent.triggerNames(*hltResults);

  *jets_.nHLTBit = hltTrgNames_.size();

  for(size_t i=0;i<hltTrgNames_.size();i++){

    for(size_t j=0;j<triggerNames.size();++j) {

      if(triggerNames.triggerName(j) == hltTrgNames_[i]){

	//cout <<"hltTrgNames_(i) "<<hltTrgNames_[i]<<endl;
	//cout <<"triggerName(j) "<<triggerNames.triggerName(j)<<endl;
	//cout<<" result "<<triggerResultsHLT->accept(j)<<endl;
	(*jets_.hltBit)[i] = triggerResultsHLT->accept(j);
      }

    }
  }
}

//--------------------------------------------------------------------------------------------------
template <typename TYPE>
inline void HiInclusiveJetAnalyzer::getProduct(const std::string name, edm::Handle<TYPE> &prod,
					       const edm::Event &event) const
{
  // Try to access data collection from EDM file. We check if we really get just one
  // product with the given name. If not we throw an exception.

  event.getByLabel(edm::InputTag(name),prod);
  if (!prod.isValid())
    throw edm::Exception(edm::errors::Configuration, "HiInclusiveJetAnalyzer::GetProduct()\n")
      << "Collection with label '" << name << "' is not valid" <<  std::endl;
}

//--------------------------------------------------------------------------------------------------
template <typename TYPE>
inline bool HiInclusiveJetAnalyzer::getProductSafe(const std::string name, edm::Handle<TYPE> &prod,
						   const edm::Event &event) const
{
  // Try to safely access data collection from EDM file. We check if we really get just one
  // product with the given name. If not, we return false.

  if (name.size()==0)
    return false;

  try {
    event.getByLabel(edm::InputTag(name),prod);
    if (!prod.isValid())
      return false;
  } catch (...) {
    return false;
  }
  return true;
}


int
HiInclusiveJetAnalyzer::getPFJetMuon(const pat::Jet& pfJet, const reco::PFCandidateCollection *pfCandidateColl)
{

  int pfMuonIndex = -1;
  float ptMax = 0.;


  for(unsigned icand=0;icand<pfCandidateColl->size(); icand++) {
    const reco::PFCandidate pfCandidate = pfCandidateColl->at(icand);

    int id = pfCandidate.particleId();
    if(abs(id) != 3) continue;

    if(reco::deltaR(pfJet,pfCandidate)>0.5) continue;

    double pt =  pfCandidate.pt();
    if(pt>ptMax){
      ptMax = pt;
      pfMuonIndex = (int) icand;
    }
  }

  return pfMuonIndex;

}


double
HiInclusiveJetAnalyzer::getPtRel(const reco::PFCandidate lep, const pat::Jet& jet )
{

  float lj_x = jet.p4().px();
  float lj_y = jet.p4().py();
  float lj_z = jet.p4().pz();

  // absolute values squared
  float lj2  = lj_x*lj_x+lj_y*lj_y+lj_z*lj_z;
  float lep2 = lep.px()*lep.px()+lep.py()*lep.py()+lep.pz()*lep.pz();

  // projection vec(mu) to lepjet axis
  float lepXlj = lep.px()*lj_x+lep.py()*lj_y+lep.pz()*lj_z;

  // absolute value squared and normalized
  float pLrel2 = lepXlj*lepXlj/lj2;

  // lep2 = pTrel2 + pLrel2
  float pTrel2 = lep2-pLrel2;

  return (pTrel2 > 0) ? std::sqrt(pTrel2) : 0.0;
}

// Recursive function, but this version gets called only the first time
void
HiInclusiveJetAnalyzer::saveDaughters(const reco::GenParticle &gen){

  for(unsigned i=0;i<gen.numberOfDaughters();i++){
    const reco::Candidate & daughter = *gen.daughter(i);
    double daughterPt = daughter.pt();
    if(daughterPt<1.) continue;
    double daughterEta = daughter.eta();
    if(fabs(daughterEta)>3.) continue;
    int daughterPdgId = daughter.pdgId();
    int daughterStatus = daughter.status();
    // Special case when b->b+string, both b and string contain all daughters, so only take the string
    if(gen.pdgId()==daughterPdgId && gen.status()==3 && daughterStatus==2) continue;

    // cheesy way of finding strings which were already used
    if(daughter.pdgId()==92){
      for(unsigned ist=0;ist<usedStringPts.size();ist++){
	if(fabs(daughter.pt() - usedStringPts[ist]) < 0.0001) return;
      }
      usedStringPts.push_back(daughter.pt());
    }
    (*jets_.bJetIndex)[*jets_.bMult] = *jets_.nref;
    (*jets_.bStatus)[*jets_.bMult] = daughterStatus;
    (*jets_.bVx)[*jets_.bMult] = daughter.vx();
    (*jets_.bVy)[*jets_.bMult] = daughter.vy();
    (*jets_.bVz)[*jets_.bMult] = daughter.vz();
    (*jets_.bPt)[*jets_.bMult] = daughterPt;
    (*jets_.bEta)[*jets_.bMult] = daughterEta;
    (*jets_.bPhi)[*jets_.bMult] = daughter.phi();
    (*jets_.bPdg)[*jets_.bMult] = daughterPdgId;
    (*jets_.bChg)[*jets_.bMult] = daughter.charge();
    (*jets_.bMult)++;
    saveDaughters(daughter);
  }
}

// This version called for all subsequent calls
void
HiInclusiveJetAnalyzer::saveDaughters(const reco::Candidate &gen){

  for(unsigned i=0;i<gen.numberOfDaughters();i++){
    const reco::Candidate & daughter = *gen.daughter(i);
    double daughterPt = daughter.pt();
    if(daughterPt<1.) continue;
    double daughterEta = daughter.eta();
    if(fabs(daughterEta)>3.) continue;
    int daughterPdgId = daughter.pdgId();
    int daughterStatus = daughter.status();
    // Special case when b->b+string, both b and string contain all daughters, so only take the string
    if(gen.pdgId()==daughterPdgId && gen.status()==3 && daughterStatus==2) continue;

    // cheesy way of finding strings which were already used
    if(daughter.pdgId()==92){
      for(unsigned ist=0;ist<usedStringPts.size();ist++){
	if(fabs(daughter.pt() - usedStringPts[ist]) < 0.0001) return;
      }
      usedStringPts.push_back(daughter.pt());
    }

    (*jets_.bJetIndex)[*jets_.bMult] = *jets_.nref;
    (*jets_.bStatus)[*jets_.bMult] = daughterStatus;
    (*jets_.bVx)[*jets_.bMult] = daughter.vx();
    (*jets_.bVy)[*jets_.bMult] = daughter.vy();
    (*jets_.bVz)[*jets_.bMult] = daughter.vz();
    (*jets_.bPt)[*jets_.bMult] = daughterPt;
    (*jets_.bEta)[*jets_.bMult] = daughterEta;
    (*jets_.bPhi)[*jets_.bMult] = daughter.phi();
    (*jets_.bPdg)[*jets_.bMult] = daughterPdgId;
    (*jets_.bChg)[*jets_.bMult] = daughter.charge();
    (*jets_.bMult)++;
    saveDaughters(daughter);
  }
}

double HiInclusiveJetAnalyzer::getEt(math::XYZPoint pos, double energy){
  double et = energy*sin(pos.theta());
  return et;
}

math::XYZPoint HiInclusiveJetAnalyzer::getPosition(const DetId &id, reco::Vertex::Point vtx){
  const GlobalPoint& pos=geo->getPosition(id);
  math::XYZPoint posV(pos.x() - vtx.x(),pos.y() - vtx.y(),pos.z() - vtx.z());
  return posV;
}

int HiInclusiveJetAnalyzer::TaggedJet(Jet calojet, Handle<JetTagCollection > jetTags ) {
  double small = 1.e-5;
  int result = -1;

  for (size_t t = 0; t < jetTags->size(); t++) {
    RefToBase<Jet> jet_p = (*jetTags)[t].first;
    if (jet_p.isNull()) {
      continue;
    }
    if (DeltaR<Candidate>()( calojet, *jet_p ) < small) {
      result = (int) t;
    }
  }
  return result;
}

DEFINE_FWK_MODULE(HiInclusiveJetAnalyzer);
