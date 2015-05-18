#ifndef HiEgammaAlgos_RxCalculator_h
#define HiEgammaAlgos_RxCalculator_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"

#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"

class RxCalculator
{
public:

  RxCalculator(const edm::Event &iEvent, const edm::EventSetup &iSetup,
	       const edm::Handle<HBHERecHitCollection> hbhe,
	       const edm::Handle<HFRecHitCollection> hfLabel,
	       const edm::Handle<HORecHitCollection> hoLabel) ;

  double getRx (const reco::SuperClusterRef clus, const double i, const double threshold, const double innerR=0.0);
  double getCRx(const reco::SuperClusterRef clus, const double i, const double threshold, const double innerR=0.0); // background subtracted Rx

private:

  const HBHERecHitCollection         *fHBHERecHits_;
  const HORecHitCollection           *fHORecHits_;
  const HFRecHitCollection           *fHFRecHits_;
  const CaloGeometry                 *geometry_;
};

#endif
