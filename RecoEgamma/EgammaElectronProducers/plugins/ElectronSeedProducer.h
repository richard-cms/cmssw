#ifndef ElectronSeedProducer_h
#define ElectronSeedProducer_h

//
// Package:         RecoEgamma/ElectronTrackSeedProducers
// Class:           ElectronSeedProducer
//
// Description:     Calls ElectronSeedGenerator
//                  to find TrackingSeeds.


class ElectronSeedGenerator ;
class SeedFilter ;
class EgammaHcalIsolation ;
class ElectronHcalHelper ;

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/CaloTopology/interface/CaloTopology.h"
#include "RecoCaloTools/MetaCollections/interface/CaloRecHitMetaCollections.h"
#include "RecoCaloTools/Selectors/interface/CaloDualConeSelector.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
namespace edm
 {
  class ConfigurationDescriptions ;
 }

#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperCluster.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeedCollection.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Common/interface/Handle.h"

#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

class ElectronSeedProducer : public edm::EDProducer
 {
  public:

    //static void fillDescriptions( edm::ConfigurationDescriptions & ) ;

    explicit ElectronSeedProducer( const edm::ParameterSet & ) ;
    virtual void beginRun( edm::Run &, edm::EventSetup const & ) ;
    virtual void endRun( edm::Run &, edm::EventSetup const & ) ;
    virtual ~ElectronSeedProducer() ;

    virtual void produce( edm::Event &, const edm::EventSetup & ) ;

  private:

    void filterClusters
     ( const reco::BeamSpot & bs,
       const edm::Handle<reco::SuperClusterCollection> & superClusters,
       /*HBHERecHitMetaCollection*mhbhe,*/ reco::SuperClusterRefVector &sclRefs,
       std::vector<float> & hoe1s, std::vector<float> & hoe2s,
       edm::Event &, const edm::EventSetup &) ;
    void filterSeeds(edm::Event& e, const edm::EventSetup& setup, reco::SuperClusterRefVector &sclRefs);

    edm::InputTag superClusters_[2] ;
    edm::InputTag initialSeeds_ ;
    edm::InputTag beamSpotTag_ ;
    edm::InputTag ebRecHitCollection_;
    edm::InputTag eeRecHitCollection_;

    edm::ParameterSet conf_ ;
    ElectronSeedGenerator * matcher_ ;
    SeedFilter * seedFilter_;

    TrajectorySeedCollection * theInitialSeedColl ;

    // for the filter

    // H/E
  //  edm::InputTag hcalRecHits_;
    bool applyHOverECut_ ;
    ElectronHcalHelper * hcalHelper_ ;
  //  edm::ESHandle<CaloGeometry> caloGeom_ ;
  //  unsigned long long caloGeomCacheId_ ;
    edm::ESHandle<CaloGeometry> caloGeom_ ;
    unsigned long long caloGeomCacheId_ ;
    edm::ESHandle<CaloTopology> caloTopo_;
    unsigned long long caloTopoCacheId_;
  //  EgammaHcalIsolation * hcalIso_ ;
  ////  CaloDualConeSelector * doubleConeSel_ ;
  //  HBHERecHitMetaCollection * mhbhe_ ;
  //  double maxHOverE_ ;
     double maxHOverEBarrel_ ;
     double maxHOverEEndcaps_ ;
     double maxHBarrel_ ;
     double maxHEndcaps_ ;
  //  double hOverEConeSize_;
  //  double hOverEHBMinE_;
  //  double hOverEHFMinE_;

    // super cluster Et cut
    double SCEtCut_;

    bool applySigmaIEtaIEtaCut_;
    double maxSigmaIEtaIEtaBarrel_;
    double maxSigmaIEtaIEtaEndcaps_;

    bool fromTrackerSeeds_;
    bool prefilteredSeeds_;

 } ;

#endif
