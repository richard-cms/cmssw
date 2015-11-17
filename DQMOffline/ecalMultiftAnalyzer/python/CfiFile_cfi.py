import FWCore.ParameterSet.Config as cms

ecalMultiftAnalyzer = cms.EDAnalyzer('ecalMultiftAnalyzer',
                                     recoPhotonSrc = cms.InputTag('photons'),
                                     recoJetSrc = cms.InputTag('akVs4CaloJets'),
                                     RecHitCollection_EB = cms.InputTag('ecalRecHit:EcalRecHitsEB'),
                                     RecHitCollection_EE = cms.InputTag('ecalRecHit:EcalRecHitsEE')
)
