import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.Geometry.GeometryIdeal_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://xrootd.cmsaf.mit.edu//store/user/richard/GlobalEcalRECO/HIRun2011_HLT_HIJet80-GlobalEcalReco/HIHighPt/HIRun2011_HLT_HIJet80-GlobalEcalReco/151115_183318/0000/step2_RAW2DIGI_L1Reco_RECO_127.root'
    )
)

process.load('DQMOffline.ecalMultiftAnalyzer.CfiFile_cfi')


process.p = cms.Path(process.ecalMultiftAnalyzer)

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("ecalAnalyzer.root"))
