// -*- C++ -*-
//
// Package:    DQMOffline/ecalMultiftAnalyzer
// Class:      ecalMultiftAnalyzer
//
/**\class ecalMultiftAnalyzer ecalMultiftAnalyzer.cc DQMOffline/ecalMultiftAnalyzer/plugins/ecalMultiftAnalyzer.cc

   Description: [one line class summary]

   Implementation:
   [Notes on implementation]
*/
//
// Original Author:  R. Alex Barbieri
//         Created:  Tue, 17 Nov 2015 17:18:50 GMT
//
//


// system include files
#include <memory>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/JetReco/interface/CaloJetCollection.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"

#include "Geometry/CaloEventSetup/interface/CaloTopologyRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloTopology/interface/CaloTopology.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Math/interface/deltaR.h"

#include <TH1F.h>
#include <TProfile.h>

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class ecalMultiftAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit ecalMultiftAnalyzer(const edm::ParameterSet&);
  ~ecalMultiftAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;

  // ----------member data ---------------------------
  edm::Service<TFileService> fs;

  edm::EDGetTokenT<reco::CaloJetCollection> caloJetToken_;
  edm::EDGetTokenT<std::vector<reco::Photon> > recoPhotonsCollection_;
  edm::EDGetTokenT<EcalRecHitCollection> RecHitCollection_EB_;
  edm::EDGetTokenT<EcalRecHitCollection> RecHitCollection_EE_;

  edm::ESHandle<CaloGeometry> geomH;

  TH1F *eb_chi2;
  TProfile *eb_chi2_eta;
  TH1F *eb_chi2_e5;
  TProfile *eb_chi2_e5_eta;
  TH1F *eb_errors;
  TProfile *eb_errors_eta;
  TH1F *eb_errors_e5;
  TProfile *eb_errors_e5_eta;
  TH1F *eb_chi2_photon15;
  TH1F *eb_errors_photon15;
  TH1F *eb_chi2_jet30;
  TH1F *eb_errors_jet30;

  TH1F *ee_chi2;
  TProfile *ee_chi2_eta;
  TH1F *ee_chi2_e5;
  TProfile *ee_chi2_e5_eta;
  TH1F *ee_errors;
  TProfile *ee_errors_eta;
  TH1F *ee_errors_e5;
  TProfile *ee_errors_e5_eta;
  TH1F *ee_chi2_photon15;
  TH1F *ee_errors_photon15;
  TH1F *ee_chi2_jet30;
  TH1F *ee_errors_jet30;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
ecalMultiftAnalyzer::ecalMultiftAnalyzer(const edm::ParameterSet& iConfig)
{
  //now do what ever initialization is needed
  usesResource("TFileService");
  recoPhotonsCollection_  = consumes<std::vector<reco::Photon> > (iConfig.getParameter<edm::InputTag>("recoPhotonSrc"));
  caloJetToken_ =  consumes<reco::CaloJetCollection>(iConfig.getParameter<edm::InputTag> ("recoJetSrc"));
  RecHitCollection_EB_       = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("RecHitCollection_EB"));
  RecHitCollection_EE_       = consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("RecHitCollection_EE"));
}


ecalMultiftAnalyzer::~ecalMultiftAnalyzer()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
ecalMultiftAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  iSetup.get<CaloGeometryRecord>().get(geomH);

  edm::Handle<std::vector<reco::Photon> > recoPhotonsHandle;
  iEvent.getByToken(recoPhotonsCollection_, recoPhotonsHandle);

  edm::Handle<reco::CaloJetCollection> recoJetHandle;
  iEvent.getByToken(caloJetToken_, recoJetHandle);

  edm::Handle<EcalRecHitCollection> ebHandle;
  iEvent.getByToken(RecHitCollection_EB_, ebHandle);

  edm::Handle<EcalRecHitCollection> eeHandle;
  iEvent.getByToken(RecHitCollection_EE_, eeHandle);

  for(EcalRecHitCollection::const_iterator hit = ebHandle->begin(); hit != ebHandle->end(); ++hit) {
    eb_chi2->Fill(hit->chi2() );
    eb_errors->Fill(hit->energyError() );
    double eta = geomH->getGeometry(hit->detid())->getPosition().eta();
    double phi = geomH->getGeometry(hit->detid())->getPosition().phi();
    eb_chi2_eta->Fill(eta, hit->chi2() );
    eb_errors_eta->Fill(eta, hit->energyError() );
    if(hit->energy() > 5)
    {
      eb_chi2_e5->Fill(hit->chi2() );
      eb_errors_e5->Fill(hit->energyError() );
      eb_chi2_e5_eta->Fill(eta, hit->chi2() );
      eb_errors_e5_eta->Fill(eta, hit->energyError() );
    }

    for (std::vector<reco::Photon>::const_iterator pho = recoPhotonsHandle->begin(); pho != recoPhotonsHandle->end(); ++pho) {
      if(pho->et() < 15 ) continue;
      double dr = reco::deltaR(eta, phi, pho->eta(), pho->phi());
      if(dr < 0.1)
      {
	eb_chi2_photon15->Fill(hit->chi2() );
	eb_errors_photon15->Fill(hit->energyError() );
      }
    }
    for (std::vector<reco::CaloJet>::const_iterator jet = recoJetHandle->begin(); jet != recoJetHandle->end(); ++jet) {
      if(jet->pt() < 30 ) continue;
      double dr = reco::deltaR(eta, phi, jet->eta(), jet->phi());
      if(dr < 0.4)
      {
	eb_chi2_jet30->Fill(hit->chi2() );
	eb_errors_jet30->Fill(hit->energyError() );
      }
    }
  }

  for(EcalRecHitCollection::const_iterator hit = eeHandle->begin(); hit != eeHandle->end(); ++hit) {
    ee_chi2->Fill(hit->chi2() );
    ee_errors->Fill(hit->energyError() );
    double eta = geomH->getGeometry(hit->detid())->getPosition().eta();
    double phi = geomH->getGeometry(hit->detid())->getPosition().phi();
    ee_chi2_eta->Fill(eta, hit->chi2() );
    ee_errors_eta->Fill(eta, hit->energyError() );
    if(hit->energy() > 5)
    {
      ee_chi2_e5->Fill(hit->chi2() );
      ee_errors_e5->Fill(hit->energyError() );
      ee_chi2_e5_eta->Fill(eta, hit->chi2() );
      ee_errors_e5_eta->Fill(eta, hit->energyError() );
    }

    for (std::vector<reco::Photon>::const_iterator pho = recoPhotonsHandle->begin(); pho != recoPhotonsHandle->end(); ++pho) {
      if(pho->et() < 15 ) continue;
      double dr = reco::deltaR(eta, phi, pho->eta(), pho->phi());
      if(dr < 0.1)
      {
	ee_chi2_photon15->Fill(hit->chi2() );
	ee_errors_photon15->Fill(hit->energyError() );
      }
    }
    for (std::vector<reco::CaloJet>::const_iterator jet = recoJetHandle->begin(); jet != recoJetHandle->end(); ++jet) {
      if(jet->pt() < 30 ) continue;
      double dr = reco::deltaR(eta, phi, jet->eta(), jet->phi());
      if(dr < 0.4)
      {
	ee_chi2_jet30->Fill(hit->chi2() );
	ee_errors_jet30->Fill(hit->energyError() );
      }
    }
  }
}


// ------------ method called once each job just before starting event loop  ------------
void
ecalMultiftAnalyzer::beginJob()
{
  const int nBins = 100;
  const float maxChi2 = 70;
  const float maxError = 0.2;
  //bookHistos();
  eb_chi2 = fs->make<TH1F>("rechit_eb_chi2","Rechit eb_chi2;chi2 fit value;",nBins,0,maxChi2);
  eb_chi2_eta = fs->make<TProfile>("rechit_eb_chi2_eta","Rechit eb_chi2 vs. eta;eta;mean chi2",nBins,-5,5);
  eb_chi2_e5 = fs->make<TH1F>("rechit_eb_chi2_e5","Rechit eb_chi2, e>5GeV;chi2 fit value;",nBins,0,maxChi2);
  eb_chi2_e5_eta = fs->make<TProfile>("rechit_eb_chi2_e5_eta","Rechit eb_chi2 vs. eta, e>5GeV;eta;mean chi2",nBins,-5,5);
  eb_errors = fs->make<TH1F>("rechit_eb_errors","Rechit eb_errors;error on the energy;",nBins,0,maxError);
  eb_errors_eta = fs->make<TProfile>("rechit_eb_errors_eta","Rechit eb_errors vs. eta;eta;mean errors",nBins,-5,5);
  eb_errors_e5 = fs->make<TH1F>("rechit_eb_errors_e5","Rechit eb_errors, e>5GeV;error on the energy;",nBins,0,maxError);
  eb_errors_e5_eta = fs->make<TProfile>("rechit_eb_errors_e5_eta","Rechit eb_errors vs. eta, e>5GeV;eta;mean errors",nBins,-5,5);
  eb_chi2_photon15 = fs->make<TH1F>("rechit_eb_chi2_photon15","Rechit eb_chi2 near photons;chi2 fit value;",nBins,0,maxChi2);
  eb_errors_photon15 = fs->make<TH1F>("rechit_eb_errors_photon15","Rechit eb_errors near photons;error on the energy;",nBins,0,maxError);
  eb_chi2_jet30 = fs->make<TH1F>("rechit_eb_chi2_jet30","Rechit eb_chi2 near jets;chi2 fit value;",nBins,0,maxChi2);
  eb_errors_jet30 = fs->make<TH1F>("rechit_eb_errors_jet30","Rechit eb_errors near jets;error on the energy;",nBins,0,maxError);

  ee_chi2 = fs->make<TH1F>("rechit_ee_chi2","Rechit ee_chi2;chi2 fit value;",nBins,0,maxChi2);
  ee_chi2_eta = fs->make<TProfile>("rechit_ee_chi2_eta","Rechit ee_chi2 vs. eta;eta;mean chi2",nBins,-5,5);
  ee_chi2_e5 = fs->make<TH1F>("rechit_ee_chi2_e5","Rechit ee_chi2, e>5GeV;chi2 fit value;",nBins,0,maxChi2);
  ee_chi2_e5_eta = fs->make<TProfile>("rechit_ee_chi2_e5_eta","Rechit ee_chi2 vs. eta, e>5GeV;eta;mean chi2",nBins,-5,5);
  ee_errors = fs->make<TH1F>("rechit_ee_errors","Rechit ee_errors;error on the energy;",nBins,0,maxError);
  ee_errors_eta = fs->make<TProfile>("rechit_ee_errors_eta","Rechit ee_errors vs. eta;eta;mean errors",nBins,-5,5);
  ee_errors_e5 = fs->make<TH1F>("rechit_ee_errors_e5","Rechit ee_errors, e>5GeV;error on the energy;",nBins,0,maxError);
  ee_errors_e5_eta = fs->make<TProfile>("rechit_ee_errors_e5_eta","Rechit ee_errors vs. eta, e>5GeV;eta;mean errors",nBins,-5,5);
  ee_chi2_photon15 = fs->make<TH1F>("rechit_ee_chi2_photon15","Rechit ee_chi2 near photons;chi2 fit value;",nBins,0,maxChi2);
  ee_errors_photon15 = fs->make<TH1F>("rechit_ee_errors_photon15","Rechit ee_errors near photons;error on the energy;",nBins,0,maxError);
  ee_chi2_jet30 = fs->make<TH1F>("rechit_ee_chi2_jet30","Rechit ee_chi2 near jets;chi2 fit value;",nBins,0,maxChi2);
  ee_errors_jet30 = fs->make<TH1F>("rechit_ee_errors_jet30","Rechit ee_errors near jets;error on the energy;",nBins,0,maxError);

}

// ------------ method called once each job just after ending the event loop  ------------
void
ecalMultiftAnalyzer::endJob()
{

}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
ecalMultiftAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ecalMultiftAnalyzer);
