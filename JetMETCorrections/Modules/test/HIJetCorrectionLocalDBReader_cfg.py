import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")
process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1)
        )

process.source = cms.Source("EmptySource")

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK3PF'),
            label  = cms.untracked.string('AK3PFLocal')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK4PF'),
            label  = cms.untracked.string('AK4PFLocal')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK4Calo'),
            label  = cms.untracked.string('AK4CaloLocal')
            ),
      cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK3Calo'),
            label  = cms.untracked.string('AK3CaloLocal')
            ),
      ),

      connect = cms.string('sqlite_file:JEC_GAMMAJET_Pbp_v1_STARTHI53_LV1.db')
)


process.demo1 = cms.EDAnalyzer('JetCorrectorDBReader',
        payloadName    = cms.untracked.string('AK3CaloLocal'),
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True),
        globalTag      = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20')
)


process.demo2 = cms.EDAnalyzer('JetCorrectorDBReader',
        payloadName    = cms.untracked.string('AK4PFLocal'),
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True),
        globalTag      = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20')
)

process.demo3 = cms.EDAnalyzer('JetCorrectorDBReader',
        payloadName    = cms.untracked.string('AK4CaloLocal'),
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True),
        globalTag      = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20')
)

process.demo4 = cms.EDAnalyzer('JetCorrectorDBReader',
        payloadName    = cms.untracked.string('AK3PFLocal'),
        printScreen    = cms.untracked.bool(False),
        createTextFile = cms.untracked.bool(True),
        globalTag      = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20')
)


process.p = cms.Path(process.demo1 * process.demo2 * process.demo3 * process.demo4)
