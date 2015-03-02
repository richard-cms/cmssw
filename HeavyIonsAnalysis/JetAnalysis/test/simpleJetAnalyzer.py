#!/usr/bin/env python2
# Run the foresting configuration on PbPb in CMSSW_5_3_X, using the new HF/Voronoi jets
# Author: Alex Barbieri
# Date: 2013-10-15

import FWCore.ParameterSet.Config as cms
process = cms.Process('ANA')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest AODSIM simple jets",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
    process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring("/store/mc/Fall13dr/Neutrino_Pt-2to20_gun/AODSIM/castor_tsg_PU1bx50_POSTLS162_V1-v1/00000/00455082-92A2-E311-B51E-002618943836.root"))

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100))


# PbPb 53X MC

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.GeneratorHI_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_GRun', '')

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("SimpleJetAnalyzer.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

process.load('HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff')

process.ak5CaloJetAnalyzer = process.inclusiveJetAnalyzer.clone(
    usePAT = cms.untracked.bool(False),
    jetTag = cms.InputTag("ak5CaloJets"),
    genjetTag = 'ak5GenJets',
    rParam = 0.5,
    matchJets = cms.untracked.bool(False),
    matchTag = '',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = True,
    isMC = True,
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    hcalHFRecHitSrc = cms.untracked.InputTag("reducedHcalRecHits:hfreco"),
    hcalHBHERecHitSrc = cms.untracked.InputTag("reducedHcalRecHits:hbhereco"),
    EBRecHitSrc = cms.untracked.InputTag("reducedEcalRecHitsEB"),
    EERecHitSrc = cms.untracked.InputTag("reducedEcalRecHitsEE")
)

process.ak5PFJetAnalyzer = process.ak5CaloJetAnalyzer.clone(
    jetTag = cms.InputTag("ak5PFJets")
    )

process.ana_step = cms.Path(
    # process.mix
    # process.genParticles*
    # process.genParticlesForJets*
    # process.ak5GenJetAnalyzer
    process.ak5CaloJetAnalyzer
    +process.ak5PFJetAnalyzer
)
