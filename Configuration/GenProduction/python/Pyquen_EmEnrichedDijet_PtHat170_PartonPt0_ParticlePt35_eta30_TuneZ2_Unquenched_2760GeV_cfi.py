import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.HI.PyquenTuneZ2Settings_cff import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
                        filterType = cms.untracked.string('EcalGenEvtSelector'),
                        partons = cms.vint32(1, 2, 3, 4, 5, 6, #quarks
                                             21, 22), #gluon, photon
                        partonPt = cms.vdouble(0, 0, 0, 0, 0, 0,
                                               0, 0),
                        partonStatus = cms.vint32(2, 2, 2, 2, 2, 2,
                                                  2, 1), 
                        particles = cms.vint32(221, #eta
                                               331, #eta'
                                               223, #omega
                                               111), #pi0
                        particlePt = cms.vdouble(35, 35, 35, 35),
                        particleStatus = cms.vint32(2, #eta
                                                    2, #eta'
                                                    2, #omega
                                                    2), #pi0
                        etaMax = cms.double(3.0),   # Photon eta cut
                        aBeamTarget = cms.double(208.0),
                        comEnergy = cms.double(2760.0),
                        qgpInitialTemperature = cms.double(1.0),
                        doCollisionalEnLoss = cms.bool(False),
                        qgpNumQuarkFlavor = cms.int32(0),
                        qgpProperTimeFormation = cms.double(0.1),
                        numQuarkFlavor = cms.int32(0),
                        hadronFreezoutTemperature = cms.double(0.14),
                        doRadiativeEnLoss = cms.bool(True),
                        backgroundLabel = cms.InputTag("generator"),
                        embeddingMode = cms.bool(True),
                        angularSpectrumSelector = cms.int32(0),
                        doIsospin = cms.bool(True),
                        doQuench = cms.bool(False),
                        cFlag = cms.int32(0),
                        bFixed = cms.double(0.0),
                        bMin = cms.double(0.0),
                        bMax = cms.double(0.0),
                        maxTries = cms.untracked.int32(5000),
                        PythiaParameters = cms.PSet(
                            ppJets = cms.vstring('MSEL=1   ! QCD high pT processes'),
                            parameterSets = cms.vstring('pythiaUESettings'
                                                        'ppJets',
                                                        'kinematics'),

                            kinematics = cms.vstring('CKIN(3)=170',
                                                     'CKIN(4)=9999'
                                                 )
                        )
)


hiSignal.embeddingMode = True
ProductionFilterSequence = cms.Sequence(hiSignal)
