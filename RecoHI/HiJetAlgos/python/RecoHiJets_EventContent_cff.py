import FWCore.ParameterSet.Config as cms

#Full Event content ---- temporary
RecoHiJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_*CaloJets_*_*',
                                           'keep *_*PFJets_*_*',
                                           'keep *_*HiGenJets_*_*',
                                           'keep *_*voronoiBackground*_*_*'
                                           )
    )

RecoHiJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_*CaloJets_*_*',
                                           'keep *_*PFJets_*_*',
                                           'keep *_*HiGenJets_*_*',
                                           'keep *_*voronoiBackground*_*_*'
                                           )
    )




