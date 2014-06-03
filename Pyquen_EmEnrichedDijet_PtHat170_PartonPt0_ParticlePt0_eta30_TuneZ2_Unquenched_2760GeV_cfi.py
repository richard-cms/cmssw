import FWCore.ParameterSet.Config as cms

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
                        particlePt = cms.vdouble(0, 0, 0, 0),
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
                            myParameters = cms.vstring(),
                            customProcesses = cms.vstring('MSEL=0   ! User processes'),
                            ppDefault = cms.vstring('MSEL=1   ! QCD hight pT processes (only jets)',
                                                    'CKIN(3)=6.',
                                                    'MSTP(81)=0'),
                            pythiaUESettingsZ2Tune = cms.vstring(
                                'MSTU(21)=1     ! Check on possible errors during program execution',
                                'MSTJ(22)=2     ! Decay those unstable particles',
                                'PARJ(71)=10 .  ! for which ctau  10 mm',
                                'MSTP(33)=0     ! no K factors in hard cross sections',
                                'MSTP(2)=1      ! which order running alphaS',
                                'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                                'MSTP(52)=2     ! work with LHAPDF',
                                'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
                                'PARP(89)=1800. ! sqrts for which PARP82 is set',
                                'PARP(90)=0.275 ! Multiple interactions: rescaling power',
                                'MSTP(95)=6     ! CR (color reconnection parameters)',
                                'PARP(77)=1.016 ! CR',
                                'PARP(78)=0.538 ! CR',
                                'PARP(80)=0.1   ! Prob. colored parton from BBR',
                                'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
                                'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
                                'PARP(62)=1.025 ! ISR cutoff',
                                'MSTP(91)=1     ! Gaussian primordial kT',
                                'PARP(93)=10.0  ! primordial kT-max',
                                'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
                                'MSTP(82)=4     ! Defines the multi-parton model'),
                            pythiaPromptPhotons = cms.vstring('MSUB(14)=1',
                                                              'MSUB(18)=1',
                                                              'MSUB(29)=1',
                                                              'MSUB(114)=1',
                                                              'MSUB(115)=1'),
                            pythiaJets = cms.vstring('MSUB(11)=1',
                                                     'MSUB(12)=1',
                                                     'MSUB(13)=1',
                                                     'MSUB(28)=1',
                                                     'MSUB(53)=1',
                                                     'MSUB(68)=1'),
                            hydjetPythiaDefault = cms.vstring('MSEL=0   ! user processes',
                                                              'CKIN(3)=6.',
                                                              'MSTP(81)=0'),
                            ppJets = cms.vstring('MSEL=1   ! QCD hight pT processes'),
                            parameterSets = cms.vstring('pythiaUESettingsZ2Tune',
                                                        'ppJets',
                                                        'kinematics'),

                            kinematics = cms.vstring('CKIN(3)=170',
                                 'CKIN(4)=9999'
                                                 )
                        )
)


hiSignal.embeddingMode = True
ProductionFilterSequence = cms.Sequence(hiSignal)
