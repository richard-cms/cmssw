import FWCore.ParameterSet.VarParsing as VarParsing

ivars = VarParsing.VarParsing('standard')
ivars.files = ''
ivars.output = ''
ivars.maxEvents = 1000
ivars.register ('randomNumber',
                                mult=ivars.multiplicity.singleton,
                                info="for testing")

ivars.register ('initialEvent',
                                mult=ivars.multiplicity.singleton,
                                info="for testing")

ivars.randomNumber=13
ivars.initialEvent=1
ivars.parseArguments()

import FWCore.ParameterSet.Config as cms

process = cms.Process("ANA")

process.option = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )            
process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration/StandardSequences/Generator_cff')
process.load('Configuration/StandardSequences/VtxSmeared')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
#process.load("Configuration.Generator.Hydjet_Quenched_MinBias_4TeV_cfi")
#process.load("Configuration/Generator/PythiaMinBias_cfi")

#process.load('Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt0_eta30_TuneZ2_Unquenched_2760GeV_cfi')
process.load(ivars.files[0])

process.generator = process.hiSignal.clone()
process.generator.embeddingMode = False
process.generator.doIsospin = False

process.source = cms.Source('EmptySource',
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(ivars.maxEvents)
)

process.RandomNumberGeneratorService.generator.initialSeed = ivars.randomNumber

process.SimpleMemoryCheck = cms.Service('SimpleMemoryCheck',
                                        ignoreTotal=cms.untracked.int32(0),
                                        oncePerEventMode = cms.untracked.bool(False)
                                        )

#process.ana = cms.EDAnalyzer('HydjetAnalyzer')

process.genpana = cms.EDAnalyzer("GenParticleCounter",
                                 src = cms.untracked.string("genParticles"),
                                 doCentrality = cms.untracked.bool(False),
                                 VertexProducer = cms.untracked.string("hiSelectedVertex")
                                 )

process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')

process.p = cms.Path(process.generator* process.genParticles* process.genpana)


process.TFileService = cms.Service("TFileService",
                                   #fileName=cms.string("Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt15_eta30_TuneZ2_Unquenched_2760GeV.root")
                                   fileName=cms.string(ivars.output))











