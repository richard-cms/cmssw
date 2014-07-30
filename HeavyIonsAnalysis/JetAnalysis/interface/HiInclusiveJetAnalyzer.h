#ifndef MNguyen_HiInclusiveJetAnalyzer_inclusiveJetAnalyzer_
#define MNguyen_HiInclusiveJetAnalyzer_inclusiveJetAnalyzer_

// system include files
#include <memory>
#include <string>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "TFile.h"
#include "TTree.h"
#include "TH1.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "RecoHI/HiCentralityAlgos/interface/CentralityProvider.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
//

/**\class HiInclusiveJetAnalyzer

   \author Matt Nguyen
   \date   November 2010
*/




class HiInclusiveJetAnalyzer : public edm::EDProducer {
public:

  explicit HiInclusiveJetAnalyzer(const edm::ParameterSet&);

  ~HiInclusiveJetAnalyzer();

  virtual void produce(edm::Event&, const edm::EventSetup&);

  virtual void beginRun(const edm::Run & r, const edm::EventSetup & c);

  virtual void beginJob();

  void fillL1Bits(const edm::Event &iEvent);

  void fillHLTBits(const edm::Event &iEvent);

  template <typename TYPE>
    void getProduct(const std::string name, edm::Handle<TYPE> &prod,
		    const edm::Event &event) const;
  template <typename TYPE>
    bool getProductSafe(const std::string name, edm::Handle<TYPE> &prod,
			const edm::Event &event) const;


private:
  void fillEvent(edm::Event &iEvent);

  int getPFJetMuon(const pat::Jet& pfJet, const reco::PFCandidateCollection *pfCandidateColl);

  double getPtRel(const reco::PFCandidate lep, const pat::Jet& jet );

  void saveDaughters( const reco::GenParticle & gen);
  void saveDaughters( const reco::Candidate & gen);
  double getEt(math::XYZPoint pos, double energy);
  math::XYZPoint getPosition(const DetId &id, reco::Vertex::Point vtx = reco::Vertex::Point(0,0,0));
  int TaggedJet(reco::Jet calojet, edm::Handle<reco::JetTagCollection > jetTags );

  edm::InputTag   jetTag_, vtxTag_, genjetTag_, eventInfoTag_, L1gtReadout_, pfCandidateLabel_, trackTag_, matchTag_;
  edm::InputTag HcalRecHitHFSrc_;
  edm::InputTag HcalRecHitHBHESrc_;
  edm::InputTag EBSrc_;
  edm::InputTag EESrc_;
  edm::InputTag genParticleSrc_;

  std::vector<float> usedStringPts;

  /// verbose ?
  bool verbose_;
  bool doMatch_;
  bool useCentrality_;
  bool useVtx_;
  bool useJEC_;
  bool usePat_;
  bool isMC_;
  bool fillGenJets_;
  bool doTrigger_;
  bool useQuality_;
  std::string trackQuality_;

  bool doSubEvent_;
  double genPtMin_;
  bool doLifeTimeTagging_;
  bool doLifeTimeTaggingExtras_;
  bool saveBfragments_;
  bool skipCorrections_;

  bool doHiJetID_;
  bool doStandardJetID_;

  double rParam;
  double hardPtMin_;
  double jetPtMin_;

  //TTree *t;
  //edm::Service<TFileService> fs1;
  //std::auto_ptr<TTree> t;

  CentralityProvider * centrality_;
  const CaloGeometry *geo;

  std::string                   hltResName_;         //HLT trigger results name
  std::vector<std::string>      hltProcNames_;       //HLT process name(s)
  std::vector<std::string>      hltTrgNames_;        //HLT trigger name(s)

  std::vector<int>              hltTrgBits_;         //HLT trigger bit(s)
  std::vector<bool>             hltTrgDeci_;         //HLT trigger descision(s)
  std::vector<std::string>      hltTrgUsedNames_;    //HLT used trigger name(s)
  std::string                   hltUsedResName_;     //used HLT trigger results name

  std::string bTagJetName_;
  std::string ImpactParameterTagInfos_;
  std::string TrackCountingHighEffBJetTags_;
  std::string NegativeTrackCountingHighEffJetTags_;
  std::string TrackCountingHighPurBJetTags_;
  std::string NegativeTrackCountingHighPur_;
  std::string JetProbabilityBJetTags_;
  std::string PositiveOnlyJetProbabilityJetTags_;
  std::string NegativeOnlyJetProbabilityJetTags_;
  std::string JetBProbabilityBJetTags_;
  std::string NegativeOnlyJetBProbabilityJetTags_;
  std::string PositiveOnlyJetBProbabilityJetTags_;
  std::string SecondaryVertexTagInfos_;
  std::string SecondaryVertexNegativeTagInfos_;
  std::string SimpleSecondaryVertexHighEffBJetTags_;
  std::string SimpleSecondaryVertexNegativeHighEffBJetTags_;
  std::string SimpleSecondaryVertexHighPurBJetTags_;
  std::string SimpleSecondaryVertexNegativeHighPurBJetTags_;
  std::string CombinedSecondaryVertexBJetTags_;
  std::string CombinedSecondaryVertexNegativeBJetTags_;
  std::string CombinedSecondaryVertexPositiveBJetTags_;
  std::string NegativeSoftMuonByPtBJetTags_;
  std::string PositiveSoftMuonByPtBJetTags_;

  static const int MAXJETS = 500;
  static const int MAXTRACKS = 5000;
  static const int MAXHLTBITS = 5000;
  static const int MAXBFRAG = 500;

  struct JRA{

    std::auto_ptr<int> nref;
    std::auto_ptr<int> run;
    std::auto_ptr<int> evt;
    std::auto_ptr<int> lumi;
    std::auto_ptr<int> bin;
    std::auto_ptr<float> vx;
    std::auto_ptr<float> vy;
    std::auto_ptr<float> vz;
    std::auto_ptr<float> b;
    std::auto_ptr<float> hf;

    std::auto_ptr<std::vector<float> > rawpt;
    std::auto_ptr<std::vector<float> > jtpt;
    std::auto_ptr<std::vector<float> > jteta;
    std::auto_ptr<std::vector<float> > jtphi;
    std::auto_ptr<std::vector<float> > jty;
    std::auto_ptr<std::vector<float> > jtpu;
    std::auto_ptr<std::vector<float> > jtm;

    std::auto_ptr<std::vector<float> > trackMax;
    std::auto_ptr<std::vector<float> > trackSum;
    std::auto_ptr<std::vector<int> > trackN;

    std::auto_ptr<std::vector<float> > chargedMax;
    std::auto_ptr<std::vector<float> > chargedSum;
    std::auto_ptr<std::vector<int> > chargedN;

    std::auto_ptr<std::vector<float> > photonMax;
    std::auto_ptr<std::vector<float> > photonSum;
    std::auto_ptr<std::vector<int> > photonN;

    std::auto_ptr<std::vector<float> > trackHardSum;
    std::auto_ptr<std::vector<float> > chargedHardSum;
    std::auto_ptr<std::vector<float> > photonHardSum;

    std::auto_ptr<std::vector<int> > trackHardN;
    std::auto_ptr<std::vector<int> > chargedHardN;
    std::auto_ptr<std::vector<int> > photonHardN;

    std::auto_ptr<std::vector<float> > neutralMax;
    std::auto_ptr<std::vector<float> > neutralSum;
    std::auto_ptr<std::vector<int> > neutralN;

    std::auto_ptr<std::vector<float> > eMax;
    std::auto_ptr<std::vector<float> > eSum;
    std::auto_ptr<std::vector<int> > eN;

    std::auto_ptr<std::vector<float> > muMax;
    std::auto_ptr<std::vector<float> > muSum;
    std::auto_ptr<std::vector<int> > muN;

    std::auto_ptr<std::vector<float> > genChargedSum;
    std::auto_ptr<std::vector<float> > genHardSum;
    std::auto_ptr<std::vector<float> > signalChargedSum;
    std::auto_ptr<std::vector<float> > signalHardSum;

    std::auto_ptr<std::vector<float> > hcalSum;
    std::auto_ptr<std::vector<float> > ecalSum;


    std::auto_ptr<std::vector<float> > fHPD;
    std::auto_ptr<std::vector<float> > fRBX;
    std::auto_ptr<std::vector<int> > n90;
    std::auto_ptr<std::vector<float> > fSubDet1;
    std::auto_ptr<std::vector<float> > fSubDet2;
    std::auto_ptr<std::vector<float> > fSubDet3;
    std::auto_ptr<std::vector<float> > fSubDet4;
    std::auto_ptr<std::vector<float> > restrictedEMF;
    std::auto_ptr<std::vector<int> > nHCAL;
    std::auto_ptr<std::vector<int> > nECAL;
    std::auto_ptr<std::vector<float> > apprHPD;
    std::auto_ptr<std::vector<float> > apprRBX;

    //    std::auto_ptr<std::vector<int> > n90;
    std::auto_ptr<std::vector<int> > n2RPC;
    std::auto_ptr<std::vector<int> > n3RPC;
    std::auto_ptr<std::vector<int> > nRPC;

    std::auto_ptr<std::vector<float> > fEB;
    std::auto_ptr<std::vector<float> > fEE;
    std::auto_ptr<std::vector<float> > fHB;
    std::auto_ptr<std::vector<float> > fHE;
    std::auto_ptr<std::vector<float> > fHO;
    std::auto_ptr<std::vector<float> > fLong;
    std::auto_ptr<std::vector<float> > fShort;
    std::auto_ptr<std::vector<float> > fLS;
    std::auto_ptr<std::vector<float> > fHFOOT;


    std::auto_ptr<std::vector<int> > subid;

    std::auto_ptr<std::vector<float> > matchedPt;
    std::auto_ptr<std::vector<float> > matchedRawPt;
    std::auto_ptr<std::vector<float> > matchedR;
    std::auto_ptr<std::vector<float> > matchedPu;

    std::auto_ptr<std::vector<float> > discr_csvMva;
    std::auto_ptr<std::vector<float> > discr_csvSimple;
    std::auto_ptr<std::vector<float> > discr_muByIp3;
    std::auto_ptr<std::vector<float> > discr_muByPt;
    std::auto_ptr<std::vector<float> > discr_prob;
    std::auto_ptr<std::vector<float> > discr_probb;
    std::auto_ptr<std::vector<float> > discr_tcHighEff;
    std::auto_ptr<std::vector<float> > discr_tcHighPur;
    std::auto_ptr<std::vector<float> > discr_ssvHighEff;
    std::auto_ptr<std::vector<float> > discr_ssvHighPur;

    std::auto_ptr<std::vector<float> > ndiscr_ssvHighEff;
    std::auto_ptr<std::vector<float> > ndiscr_ssvHighPur;
    std::auto_ptr<std::vector<float> > ndiscr_csvSimple;
    std::auto_ptr<std::vector<float> > ndiscr_muByPt;
    std::auto_ptr<std::vector<float> > ndiscr_prob;
    std::auto_ptr<std::vector<float> > ndiscr_probb;
    std::auto_ptr<std::vector<float> > ndiscr_tcHighEff;
    std::auto_ptr<std::vector<float> > ndiscr_tcHighPur;

    std::auto_ptr<std::vector<float> > pdiscr_csvSimple;
    std::auto_ptr<std::vector<float> > pdiscr_prob;
    std::auto_ptr<std::vector<float> > pdiscr_probb;

    std::auto_ptr<std::vector<int> > nsvtx;
    std::auto_ptr<std::vector<int> > svtxntrk;
    std::auto_ptr<std::vector<float> > svtxdl;
    std::auto_ptr<std::vector<float> > svtxdls;
    std::auto_ptr<std::vector<float> > svtxm;
    std::auto_ptr<std::vector<float> > svtxpt;
    std::auto_ptr<std::vector<float> > svtxnormchi2;

    std::auto_ptr<std::vector<int> > nIPtrk;
    std::auto_ptr<std::vector<int> > nselIPtrk;

    std::auto_ptr<int> nIP;
    std::auto_ptr<std::vector<int> > ipJetIndex;
    std::auto_ptr<std::vector<float> > ipPt;
    std::auto_ptr<std::vector<float> > ipEta;
    std::auto_ptr<std::vector<float> > ipDxy;
    std::auto_ptr<std::vector<float> > ipDz;
    std::auto_ptr<std::vector<float> > ipChi2;
    std::auto_ptr<std::vector<int> > ipNHit;
    std::auto_ptr<std::vector<int> > ipNHitPixel;
    std::auto_ptr<std::vector<int> > ipNHitStrip;
    std::auto_ptr<std::vector<bool> > ipIsHitL1;
    std::auto_ptr<std::vector<float> > ipProb0;
    std::auto_ptr<std::vector<float> > ipProb1;
    std::auto_ptr<std::vector<float> > ip2d;
    std::auto_ptr<std::vector<float> > ip2dSig;
    std::auto_ptr<std::vector<float> > ip3d;
    std::auto_ptr<std::vector<float> > ip3dSig;
    std::auto_ptr<std::vector<float> > ipDist2Jet;
    std::auto_ptr<std::vector<float> > ipDist2JetSig;
    std::auto_ptr<std::vector<float> > ipClosest2Jet;

    std::auto_ptr<std::vector<float> > mue;
    std::auto_ptr<std::vector<float> > mupt;
    std::auto_ptr<std::vector<float> > mueta;
    std::auto_ptr<std::vector<float> > muphi;
    std::auto_ptr<std::vector<float> > mudr;
    std::auto_ptr<std::vector<float> > muptrel;
    std::auto_ptr<std::vector<int> > muchg;

    std::auto_ptr<std::vector<float> > discr_fr01;

    std::auto_ptr<std::vector<float> > refpt;
    std::auto_ptr<std::vector<float> > refeta;
    std::auto_ptr<std::vector<float> > refphi;
    std::auto_ptr<std::vector<float> > refy;
    std::auto_ptr<std::vector<float> > refdphijt;
    std::auto_ptr<std::vector<float> > refdrjt;
    std::auto_ptr<std::vector<float> > refparton_pt;
    std::auto_ptr<std::vector<int> > refparton_flavor;
    std::auto_ptr<std::vector<int> > refparton_flavorForB;

    std::auto_ptr<float> pthat;
    std::auto_ptr<int> beamId1;
    std::auto_ptr<int> beamId2;
    std::auto_ptr<int> ngen;
    std::auto_ptr<std::vector<int> > genmatchindex;
    std::auto_ptr<std::vector<float> > genpt;
    std::auto_ptr<std::vector<float> > geneta;
    std::auto_ptr<std::vector<float> > genphi;
    std::auto_ptr<std::vector<float> > geny;
    std::auto_ptr<std::vector<float> > gendphijt;
    std::auto_ptr<std::vector<float> > gendrjt;
    std::auto_ptr<std::vector<int> > gensubid;

    // hlt
    std::auto_ptr<int> nHLTBit;
    std::auto_ptr<std::vector<bool> > hltBit;

    // l1
    std::auto_ptr<int> nL1TBit;
    std::auto_ptr<std::vector<bool> > l1TBit;
    std::auto_ptr<int> nL1ABit;
    std::auto_ptr<std::vector<bool> > l1ABit;

    std::auto_ptr<int> bMult;
    std::auto_ptr<std::vector<int> > bJetIndex;
    std::auto_ptr<std::vector<int> > bStatus;
    std::auto_ptr<std::vector<int> > bPdg;
    std::auto_ptr<std::vector<int> > bChg;
    std::auto_ptr<std::vector<float> > bVx;
    std::auto_ptr<std::vector<float> > bVy;
    std::auto_ptr<std::vector<float> > bVz;
    std::auto_ptr<std::vector<float> > bPt;
    std::auto_ptr<std::vector<float> > bEta;
    std::auto_ptr<std::vector<float> > bPhi;


  };

  JRA jets_;

};

#endif
