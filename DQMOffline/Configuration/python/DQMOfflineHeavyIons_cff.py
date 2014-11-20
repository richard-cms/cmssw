import FWCore.ParameterSet.Config as cms

from DQMServices.Components.DQMMessageLogger_cfi import *
from DQMServices.Components.DQMDcsInfo_cfi import *
from DQMServices.Components.DQMFastTimerService_cff import *

from DQMOffline.Ecal.ecal_dqm_source_offline_HI_cff import *
from DQM.HcalMonitorModule.hcal_dqm_source_fileT0_HeavyIons_cff import *
from DQM.SiStripMonitorClient.SiStripSourceConfigTier0_HeavyIons_cff import *
from DQM.SiPixelCommon.SiPixelOfflineDQM_source_cff import *
from DQM.DTMonitorModule.dtDQMOfflineSources_cff import *
from DQM.RPCMonitorClient.RPCTier0Source_cff import *
from DQM.CSCMonitorModule.csc_dqm_sourceclient_offline_cff import *
from DQM.EcalPreshowerMonitorModule.es_dqm_source_offline_cff import *
from DQM.BeamMonitor.AlcaBeamMonitorHeavyIons_cff import *
from DQMOffline.L1Trigger.L1TriggerDqmOffline_cff import *

DQMOfflineHeavyIonsPreDPG = cms.Sequence( dqmDcsInfo *
                                          l1TriggerDqmOffline * # L1 emulator is run within this sequence for real data
                                          ecal_dqm_source_offline *
                                          hcalOfflineDQMSource *
                                          SiStripDQMTier0_hi *
                                          siPixelOfflineDQM_heavyions_source *
                                          dtSources *
                                          rpcTier0Source *
                                          cscSources *
                                          es_dqm_source_offline )

DQMOfflineHeavyIonsDPG = cms.Sequence( DQMOfflineHeavyIonsPreDPG *
                                       DQMMessageLogger )

from DQMOffline.Muon.muonMonitors_cff import *
from DQMOffline.JetMET.jetMETDQMOfflineSourceHI_cff import *
from DQMOffline.EGamma.egammaDQMOffline_cff import *
from DQMOffline.Trigger.DQMOffline_Trigger_cff import *
#from DQMOffline.RecoB.PrimaryVertexMonitor_cff import *
from DQM.Physics.DQMPhysics_cff import *
from DQM.TrackingMonitorSource.TrackingSourceConfig_Tier0_HeavyIons_cff import *


#triggerOfflineDQMSource.remove(jetMETHLTOfflineAnalyzer)
#ak4CaloL1FastjetCorrector.srcRho = cms.InputTag("hltAK4CaloJets:rho")
#ak4PFL1FastjetCorrector.srcRho = cms.InputTag("hltAK4PFJets:rho")
triggerOfflineDQMSource.remove(ak4CaloL1FastjetCorrector)
triggerOfflineDQMSource.remove(ak4CaloL1FastjetCorrector)
ak4CaloL1FastL2L3Corrector.correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
ak4CaloL1FastL2L3ResidualCorrector.correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
triggerOfflineDQMSource.remove(ak4PFL1FastjetCorrector)
triggerOfflineDQMSource.remove(ak4PFL1FastjetCorrector)
ak4PFL1FastL2L3Corrector.correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
ak4PFL1FastL2L3ResidualCorrector.correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")



egammaDQMOffline.remove(electronAnalyzerSequence)
egammaDQMOffline.remove(zmumugammaAnalysis)
egammaDQMOffline.remove(zmumugammaOldAnalysis)
egammaDQMOffline.remove(photonAnalysis)
stdPhotonAnalysis.isHeavyIon = True
stdPhotonAnalysis.barrelRecHitProducer = cms.InputTag("ecalRecHit", "EcalRecHitsEB")
stdPhotonAnalysis.endcapRecHitProducer = cms.InputTag("ecalRecHit", "EcalRecHitsEE")
hltResults.RecHitsEBTag = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEB")
hltResults.RecHitsEETag = cms.untracked.InputTag("ecalRecHit", "EcalRecHitsEE")


globalAnalyzer.inputTags.offlinePVs = cms.InputTag("hiSelectedVertex")
trackerAnalyzer.inputTags.offlinePVs = cms.InputTag("hiSelectedVertex")
tightAnalyzer.inputTags.offlinePVs = cms.InputTag("hiSelectedVertex")
looseAnalyzer.inputTags.offlinePVs = cms.InputTag("hiSelectedVertex")


DQMOfflineHeavyIonsPrePOG = cms.Sequence( muonMonitors
                                          * TrackMonDQMTier0_hi
                                          * jetMETDQMOfflineSource
                                          * egammaDQMOffline
                                          * triggerOfflineDQMSource
                                          #* pvMonitor
                                          * alcaBeamMonitor
                                          * dqmPhysicsHI
                                          )

DQMOfflineHeavyIonsPOG = cms.Sequence( DQMOfflineHeavyIonsPrePOG *
                                       DQMMessageLogger )

DQMOfflineHeavyIons = cms.Sequence( DQMOfflineHeavyIonsPreDPG *
                                    DQMOfflineHeavyIonsPrePOG *
                                    DQMMessageLogger )

#DQMOfflineHeavyIonsPhysics = cms.Sequence( dqmPhysics )
