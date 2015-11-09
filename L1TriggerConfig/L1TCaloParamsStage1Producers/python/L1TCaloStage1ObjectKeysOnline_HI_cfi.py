import FWCore.ParameterSet.Config as cms

L1TCaloStage1ObjectKeysOnlineHI = cms.ESProducer("L1TCaloStage1ObjectKeysOnlineProdHI",
    onlineAuthentication = cms.string('.'),
    subsystemLabel = cms.string('S1CALOL2'),
    onlineDB = cms.string('oracle://CMS_OMDS_LB/CMS_TRG_R')
)
