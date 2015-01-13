import FWCore.ParameterSet.Config as cms
process = cms.Process('jecdb')
process.load('CondCore.DBCommon.CondDBCommon_cfi')
process.CondDBCommon.connect = 'sqlite_file:JEC_GAMMAJET_pp_v1_STARTHI53_LV1.db'
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source('EmptySource')
process.PoolDBOutputService = cms.Service('PoolDBOutputService',
   process.CondDBCommon,
   toPut = cms.VPSet(
    cms.PSet(
    record = cms.string('AK3PF'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK3PF'),
    label  = cms.string('AK3PF')
    ),
    cms.PSet(
    record = cms.string('AK4PF'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK4PF'),
    label  = cms.string('AK4PF')
    ),
    cms.PSet(
    record = cms.string('AK5PF'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK5PF'),
    label  = cms.string('AK5PF')
    ),
    cms.PSet(
    record = cms.string('AK3Calo'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK3Calo'),
    label  = cms.string('AK3Calo')
    ),
    cms.PSet(
    record = cms.string('AK4Calo'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK4Calo'),
    label  = cms.string('AK4Calo')
    ),
    cms.PSet(
    record = cms.string('AK5Calo'),
    tag    = cms.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20_AK5Calo'),
    label  = cms.string('AK5Calo')
    ),
  )
)


process.dbWriterAK3PF = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK3PF')
)
process.dbWriterAK4PF = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK4PF')
)
process.dbWriterAK5PF = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK5PF')
)


process.dbWriterAK3Calo = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK3Calo')
)
process.dbWriterAK4Calo = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK4Calo')
)
process.dbWriterAK5Calo = cms.EDAnalyzer('JetCorrectorDBWriter',
   era    = cms.untracked.string('JEC_gammajet_HiWinter13_STARTHI53_LV1_5_3_20'),
   algo   = cms.untracked.string('AK5Calo')
)


process.p = cms.Path(
    process.dbWriterAK3PF *
    process.dbWriterAK4PF *
    process.dbWriterAK5PF *
    process.dbWriterAK3Calo *
    process.dbWriterAK4Calo *
    process.dbWriterAK5Calo
)
