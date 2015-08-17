# /users/krajczar/HI2015/7_4_6_patch2/HIon/V29 (CMSSW_7_4_6)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/krajczar/HI2015/7_4_6_patch2/HIon/V29')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter3PSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.2 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet(
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterL3 = cms.PSet(
  minPt = cms.double( 0.5 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterForElectrons = cms.PSet(
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minPt = cms.double( 2.0 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 )
)
process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet(
  minPt = cms.double( 10.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet(
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 9 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetCkfTrajectoryFilter = cms.PSet(
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet(
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet(
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetPvClusterComparer = cms.PSet(
  track_pt_min = cms.double( 2.5 ),
  track_pt_max = cms.double( 10.0 ),
  track_chi2_max = cms.double( 9999999.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetPvClusterComparerForBTag = cms.PSet(
  track_pt_min = cms.double( 0.1 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet(
  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTSeedFromConsecutiveHitsCreator = cms.PSet(
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterial" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "" )
)
process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 4 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2HighPtTkMuPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" )
)
process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet(
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 3 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetPvClusterComparerForIT = cms.PSet(
  track_pt_min = cms.double( 1.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
process.HLTSiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
process.HLTSiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet(
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTSeedFromProtoTracks = cms.PSet(
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.transferSystem = cms.PSet(
  destinations = cms.vstring( 'Tier0',
    'DQM',
    'ECAL',
    'EventDisplay',
    'Lustre',
    'None' ),
  transferModes = cms.vstring( 'default',
    'test',
    'emulator' ),
  streamA = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamCalibration = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQM = cms.PSet(
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQMCalibration = cms.PSet(
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEcalCalibration = cms.PSet(
    default = cms.vstring( 'ECAL' ),
    test = cms.vstring( 'ECAL' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEventDisplay = cms.PSet(
    default = cms.vstring( 'EventDisplay',
      'Tier0' ),
    test = cms.vstring( 'EventDisplay',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamExpressCosmics = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamNanoDST = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamRPCMON = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamTrackerCalibration = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  default = cms.PSet(
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' ),
    streamLookArea = cms.PSet(  )
  ),
  streamLookArea = cms.PSet(
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  )
)
process.hltESPCkfTrajectoryBuilderForHI = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  intermediateCleaning = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.hltESPCkfTrajectoryFilterForHI = cms.PSet(
  minimumNumberOfHits = cms.int32( 6 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minPt = cms.double( 0.9 )
)
process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet(
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet(
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 )
)
process.HLTPSetLowPtCkfTrajectoryFilterForHI = cms.PSet(
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.4 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetLowPtCkfTrajectoryBuilderForHI = cms.PSet(
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet(
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  maxNumberOfHits = cms.int32( 100 )
)
process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet(
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTSiStripClusterChargeCutForHI = cms.PSet(  value = cms.double( 2069.0 ) )
process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet(
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.streams = cms.PSet(
  A = cms.vstring( 'HLTPhysics',
    'InitialPDForHI' ),
  DQM = cms.vstring( 'OnlineMonitor' )
)
process.datasets = cms.PSet(
  HLTPhysics = cms.vstring( 'HLT_Physics_v2' ),
  InitialPDForHI = cms.vstring( 'HLT_HIFullTrack12_v1',
    'HLT_HIFullTrack30_L1Centrality010_v1',
    'HLT_HIFullTrack30_L1Centrality1030_v1',
    'HLT_HIFullTrack30_L1Centrality3050_v1',
    'HLT_HIFullTrack30_L1Centrality50100_v1',
    'HLT_HIFullTrack45_L1Centrality010_v1',
    'HLT_HIFullTrack45_L1Centrality1030_v1',
    'HLT_HIFullTrack45_L1Centrality3050_v1',
    'HLT_HIFullTrack45_L1Centrality50100_v1',
    'HLT_HIL1DoubleMu0_v1',
    'HLT_HIL2DoubleMu0_NHitQ_v1',
    'HLT_HIL2DoubleMu0_v1',
    'HLT_HIL2DoubleMu3_v1',
    'HLT_HIL2Mu15_v1',
    'HLT_HIL2Mu20_noHF_v1',
    'HLT_HIL2Mu20_v1',
    'HLT_HIL2Mu3_NHitQ_v1',
    'HLT_HIL2Mu3_noHF_v1',
    'HLT_HIL2Mu3_v1',
    'HLT_HIL2Mu7_v1',
    'HLT_HIL3DoubleMu0_Cent3050_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_Cent3050_Upsilon_v1',
    'HLT_HIL3DoubleMu0_Cent3050_v1',
    'HLT_HIL3DoubleMu0_Cent50100_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_Cent50100_Upsilon_v1',
    'HLT_HIL3DoubleMu0_Cent50100_v1',
    'HLT_HIL3DoubleMu0_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_OS_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_OS_NoCowboy_v1',
    'HLT_HIL3DoubleMu0_OS_Upsilon_v1',
    'HLT_HIL3DoubleMu0_OS_er16_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_OS_er16_Upsilon_v1',
    'HLT_HIL3DoubleMu0_OS_er16_v1',
    'HLT_HIL3DoubleMu0_OS_er16to24_JpsiPsi_v1',
    'HLT_HIL3DoubleMu0_OS_er16to24_Upsilon_v1',
    'HLT_HIL3DoubleMu0_OS_er16to24_v1',
    'HLT_HIL3DoubleMu0_OS_v1',
    'HLT_HIL3DoubleMu0_SS_v1',
    'HLT_HIL3DoubleMu0_Upsilon_v1',
    'HLT_HIL3DoubleMu0_WdEta18_OS_v1',
    'HLT_HIL3DoubleMu0_noHF_v1',
    'HLT_HIL3DoubleMu0_v1',
    'HLT_HIL3DoubleMu3_v1',
    'HLT_HIL3DoubleMuOpen_NotHF2_v1',
    'HLT_HIL3Mu14_v1',
    'HLT_HIL3Mu3_v1',
    'HLT_HIL3Mu5_v1',
    'HLT_HIL3Mu7_v1',
    'HLT_HIL3MuOpen_NotHF2_v1',
    'HLT_HIUCC020_v1',
    'HLT_HIUCC100_v1',
    'HLT_HIUPCDoubleEG2NotHF2Pixel_SingleTrack_v1',
    'HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1',
    'HLT_HIUPCL1DoubleEG2NotHF2_v1',
    'HLT_HIUPCL1DoubleMuOpenNotHF2_v1',
    'HLT_HIUPCL1SingleEG2NotHF2_v1',
    'HLT_HIUPCL1SingleEG5NotHF2_v1',
    'HLT_HIUPCL1SingleMuOpenNotHF2_v1',
    'HLT_HIUPCSingleMuNotHF2Pixel_SingleTrack_v1',
    'HLT_HIUPSingleEG2NotHF2Pixel_SingleTrack_v1',
    'HLT_HIUPSingleEG5NotHF2Pixel_SingleTrack_v1' ),
  OnlineMonitor = cms.vstring( 'HLT_Physics_v2' )
)

process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool( False ),
    toGet = cms.untracked.vstring( 'GainWidths' )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalMappingRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" )
)
process.GlobalTag = cms.ESSource( "PoolDBESSource",
    globaltag = cms.string( "GR_H_V58" ),
    RefreshEachRun = cms.untracked.bool( True ),
    RefreshOpenIOVs = cms.untracked.bool( False ),
    toGet = cms.VPSet(
    ),
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialPeriod = cms.untracked.int32( 10 )
    ),
    RefreshAlways = cms.untracked.bool( False ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_CONDITIONS" ),
    ReconnectEachRun = cms.untracked.bool( True ),
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    DumpStat = cms.untracked.bool( False )
)
process.CSCINdexerESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCIndexerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCChannelMapperRecord" ),
    firstValid = cms.vuint32( 1 )
)

process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutForHI" ) ),
  nSigma = cms.double( 3.0 )
)
process.hltESPKFFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForLoopers" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.PropagatorWithMaterialForLoopers = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForLoopers" ),
  Mass = cms.double( 0.1396 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 4.0 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFlexibleKFFittingSmoother" ),
  standardFitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  looperFitter = cms.string( "hltESPKFFittingSmootherForLoopers" )
)
process.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( True ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
process.hltESPMeasurementTrackerForHI = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet(
    TOB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet(
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet(
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerForHI" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
process.MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.2 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.2 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 2 ),
  useSignedImpactParameterSig = cms.bool( True )
)
process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.MaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMf" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.VolumeBasedMagneticFieldESProducer = cms.ESProducer( "VolumeBasedMagneticFieldESProducerFromDB",
  debugBuilder = cms.untracked.bool( False ),
  valueOverride = cms.int32( -1 ),
  label = cms.untracked.string( "" )
)
process.ParametrizedMagneticFieldProducer = cms.ESProducer( "AutoParametrizedMagneticFieldProducer",
  version = cms.string( "Parabolic" ),
  valueOverride = cms.int32( -1 ),
  label = cms.untracked.string( "ParabolicMf" )
)
process.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
process.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
process.hltESPChi2MeasurementEstimator30 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator30" )
)
process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
process.CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperPostls1" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  useRealWireGeometry = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  alignmentsLabel = cms.string( "" ),
  useGangedStripsInME1a = cms.bool( False ),
  debugV = cms.untracked.bool( False ),
  useOnlyWiresInME1a = cms.bool( False ),
  useDDD = cms.bool( False ),
  useCentreTIOffsets = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerPostls1" )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  appendToDataLabel = cms.string( "" ),
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet(
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
process.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder" )
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService" )
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  nSigma = cms.double( 3.0 )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet(
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  Exclude = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" ),
  hcalTopologyConstants = cms.PSet(
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  useDDD = cms.untracked.bool( False ),
  compatibiltyWith11 = cms.untracked.bool( True )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  printDebug = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  APVGain = cms.VPSet(
    cms.PSet(  Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(  Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  ),
  AutomaticNormalization = cms.bool( False )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet(
    cms.PSet(  record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  PreFilter = cms.bool( False ),
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  trackerGeometryConstants = cms.PSet(
    ROCS_X = cms.int32( 0 ),
    ROCS_Y = cms.int32( 0 ),
    upgradeGeometry = cms.bool( False ),
    BIG_PIX_PER_ROC_Y = cms.int32( 2 ),
    BIG_PIX_PER_ROC_X = cms.int32( 1 ),
    ROWS_PER_ROC = cms.int32( 80 ),
    COLS_PER_ROC = cms.int32( 52 )
  ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet(
    kGood = cms.vstring( 'kOk' ),
    kProblematic = cms.vstring( 'kDAC',
      'kNoLaser',
      'kNoisy',
      'kNNoisy',
      'kNNNoisy',
      'kNNNNoisy',
      'kNNNNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0' ),
    kRecovered = cms.vstring(  ),
    kTime = cms.vstring(  ),
    kWeird = cms.vstring(  ),
    kBad = cms.vstring( 'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP' )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet(
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet(
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit',
  'HBHEIsolatedNoise',
  'AddedSimHcalNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFPET',
  'HFS8S1Ratio',
  'HFDigiTime' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEFlatNoise',
  'HBHESpikeNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer" )
process.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  categoryVariableName = cms.string( "vertexCategory" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  correctVertexMass = cms.bool( True ),
  trackSelection = cms.PSet(
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet(
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
process.hltCombinedSecondaryVertexV2 = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  categoryVariableName = cms.string( "vertexCategory" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  correctVertexMass = cms.bool( True ),
  trackSelection = cms.PSet(
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    b_dR = cms.double( 0.6263 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVIVFV2RecoVertex',
    'CombinedSVIVFV2PseudoVertex',
    'CombinedSVIVFV2NoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet(
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    b_dR = cms.double( 0.6263 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
process.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" )
)
process.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
process.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" )
process.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
process.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
process.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet(
    TOB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet(
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer" )
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  useLAWidthFromDB = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  IrradiationBiasCorrection = cms.bool( False )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
process.hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet(
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( False ),
    mTEC_P1 = cms.double( 0.471 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P0 = cms.double( -1.026 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTIB_P0 = cms.double( -0.742 ),
    mTIB_P1 = cms.double( 0.202 ),
    mTID_P0 = cms.double( -1.427 ),
    mTID_P1 = cms.double( 0.433 ),
    maxChgOneMIP = cms.double( 6000.0 )
  )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" ),
  trackerGeometryLabel = cms.untracked.string( "" )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  SimpleMagneticField = cms.string( "ParabolicMf" )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet(
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet(
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet(
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet(
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet(
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet(
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet(
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.trackerTopology = cms.ESProducer( "TrackerTopologyEP",
  pxb_layerMask = cms.uint32( 15 ),
  tib_str_int_extStartBit = cms.uint32( 10 ),
  tib_layerMask = cms.uint32( 7 ),
  tib_str_fw_bwStartBit = cms.uint32( 12 ),
  pxf_bladeMask = cms.uint32( 63 ),
  pxb_moduleStartBit = cms.uint32( 2 ),
  pxb_ladderStartBit = cms.uint32( 8 ),
  pxb_layerStartBit = cms.uint32( 16 ),
  tec_wheelStartBit = cms.uint32( 14 ),
  tib_str_fw_bwMask = cms.uint32( 3 ),
  tec_ringStartBit = cms.uint32( 5 ),
  tib_moduleStartBit = cms.uint32( 2 ),
  tib_sterMask = cms.uint32( 3 ),
  tid_sideStartBit = cms.uint32( 13 ),
  tid_wheelStartBit = cms.uint32( 11 ),
  tid_ringMask = cms.uint32( 3 ),
  tid_sterMask = cms.uint32( 3 ),
  tec_petal_fw_bwStartBit = cms.uint32( 12 ),
  tec_ringMask = cms.uint32( 7 ),
  tib_strMask = cms.uint32( 63 ),
  tec_sterMask = cms.uint32( 3 ),
  tec_sideStartBit = cms.uint32( 18 ),
  pxb_moduleMask = cms.uint32( 63 ),
  pxf_panelStartBit = cms.uint32( 8 ),
  tid_sideMask = cms.uint32( 3 ),
  tob_moduleMask = cms.uint32( 7 ),
  tid_ringStartBit = cms.uint32( 9 ),
  pxf_sideMask = cms.uint32( 3 ),
  appendToDataLabel = cms.string( "" ),
  pxf_diskStartBit = cms.uint32( 16 ),
  tib_str_int_extMask = cms.uint32( 3 ),
  tec_moduleMask = cms.uint32( 7 ),
  tob_sterMask = cms.uint32( 3 ),
  tob_rod_fw_bwMask = cms.uint32( 3 ),
  tob_layerStartBit = cms.uint32( 14 ),
  tec_petal_fw_bwMask = cms.uint32( 3 ),
  tib_layerStartBit = cms.uint32( 14 ),
  tec_sterStartBit = cms.uint32( 0 ),
  tid_moduleMask = cms.uint32( 31 ),
  tib_sterStartBit = cms.uint32( 0 ),
  tid_sterStartBit = cms.uint32( 0 ),
  pxf_moduleStartBit = cms.uint32( 2 ),
  pxf_diskMask = cms.uint32( 15 ),
  pxf_sideStartBit = cms.uint32( 23 ),
  tid_module_fw_bwStartBit = cms.uint32( 7 ),
  tob_layerMask = cms.uint32( 7 ),
  tid_module_fw_bwMask = cms.uint32( 3 ),
  tob_rod_fw_bwStartBit = cms.uint32( 12 ),
  tec_petalMask = cms.uint32( 15 ),
  pxb_ladderMask = cms.uint32( 255 ),
  tec_moduleStartBit = cms.uint32( 2 ),
  tec_sideMask = cms.uint32( 3 ),
  tob_rodMask = cms.uint32( 127 ),
  tib_strStartBit = cms.uint32( 4 ),
  tec_wheelMask = cms.uint32( 15 ),
  tob_rodStartBit = cms.uint32( 5 ),
  pxf_panelMask = cms.uint32( 3 ),
  tib_moduleMask = cms.uint32( 3 ),
  pxf_bladeStartBit = cms.uint32( 10 ),
  tid_wheelMask = cms.uint32( 3 ),
  tob_sterStartBit = cms.uint32( 0 ),
  tid_moduleStartBit = cms.uint32( 2 ),
  tec_petalStartBit = cms.uint32( 8 ),
  tob_moduleStartBit = cms.uint32( 2 ),
  pxf_moduleMask = cms.uint32( 63 )
)

process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    enableTimingExclusive = cms.untracked.bool( True ),
    skipFirstPath = cms.untracked.bool( False ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( True ),
    enableDQMbyPathTotal = cms.untracked.bool( True ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( True ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    enableDQMbyPathActive = cms.untracked.bool( True ),
    enableDQMbyPathDetails = cms.untracked.bool( True ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    enableDQMbyPathCounters = cms.untracked.bool( True ),
    enableDQMbyModuleType = cms.untracked.bool( False )
)
process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet(
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet(
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet(
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet(
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet(
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet(
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    Verbosity = cms.untracked.int32( 0 ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltCaloStage1Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage1::CaloSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    FWId = cms.untracked.int32( 2 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FedId = cms.int32( 1352 )
)
process.hltCaloStage1LegacyFormatDigis = cms.EDProducer( "L1TCaloUpgradeToGCTConverter",
    InputHFCountsCollection = cms.InputTag( 'hltCaloStage1Digis','HFBitCounts' ),
    InputHFSumsCollection = cms.InputTag( 'hltCaloStage1Digis','HFRingSums' ),
    InputRlxTauCollection = cms.InputTag( 'hltCaloStage1Digis','rlxTaus' ),
    InputIsoTauCollection = cms.InputTag( 'hltCaloStage1Digis','isoTaus' ),
    InputCollection = cms.InputTag( "hltCaloStage1Digis" )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    isoTauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoTauJets' ),
    etTotalSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltPrePhysics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltL1sL1SingleJet8BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet8_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet40Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet(
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 100.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet(
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet(
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    UnpackerMode = cms.untracked.int32( 0 ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    UnpackZDC = cms.untracked.bool( True ),
    firstSample = cms.int32( 0 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HBHE" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    ts3chi2 = cms.double( 5.0 ),
    ts4Min = cms.double( 5.0 ),
    pulseShapeParameters = cms.PSet(  ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet(
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    digistat = cms.PSet(
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    hfTimingTrustParameters = cms.PSet(
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet(
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HF" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts3chi2 = cms.double( 5.0 ),
    ts4Min = cms.double( 5.0 ),
    pulseShapeParameters = cms.PSet(  ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    puCorrMethod = cms.int32( 0 ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    pulseJitter = cms.double( 1.0 ),
    chargeMax = cms.double( 6.0 ),
    timeMin = cms.double( -15.0 ),
    ts4chi2 = cms.double( 15.0 ),
    ts345chi2 = cms.double( 100.0 ),
    applyTimeSlew = cms.bool( True ),
    applyTimeConstraint = cms.bool( True ),
    applyPulseJitter = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    ts3chi2 = cms.double( 5.0 ),
    ts4Min = cms.double( 5.0 ),
    pulseShapeParameters = cms.PSet(  ),
    noise = cms.double( 1.0 ),
    applyPedConstraint = cms.bool( True ),
    applyUnconstrainedFit = cms.bool( False ),
    ts4Max = cms.double( 500.0 ),
    meanTime = cms.double( -2.5 ),
    flagParameters = cms.PSet(  ),
    fitTimes = cms.int32( 1 ),
    timeMax = cms.double( 10.0 ),
    timeSigma = cms.double( 5.0 ),
    pedSigma = cms.double( 0.5 ),
    meanPed = cms.double( 0.0 ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltPuAK4CaloJets = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 1 ),
    doAreaFastjet = cms.bool( True ),
    voronoiRfact = cms.double( -0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "CaloJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 6.5 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.4 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    inputEtMin = cms.double( 0.3 ),
    puPtMin = cms.double( 8.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 10.0 ),
    radiusPU = cms.double( 0.5 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( True ),
    inputEMin = cms.double( 0.0 ),
    useMassDropTagger = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    subtractorName = cms.string( "MultipleAlgoIterator" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    yMin = cms.double( -1.0 ),
    useFiltering = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    nFilt = cms.int32( -1 ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    trimPtFracMin = cms.double( -1.0 ),
    dRMax = cms.double( -1.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False )
)
process.hltPuAK4CaloJetsIDPassed = cms.EDProducer( "HLTCaloJetIDProducer",
    min_N90 = cms.int32( -2 ),
    min_N90hits = cms.int32( 2 ),
    min_EMF = cms.double( 1.0E-6 ),
    jetsInput = cms.InputTag( "hltPuAK4CaloJets" ),
    JetIDParams = cms.PSet(
      useRecHits = cms.bool( True ),
      hbheRecHitsColl = cms.InputTag( "hltHbhereco" ),
      hoRecHitsColl = cms.InputTag( "hltHoreco" ),
      hfRecHitsColl = cms.InputTag( "hltHfreco" ),
      ebRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      eeRecHitsColl = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
    ),
    max_EMF = cms.double( 999.0 )
)
process.hltFixedGridRhoFastjetAllCalo = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltAK4CaloRelativeCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L2Relative" )
)
process.hltAK4CaloAbsoluteCorrector = cms.EDProducer( "LXXXCorrectorProducer",
    algorithm = cms.string( "AK4CaloHLT" ),
    level = cms.string( "L3Absolute" )
)
process.hltPuAK4CaloCorrector = cms.EDProducer( "ChainedJetCorrectorProducer",
    correctors = cms.VInputTag( 'hltAK4CaloRelativeCorrector','hltAK4CaloAbsoluteCorrector' )
)
process.hltPuAK4CaloJetsCorrected = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltPuAK4CaloJets" ),
    correctors = cms.VInputTag( 'hltPuAK4CaloCorrector' )
)
process.hltPuAK4CaloJetsCorrectedIDPassed = cms.EDProducer( "CorrectedCaloJetProducer",
    src = cms.InputTag( "hltPuAK4CaloJetsIDPassed" ),
    correctors = cms.VInputTag( 'hltPuAK4CaloCorrector' )
)
process.hltSinglePuAK4CaloJet40Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleJet16BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet16_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet60Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet60Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleJet28BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet28_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet80Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleJet44BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet44_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet100Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 100.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltPrePuAK4CaloJet110Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet110Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 110.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleJet56BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet56_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet120Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet120Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 120.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleJet8Cent3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet8_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet40Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleJet16Cent3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet16_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet60Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleJet28Cent3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet28_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet80Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePuAK4CaloJet100Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePuAK4CaloJet110Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleJet8Cent50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet8_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet40Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleJet16Cent50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet16_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet60Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleJet28Cent50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleS1Jet28_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPrePuAK4CaloJet80Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePuAK4CaloJet100Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePuAK4CaloJet110Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePuAK4CaloJet80Jet35Eta1p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltDoublePuAK4CaloJet35Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 1.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltPrePuAK4CaloJet80Jet35Eta0p7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet80Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 80.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 0.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltDoublePuAK4CaloJet35Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 35.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 0.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltPrePuAK4CaloJet100Jet35Eta1p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta1p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 100.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltPrePuAK4CaloJet100Jet35Eta0p7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSinglePuAK4CaloJet100Eta0p7 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 100.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 0.7 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltPrePuAK4CaloJet804545Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltTriplePuAK4CaloJet45Eta2p1 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 45.0 ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltPuAK4CaloJetsCorrectedIDPassed" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 85 )
)
process.hltL1sL1SingleEG3BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG3_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton10Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltIslandBasicClustersHI = cms.EDProducer( "IslandClusterProducer",
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    barrelShapeAssociation = cms.string( "islandBarrelShapeAssoc" ),
    endcapShapeAssociation = cms.string( "islandEndcapShapeAssoc" ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    clustershapecollectionEE = cms.string( "islandEndcapShape" ),
    clustershapecollectionEB = cms.string( "islandBarrelShape" ),
    VerbosityLevel = cms.string( "ERROR" ),
    IslandBarrelSeedThr = cms.double( 0.5 ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" )
)
process.hltHiIslandSuperClustersHI = cms.EDProducer( "HiSuperClusterProducer",
    barrelSuperclusterCollection = cms.string( "islandBarrelSuperClustersHI" ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    barrelClusterCollection = cms.string( "islandBarrelBasicClustersHI" ),
    endcapClusterProducer = cms.string( "hltIslandBasicClustersHI" ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    endcapBCEnergyThreshold = cms.double( 0.0 ),
    VerbosityLevel = cms.string( "ERROR" ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    barrelEtaSearchRoad = cms.double( 0.07 ),
    endcapSuperclusterCollection = cms.string( "islandEndcapSuperClustersHI" ),
    barrelBCEnergyThreshold = cms.double( 0.0 ),
    doBarrel = cms.bool( True ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "islandEndcapBasicClustersHI" ),
    barrelClusterProducer = cms.string( "hltIslandBasicClustersHI" )
)
process.hltHiCorrectedIslandBarrelSuperClustersHI = cms.EDProducer( "HiEgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    superClusterAlgo = cms.string( "Island" ),
    etThresh = cms.double( 0.0 ),
    rawSuperClusterProducer = cms.InputTag( 'hltHiIslandSuperClustersHI','islandBarrelSuperClustersHI' ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(
      fEtaVect = cms.vdouble( 0.993, 0.0, 0.00546, 1.165, -0.180844, 0.040312 ),
      fBremVect = cms.vdouble( -0.773799, 2.73438, -1.07235, 0.986821, -0.0101822, 3.06744E-4, 1.00595, -0.0495958, 0.00451986, 1.00595, -0.0495958, 0.00451986 ),
      fBremThVect = cms.vdouble( 1.2, 1.2 ),
      fEtEtaVect = cms.vdouble( 0.9497, 0.006985, 1.03754, -0.0142667, -0.0233993, 0.0, 0.0, 0.908915, 0.0137322, 16.9602, -29.3093, 19.8976, -5.92666, 0.654571 ),
      brLinearLowThr = cms.double( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      minR9Barrel = cms.double( 0.94 ),
      minR9Endcap = cms.double( 0.95 ),
      maxR9 = cms.double( 1.5 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' )
)
process.hltHiCorrectedIslandEndcapSuperClustersHI = cms.EDProducer( "HiEgammaSCCorrectionMaker",
    corectedSuperClusterCollection = cms.string( "" ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    superClusterAlgo = cms.string( "Island" ),
    etThresh = cms.double( 0.0 ),
    rawSuperClusterProducer = cms.InputTag( 'hltHiIslandSuperClustersHI','islandEndcapSuperClustersHI' ),
    applyEnergyCorrection = cms.bool( True ),
    isl_fCorrPset = cms.PSet(
      fEtaVect = cms.vdouble( 0.993, 0.0, 0.00546, 1.165, -0.180844, 0.040312 ),
      fBremVect = cms.vdouble( -0.773799, 2.73438, -1.07235, 0.986821, -0.0101822, 3.06744E-4, 1.00595, -0.0495958, 0.00451986, 1.00595, -0.0495958, 0.00451986 ),
      fBremThVect = cms.vdouble( 1.2, 1.2 ),
      fEtEtaVect = cms.vdouble( 0.9497, 0.006985, 1.03754, -0.0142667, -0.0233993, 0.0, 0.0, 0.908915, 0.0137322, 16.9602, -29.3093, 19.8976, -5.92666, 0.654571 ),
      brLinearLowThr = cms.double( 0.0 ),
      brLinearHighThr = cms.double( 0.0 ),
      minR9Barrel = cms.double( 0.94 ),
      minR9Endcap = cms.double( 0.95 ),
      maxR9 = cms.double( 1.5 )
    ),
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' )
)
process.hltCleanedHiCorrectedIslandBarrelSuperClustersHI = cms.EDProducer( "HiSpikeCleaner",
    originalSuperClusterProducer = cms.InputTag( "hltHiCorrectedIslandBarrelSuperClustersHI" ),
    recHitProducerEndcap = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    TimingCut = cms.untracked.double( 9999999.0 ),
    swissCutThr = cms.untracked.double( 0.95 ),
    recHitProducerBarrel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    etCut = cms.double( 8.0 ),
    outputColl = cms.string( "" )
)
process.hltRecoHIEcalWithCleaningCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( "hltHiCorrectedIslandEndcapSuperClustersHI" ),
    scHybridBarrelProducer = cms.InputTag( "hltCleanedHiCorrectedIslandBarrelSuperClustersHI" ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltHIPhoton10Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 10.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltPreHISinglePhoton15Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton15Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 15.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltPreHISinglePhoton20Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton20Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltL1sL1SingleEG7BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton30Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton30Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 30.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltL1sL1SingleEG21BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG21_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton40Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton40Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 40.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltPreHISinglePhoton50Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton50Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 50.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltL1sL1SingleEG30BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG30_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton60Eta2p1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIPhoton60Eta2p1 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 60.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.1 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltL1sL1SingleEG7Cent50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton30Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHISinglePhoton40Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHISinglePhoton50Eta2p1Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleEG7Cent3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG7_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHISinglePhoton30Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHISinglePhoton40Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHISinglePhoton50Eta2p1Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIDoublePhoton15Eta1p5Mass501000 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoublePhoton15Eta1p5 = cms.EDFilter( "HLT1Photon",
    saveTags = cms.bool( True ),
    MinPt = cms.double( 15.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 1.5 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltRecoHIEcalWithCleaningCandidate" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 81 )
)
process.hltHIDoublePhoton15Eta1p5Mass501000Filter = cms.EDFilter( "HLTPMMassFilter",
    saveTags = cms.bool( False ),
    lowerMassCut = cms.double( 50.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "" ),
    isElectron1 = cms.untracked.bool( False ),
    isElectron2 = cms.untracked.bool( False ),
    upperMassCut = cms.double( 1000.0 ),
    candTag = cms.InputTag( "hltHIDoublePhoton15Eta1p5" ),
    reqOppCharge = cms.untracked.bool( False ),
    nZcandcut = cms.int32( 1 )
)
process.hltBPTXCoincidence = cms.EDFilter( "HLTLevel1Activity",
    technicalBits = cms.uint64( 0x1 ),
    ignoreL1Mask = cms.bool( True ),
    invert = cms.bool( False ),
    physicsLoBits = cms.uint64( 0x1 ),
    physicsHiBits = cms.uint64( 0x40000 ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    daqPartitions = cms.uint32( 1 ),
    bunchCrossings = cms.vint32( 0, -1, 1 )
)
process.hltL1sMinBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack12 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltHISiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltHISiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( -1 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltHISiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltHISiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltHISiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltHISiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltHIPixelClusterVertices = cms.EDProducer( "HIPixelClusterVtxProducer",
    maxZ = cms.double( 30.0 ),
    zStep = cms.double( 0.1 ),
    minZ = cms.double( -30.0 ),
    pixelRecHits = cms.string( "hltHISiPixelRecHits" )
)
process.hltHIPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltHIPixel3ProtoTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIProtoTrackFilter" ),
      ptMin = cms.double( 1.0 ),
      tipMax = cms.double( 1.0 ),
      doVariablePtMin = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      siPixelRecHits = cms.InputTag( "hltHISiPixelRecHits" )
    ),
    passLabel = cms.string( "Pixel triplet tracks for vertexing" ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "HITrackingRegionForPrimaryVtxProducer" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.7 ),
        directionXCoord = cms.double( 1.0 ),
        directionZCoord = cms.double( 0.0 ),
        directionYCoord = cms.double( 1.0 ),
        useFoundVertices = cms.bool( True ),
        doVariablePtMin = cms.bool( True ),
        nSigmaZ = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 3.0 ),
        sigmaZVertex = cms.double( 3.0 ),
        siPixelRecHits = cms.InputTag( "hltHISiPixelRecHits" ),
        VertexCollection = cms.InputTag( "hltHIPixelClusterVertices" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.037 ),
        maxElement = cms.uint32( 100000 ),
        SeedComparitorPSet = cms.PSet(
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
    )
)
process.hltHIPixelMedianVertex = cms.EDProducer( "HIPixelMedianVtxProducer",
    PeakFindThreshold = cms.uint32( 100 ),
    PeakFindMaxZ = cms.double( 30.0 ),
    FitThreshold = cms.int32( 5 ),
    TrackCollection = cms.InputTag( "hltHIPixel3ProtoTracks" ),
    PtMin = cms.double( 0.075 ),
    PeakFindBinsPerCm = cms.int32( 10 ),
    FitMaxZ = cms.double( 0.1 ),
    FitBinsPerCm = cms.int32( 500 )
)
process.hltHISelectedProtoTracks = cms.EDFilter( "HIProtoTrackSelection",
    src = cms.InputTag( "hltHIPixel3ProtoTracks" ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    maxD0Significance = cms.double( 5.0 ),
    minZCut = cms.double( 0.2 ),
    VertexCollection = cms.InputTag( "hltHIPixelMedianVertex" ),
    ptMin = cms.double( 0.0 ),
    nSigmaZ = cms.double( 5.0 )
)
process.hltHIPixelAdaptiveVertex = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet(
      cms.PSet(  maxDistanceToBeam = cms.double( 0.1 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      )
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet(
      maxD0Significance = cms.double( 3.0 ),
      minPt = cms.double( 0.0 ),
      maxNormalizedChi2 = cms.double( 5.0 ),
      minSiliconLayersWithHits = cms.int32( 0 ),
      minPixelLayersWithHits = cms.int32( 2 ),
      trackQuality = cms.string( "any" ),
      numTracksThreshold = cms.int32( 2 ),
      algorithm = cms.string( "filterWithThreshold" )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltHISelectedProtoTracks" ),
    TkClusParameters = cms.PSet(
      algorithm = cms.string( "gap" ),
      TkGapClusParameters = cms.PSet(  zSeparation = cms.double( 1.0 ) )
    )
)
process.hltHIBestAdaptiveVertex = cms.EDFilter( "HIBestVertexSelection",
    maxNumber = cms.uint32( 1 ),
    src = cms.InputTag( "hltHIPixelAdaptiveVertex" )
)
process.hltHISelectedVertex = cms.EDProducer( "HIBestVertexProducer",
    adaptiveVertexCollection = cms.InputTag( "hltHIBestAdaptiveVertex" ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    medianVertexCollection = cms.InputTag( "hltHIPixelMedianVertex" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltHISiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet(
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "IteratedMedian" ),
      PedestalSubtractionFedMode = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( True ),
      useCMMeanMap = cms.bool( False ),
      CutToAvoidSignal = cms.double( 2.0 ),
      Fraction = cms.double( 0.2 ),
      minStripsToFit = cms.uint32( 4 ),
      consecThreshold = cms.uint32( 5 ),
      hitStripThreshold = cms.uint32( 40 ),
      Deviation = cms.uint32( 25 ),
      restoreThreshold = cms.double( 0.5 ),
      APVInspectMode = cms.string( "BaselineFollower" ),
      ForceNoRestore = cms.bool( False ),
      useRealMeanCM = cms.bool( False ),
      DeltaCMThreshold = cms.uint32( 20 ),
      nSigmaNoiseDerTh = cms.uint32( 4 ),
      nSaturatedStrip = cms.uint32( 2 ),
      APVRestoreMode = cms.string( "BaselineFollower" ),
      distortionThreshold = cms.uint32( 20 ),
      Iterations = cms.int32( 3 ),
      nSmooth = cms.uint32( 9 ),
      SelfSelectRestoreAlgo = cms.bool( False ),
      MeanCM = cms.int32( 0 ),
      CleaningSequence = cms.uint32( 1 ),
      slopeX = cms.int32( 3 ),
      slopeY = cms.int32( 4 ),
      ApplyBaselineRejection = cms.bool( True ),
      filteredBaselineMax = cms.double( 6.0 ),
      filteredBaselineDerivativeSumSquare = cms.double( 30.0 ),
      ApplyBaselineCleaner = cms.bool( True )
    ),
    Clusterizer = cms.PSet(
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( False )
)
process.hltHISiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltHISiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltHISiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTrackerForHI" )
)
process.hltHIPixel3PrimTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 0.9 ),
      tipMax = cms.double( 0.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 6.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 0.3 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.1 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 3.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.2 ),
        sigmaZVertex = cms.double( 3.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet(
          ComponentName = cms.string( "none" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.037 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
    )
)
process.hltHIPixelTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIPixel3PrimTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIPrimTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "hltESPCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPrimTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "initialStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter0TrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 1000.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 0 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( True ),
    nSigmaZ = cms.double( 9999.0 ),
    dz_par2 = cms.vdouble( 3.0, 0.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 9999.0, 0.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 0.2 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 999 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 15.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 1000.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 13 ),
    src = cms.InputTag( "hltHIGlobalPrimTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 0.15 ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 3.0, 0.0 ),
    d0_par1 = cms.vdouble( 9999.0, 0.0 ),
    res_par = cms.vdouble( 99999.0, 99999.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltHIIter1ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIIter0TrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltHISiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter1MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter1ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIDetachedPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter1ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIDetachedPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 0.95 ),
      tipMax = cms.double( 1.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      nSigmaLipMaxTolerance = cms.double( 0.0 ),
      lipMax = cms.double( 1.0 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel detached tracks with vertex constraint" ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.5 ),
        ptMin = cms.double( 0.9 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFixedError = cms.bool( True ),
        fixedError = cms.double( 0.5 ),
        sigmaZVertex = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 1000000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet(
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.0 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHIDetachedPixelLayerTriplets" )
    )
)
process.hltHIDetachedPixelTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHIDetachedPixelTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHIDetachedTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIDetachedPixelTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIDetachedGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIDetachedTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter1MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "detachedTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( False ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter1TrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 1000.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 0 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( True ),
    nSigmaZ = cms.double( 9999.0 ),
    dz_par2 = cms.vdouble( 3.0, 0.0 ),
    applyAdaptedPVCuts = cms.bool( False ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 9999.0, 0.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 0.2 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 999 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 15.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 1000.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 13 ),
    src = cms.InputTag( "hltHIDetachedGlobalPrimTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 0.15 ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 3.0, 0.0 ),
    d0_par1 = cms.vdouble( 9999.0, 0.0 ),
    res_par = cms.vdouble( 99999.0, 99999.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltHIIter1Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter0TrackSelectionHighPurity','hltHIIter1TrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  tLists = cms.vint32( 0, 1 ),
        pQual = cms.bool( False )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltHIIter0TrackSelectionHighPurity','hltHIIter1TrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIIter2ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIIter1TrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltHIIter1ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltHISiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter2MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter2ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHILowPtPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter2ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltHILowPtPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( True ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      ComponentName = cms.string( "HIPixelTrackFilter" ),
      ptMin = cms.double( 0.4 ),
      tipMax = cms.double( 0.0 ),
      useClusterShape = cms.bool( False ),
      VertexCollection = cms.InputTag( "hltHISelectedVertex" ),
      nSigmaTipMaxTolerance = cms.double( 4.0 ),
      nSigmaLipMaxTolerance = cms.double( 4.0 ),
      lipMax = cms.double( 0.0 ),
      clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    passLabel = cms.string( "Pixel primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.02 ),
        ptMin = cms.double( 0.4 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFixedError = cms.bool( False ),
        fixedError = cms.double( 0.2 ),
        sigmaZVertex = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "TrackCleaner" ) ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 500000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.0 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet(
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.0 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltHILowPtPixelLayerTriplets" )
    )
)
process.hltHILowPtPixelTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 1.0E9 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      forceKinematicWithRegionDirection = cms.bool( False ),
      magneticField = cms.string( "ParabolicMf" ),
      SeedMomentumForBOFF = cms.double( 5.0 ),
      OriginTransverseErrorMultiplier = cms.double( 1.0 ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MinOneOverPtError = cms.double( 1.0 ),
      propagator = cms.string( "PropagatorWithMaterialForHI" )
    ),
    InputVertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    InputCollection = cms.InputTag( "hltHILowPtPixelTracks" ),
    originRadius = cms.double( 1.0E9 )
)
process.hltHILowPtTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIDetachedPixelTrackSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHILowPtGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHILowPtTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter2MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "lowPtTripletStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter2TrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 1000.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 0 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( True ),
    nSigmaZ = cms.double( 9999.0 ),
    dz_par2 = cms.vdouble( 3.0, 0.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 9999.0, 0.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 0.2 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 999 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 15.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 1000.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 13 ),
    src = cms.InputTag( "hltHILowPtGlobalPrimTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 0.15 ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 3.0, 0.0 ),
    d0_par1 = cms.vdouble( 9999.0, 0.0 ),
    res_par = cms.vdouble( 99999.0, 99999.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltHIIter2Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter1Merged','hltHIIter2TrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltHIIter1Merged','hltHIIter2TrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIIter3ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltHIIter2TrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltHIIter2ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltHISiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltHISiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
process.hltHIIter3MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltHIIter3ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltHISiStripClusters" )
)
process.hltHIPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      skipClusters = cms.InputTag( "hltHIIter3ClustersRefRemoval" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      skipClusters = cms.InputTag( "hltHIIter3ClustersRefRemoval" )
    ),
    TIB = cms.PSet(  )
)
process.hltHIPixelPairSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.005 ),
        ptMin = cms.double( 4.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( False ),
        sigmaZVertex = cms.double( 4.0 ),
        fixedError = cms.double( 0.2 ),
        useFoundVertices = cms.bool( True ),
        useFakeVertices = cms.bool( False ),
        nSigmaZ = cms.double( 4.0 ),
        VertexCollection = cms.InputTag( "hltHISelectedVertex" )
      )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "PixelClusterShapeSeedComparitor" ),
      FilterAtHelixStage = cms.bool( True ),
      FilterPixelHits = cms.bool( True ),
      FilterStripHits = cms.bool( False ),
      ClusterShapeHitFilterName = cms.string( "ClusterShapeHitFilter" ),
      ClusterShapeCacheSrc = cms.InputTag( "hltHISiPixelClustersCache" )
    ),
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( "hltHISiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000000 ),
      doClusterCheck = cms.bool( True ),
      ClusterCollectionLabel = cms.InputTag( "hltHISiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 500000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 5000000 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet(
        maxElement = cms.uint32( 5000000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltHIPixelLayerPairs" )
    ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreatorIT" ) )
)
process.hltHIPixelPairTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltHIPixelPairSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialForHI" ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOppositeForHI" ),
      numberMeasurementsForFit = cms.int32( 4 )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter3MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryBuilderForHI" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltHIPixelPairGlobalPrimTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIPixelPairTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHIIter3MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFlexibleKFFittingSmoother" ),
    useHitsSplitting = cms.bool( True ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "pixelPairStep" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderAngleAndTemplate" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltHIIter3TrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 1000.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 0 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( True ),
    nSigmaZ = cms.double( 9999.0 ),
    dz_par2 = cms.vdouble( 3.0, 0.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 9999.0, 0.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 0.2 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 999 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 15.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 1000.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 14 ),
    src = cms.InputTag( "hltHIPixelPairGlobalPrimTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 0.15 ),
    vertices = cms.InputTag( "hltHISelectedVertex" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 3.0, 0.0 ),
    d0_par1 = cms.vdouble( 9999.0, 0.0 ),
    res_par = cms.vdouble( 99999.0, 99999.0 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltHIIter3Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( False ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIIter2Merged','hltHIIter3TrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( True ),
    FoundHitBonus = cms.double( 5.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltHIIter2Merged','hltHIIter3TrackSelectionHighPurity' ),
    LostHitPenalty = cms.double( 20.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIFullTrackCandsForHITrackTrigger = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltHIIter3Merged" ),
    particleType = cms.string( "pi+" )
)
process.hltHIFullTrackFilter12 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( False ),
    MinTrks = cms.int32( 1 ),
    MinPt = cms.double( 12.0 ),
    MaxVz = cms.double( 15.0 ),
    MaxEta = cms.double( 1.0 ),
    trackCollection = cms.InputTag( "hltHIFullTrackCandsForHITrackTrigger" ),
    vertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    MaxPt = cms.double( 10000.0 ),
    MinSep = cms.double( 0.2 )
)
process.hltL1sSingleTrack12Centrality010 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack12_Centrality0_10" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack30L1Centrality010 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIFullTrackFilter30 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( False ),
    MinTrks = cms.int32( 1 ),
    MinPt = cms.double( 30.0 ),
    MaxVz = cms.double( 15.0 ),
    MaxEta = cms.double( 1.0 ),
    trackCollection = cms.InputTag( "hltHIFullTrackCandsForHITrackTrigger" ),
    vertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    MaxPt = cms.double( 10000.0 ),
    MinSep = cms.double( 0.2 )
)
process.hltL1sSingleTrack12Centrality1030 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack12_Centrality10_30" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack30L1Centrality1030 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleTrack12Centrality3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack12_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack30L1Centrality3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleTrack12Centrality50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack12_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack30L1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleTrack20Centrality010 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack20_Centrality0_10" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack45L1Centrality010 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIFullTrackFilter45 = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( False ),
    MinTrks = cms.int32( 1 ),
    MinPt = cms.double( 45.0 ),
    MaxVz = cms.double( 15.0 ),
    MaxEta = cms.double( 1.0 ),
    trackCollection = cms.InputTag( "hltHIFullTrackCandsForHITrackTrigger" ),
    vertexCollection = cms.InputTag( "hltHISelectedVertex" ),
    MaxPt = cms.double( 10000.0 ),
    MinSep = cms.double( 0.2 )
)
process.hltL1sSingleTrack20Centrality1030 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack20_Centrality10_30" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack45L1Centrality1030 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleTrack20Centrality3050 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack20_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack45L1Centrality3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleTrack20Centrality50100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleTrack20_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIFullTrack45L1Centrality50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sCentrality5 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_Centrality0_5" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUCC100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltTowerMakerForHf = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( True ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( True ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0E-99 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0E-99 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kProblematic',
      'kRecovered',
      'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( True ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag(  ),
    UseRejectedRecoveredHcalHits = cms.bool( True ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltMetForHf = cms.EDProducer( "CaloMETProducer",
    alias = cms.string( "RawCaloMET" ),
    calculateSignificance = cms.bool( False ),
    globalThreshold = cms.double( 0.5 ),
    noHF = cms.bool( False ),
    src = cms.InputTag( "hltTowerMakerForHf" )
)
process.hltGlobalSumETHfFilter4340 = cms.EDFilter( "HLTGlobalSumsCaloMET",
    saveTags = cms.bool( False ),
    observable = cms.string( "sumEt" ),
    MinN = cms.int32( 1 ),
    Min = cms.double( 4340.0 ),
    Max = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetForHf" ),
    triggerType = cms.int32( 88 )
)
process.hltPixelActivityFilter56000 = cms.EDFilter( "HLTPixelActivityFilter",
    maxClusters = cms.uint32( 1000000 ),
    saveTags = cms.bool( False ),
    inputTag = cms.InputTag( "hltHISiPixelClusters" ),
    minClusters = cms.uint32( 56000 )
)
process.hltPreHIUCC020 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltGlobalSumETHfFilter4580 = cms.EDFilter( "HLTGlobalSumsCaloMET",
    saveTags = cms.bool( False ),
    observable = cms.string( "sumEt" ),
    MinN = cms.int32( 1 ),
    Min = cms.double( 4580.0 ),
    Max = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltMetForHf" ),
    triggerType = cms.int32( 88 )
)
process.hltPixelActivityFilter59000 = cms.EDFilter( "HLTPixelActivityFilter",
    maxClusters = cms.uint32( 1000000 ),
    saveTags = cms.bool( False ),
    inputTag = cms.InputTag( "hltHISiPixelClusters" ),
    minClusters = cms.uint32( 59000 )
)
process.hltL1sL1MuOpenNotMinimumBiasHF2AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_MuOpen_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUPCL1SingleMuOpenNotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1MuOpenL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1MuOpenNotMinimumBiasHF2AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltPreHIUPCSingleMuNotHF2PixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( False ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltPixelTracksForUPC = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    passLabel = cms.string( "" ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.1 ),
        originHalfLength = cms.double( 24.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet(
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
process.hltPixelVerticesForUPC = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksForUPC" ),
    PtMin = cms.double( 0.1 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
process.hltTrimmedPixelVerticesForUPC = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltPixelVerticesForUPC" )
)
process.hltGoodPixelTracksForUPC = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "loose" ),
    minNumberLayers = cms.uint32( 0 ),
    chi2n_par = cms.double( 9999.0 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 100.0 ),
    dz_par2 = cms.vdouble( 1.0, 1.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 9999.0, 1.0 ),
    copyTrajectories = cms.untracked.bool( False ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 0.5 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 999 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 999.0 ),
    copyExtras = cms.untracked.bool( False ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltPixelTracksForUPC" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesForUPC" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 9999.0, 1.0 ),
    d0_par1 = cms.vdouble( 9999.0, 1.0 ),
    res_par = cms.vdouble( 99999.0, 99999.0 ),
    minHitsToBypassChecks = cms.uint32( 999 )
)
process.hltPixelCandsForUPC = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltGoodPixelTracksForUPC" ),
    particleType = cms.string( "pi+" )
)
process.hltSinglePixelTrackForUPC = cms.EDFilter( "HLTSingleVertexPixelTrackFilter",
    saveTags = cms.bool( True ),
    MinTrks = cms.int32( 1 ),
    MinPt = cms.double( 0.4 ),
    MaxVz = cms.double( 15.0 ),
    MaxEta = cms.double( 2.4 ),
    trackCollection = cms.InputTag( "hltPixelCandsForUPC" ),
    vertexCollection = cms.InputTag( "hltPixelVerticesForUPC" ),
    MaxPt = cms.double( 9999.0 ),
    MinSep = cms.double( 0.12 )
)
process.hltL1sL1DoubleMuOpenNotMinimumBiasHF2AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMuOpen_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUPCL1DoubleMuOpenNotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1MuOpenL1Filtered2 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpenNotMinimumBiasHF2AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltPreHIUPCDoubleMuNotHF2PixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1EG2NotMinimumBiasHF2AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_EG2_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUPCL1SingleEG2NotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIUPSingleEG2NotHF2PixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1DoubleEG2NotMinimumBiasHF2AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG2_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUPCL1DoubleEG2NotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIUPCDoubleEG2NotHF2PixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1EG5NotMinimumBiasHF2AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_EG5_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIUPCL1SingleEG5NotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreHIUPSingleEG5NotHF2PixelSingleTrack = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1SingleMu3MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu3_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL2Mu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL1SingleMu3MinBiasFiltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    maxFEDid = cms.untracked.int32( 779 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    minFEDid = cms.untracked.int32( 770 ),
    dataType = cms.string( "DDU" ),
    readOutParameters = cms.PSet(
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet(
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet(
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( True ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet(
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      ),
      useUncertDB = cms.bool( True )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet(
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet(
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet(
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        ),
        useUncertDB = cms.bool( True )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet(
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet(
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( True ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
          tTrigModeConfig = cms.PSet(
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          ),
          useUncertDB = cms.bool( True )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0x0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet(
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet(
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    deltaPhiSearchWindow = cms.double( 0.25 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    deltaEtaSearchWindow = cms.double( 0.2 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    deltaEtaCrackSearchWindow = cms.double( 0.25 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    EnableDTMeasurement = cms.bool( True ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    EnableCSCMeasurement = cms.bool( True ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL1extraParticles" ),
    L1MaxEta = cms.double( 2.5 ),
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 1 ),
    GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet(
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      NMinRecHits = cms.uint32( 2 ),
      UseSubRecHits = cms.bool( False ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      RescaleError = cms.double( 100.0 )
    ),
    L2TrajBuilderParameters = cms.PSet(
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet(
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet(
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet(
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet(
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltHIL2Mu3L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu3MinBiasFiltered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1SingleMu5MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL2Mu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL1SingleMu5MinBiasFiltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu5MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2Mu7L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu5MinBiasFiltered" ),
    MinPt = cms.double( 7.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1SingleMu14MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu14_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL2Mu15 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL1SingleMu14MinBiasFiltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu14MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2Mu15L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu14MinBiasFiltered" ),
    MinPt = cms.double( 15.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltPreHIL2Mu20 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL2Mu20L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu14MinBiasFiltered" ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1SingleMu3noMinBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL2Mu3noHF = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL1SingleMu3noMinBiasFiltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3noMinBias" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2Mu3noMinBiasL2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu3noMinBiasFiltered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1SingleMu14noMinBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu14" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL2Mu20noHF = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL1SingleMu14noMinBiasFiltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu14noMinBias" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2Mu20noMinBiasL2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu14noMinBiasFiltered" ),
    MinPt = cms.double( 20.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltPreHIL2Mu3NHitQ = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL2Mu3N1HitQL2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL1SingleMu3MinBiasFiltered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.vint32( 1 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1SingleMuOpenNotHF2 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_MuOpen_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3MuOpenNotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL2MuOpenNotHF2L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenNotHF2" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2MuOpenNotHF2L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIL2MuOpenNotHF2L1Filtered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet(
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet(
          pf3_V12 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          pf3_V33 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V44 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V22 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V23 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V45 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V55 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" ),
      MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'hltESPSteppingHelixPropagatorOpposite',
        'hltESPSteppingHelixPropagatorAlong' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(  ),
    PtCut = cms.double( 1.0 )
)
process.hltHIL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltHIL3TrajSeedOIState" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilderSeedHit" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilderSeedHit" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltHIL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIL3TrackCandidateFromL2OIState" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltHIL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltHIL3TkTracksFromL2OIState" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltHIL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltHIL3MuonsOIState" ),
      iterativeTSG = cms.PSet(
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "unused" ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet(
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet(
            pf3_V12 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V13 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V11 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V14 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V15 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
            pf3_V33 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            zAxis = cms.vdouble( -3.14159, 3.14159 ),
            pf3_V44 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
            pf3_V22 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V23 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V45 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V55 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
            ),
            pf3_V34 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V35 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V25 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            ),
            pf3_V24 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTrackerForHI" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
        MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial',
        'hltESPSmartPropagatorAnyOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(  ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltHIL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltHIL3TrajSeedOIHit" ),
    reverseTrajectories = cms.bool( True ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltHIL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIL3TrackCandidateFromL2OIHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltHIL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltHIL3TkTracksFromL2OIHit" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltHIL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltHIL3MuonsOIState','hltHIL3MuonsOIHit' )
)
process.hltHIPixelLayerPairsNoSkip = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltHIMixedLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix2_pos+TEC1_pos',
      'FPix2_pos+TEC2_pos',
      'TEC1_pos+TEC2_pos',
      'TEC2_pos+TEC3_pos',
      'FPix2_neg+TEC1_neg',
      'FPix2_neg+TEC2_neg',
      'TEC1_neg+TEC2_neg',
      'TEC2_neg+TEC3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltHIL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    TkSeedGenerator = cms.PSet(
      PSetNames = cms.vstring( 'skipTSG',
        'iterativeTSG' ),
      L3TkCollectionA = cms.InputTag( "hltHIL3TkFromL2OICombination" ),
      iterativeTSG = cms.PSet(
        firstTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet(
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 0 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 ),
              SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
            ),
            SeedingLayers = cms.InputTag( "hltHIPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        ),
        PSetNames = cms.vstring( 'firstTSG',
          'secondTSG' ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet(
          PSetNames = cms.vstring( 'endcapTSG',
            'barrelTSG' ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet(
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet(
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              useOnDemandTracker = cms.untracked.int32( 0 ),
              SeedingLayers = cms.InputTag( "hltHIMixedLayerPairs" )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        ),
        secondTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            useOnDemandTracker = cms.untracked.int32( 0 ),
            SeedingLayers = cms.InputTag( "hltHIPixelLayerPairsNoSkip" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
          SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'PropagatorWithMaterial' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      Eta_min = cms.double( 0.1 ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
    ),
    PCut = cms.double( 2.5 ),
    TrackerSeedCleaner = cms.PSet(
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      directionCleaner = cms.bool( True )
    ),
    PtCut = cms.double( 1.0 )
)
process.hltHIL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    src = cms.InputTag( "hltHIL3TrajSeedIOHit" ),
    reverseTrajectories = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    trackCandidateAlso = cms.bool( True ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltHIL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltHIL3TrackCandidateFromL2IOHit" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltHISiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIterX" ),
    alias = cms.untracked.string( "" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
process.hltHIL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 ),
        DYTthrs = cms.vint32( 30, 15 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Eta_min = cms.double( 0.05 ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( "hltHIL3TkTracksFromL2IOHit" ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      tkTrajMaxDXYBeamSpot = cms.double( 0.2 ),
      tkTrajVertex = cms.InputTag( "pixelVertices" ),
      tkTrajUseVertex = cms.bool( False )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
      ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.hltHIL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltHIL3TrajSeedIOHit','hltHIL3TrajSeedOIState','hltHIL3TrajSeedOIHit' )
)
process.hltHIL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltHIL3TrackCandidateFromL2IOHit','hltHIL3TrackCandidateFromL2OIHit','hltHIL3TrackCandidateFromL2OIState' )
)
process.hltHIL3TkTracksMergeStep1 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIL3TkTracksFromL2OIState','hltHIL3TkTracksFromL2OIHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltHIL3TkTracksFromL2OIState','hltHIL3TkTracksFromL2OIHit' ),
    LostHitPenalty = cms.double( 0.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIL3TkTracksFromL2 = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltHIL3TkTracksMergeStep1','hltHIL3TkTracksFromL2IOHit' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 100.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltHIL3TkTracksMergeStep1','hltHIL3TkTracksFromL2IOHit' ),
    LostHitPenalty = cms.double( 0.0 ),
    newQuality = cms.string( "confirmed" )
)
process.hltHIL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltHIL3MuonsOIState','hltHIL3MuonsOIHit','hltHIL3MuonsIOHit' )
)
process.hltHIL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltHIL3MuonsOIState','hltHIL3MuonsOIHit','hltHIL3MuonsIOHit' )
)
process.hltHIL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltHIL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltHIL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
process.hltHIL2MuOpenNotHF2L3Filtered = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltHIL2MuOpenNotHF2L2Filtered" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 3.0 )
)
process.hltPreHIL3Mu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISingleMu3L3Filtered = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltHIL2Mu3L2Filtered" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 3.0 )
)
process.hltPreHIL3Mu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISingleMu5L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu5MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHISingleMu5L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu5L1Filtered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHISingleMu5L3Filtered = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu5L2Filtered" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 3.0 )
)
process.hltL1sL1SingleMu7MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu7_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3Mu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISingleMu7L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu7MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHISingleMu7L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu7L1Filtered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHISingleMu7L3Filtered = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu7L2Filtered" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 3.0 )
)
process.hltPreHIL3Mu14 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHISingleMu14L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( False ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu14MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHISingleMu14L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu14L1Filtered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHISingleMu14L3Filtered = cms.EDFilter( "HLTMuonL3PreFilter",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltHISingleMu14L2Filtered" ),
    MinNmuonHits = cms.int32( 0 ),
    MinN = cms.int32( 1 ),
    MinTrackPt = cms.double( 0.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxDXYBeamSpot = cms.double( 0.1 ),
    MinNhits = cms.int32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDz = cms.double( 9999.0 ),
    MaxPtDifference = cms.double( 9999.0 ),
    MaxDr = cms.double( 2.0 ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    MinDXYBeamSpot = cms.double( -1.0 ),
    MinDr = cms.double( -1.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinPt = cms.double( 3.0 )
)
process.hltL1sL1DoubleMu0BptxAND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_BptxAND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL1DoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1DoubleMu0HQL1Filtered0 = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0BptxAND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltPreHIL2DoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0Level1PathL1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0BptxAND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIL2DoubleMu0L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0Level1PathL1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltPreHIL2DoubleMu0NHitQ = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL2DoubleMu0L2N1HitsFiltered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0Level1PathL1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.vint32( 1 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltPreHIL2DoubleMu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIL2DoubleMu3L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0Level1PathL1Filtered" ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltL1sL1DoubleMu0MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasL1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuonL2PreFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasL1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuonL3FilterOpen = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu3 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu3_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu3L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu3" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu3L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu3L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu3L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu3L2Filtered" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 3.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMuOpenNotFHF2 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMuOpen_NotMinimumBiasHF2_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMuOpenNotHF2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMuOpenNotHF2L1Filter = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpenNotFHF2" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMuOpenNotHF2L2Filter = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMuOpenNotHF2L1Filter" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMuOpenNotHF2L3Filter = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMuOpenNotHF2L2Filter" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0WdEta18OSMinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_WdEta18_OS_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0WdEta18OS = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0WdEta18L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0WdEta18OSMinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0WdEta18L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0WdEta18L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0WdEta18L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0WdEta18L2Filtered" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_MinimumBiasHF1_AND_Centrality30_50" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0Cent3050 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCentrality30to50L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuonOpenCentrality30to50L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCentrality30to50L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuonOpenCentrality30to50L3Filter = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonOpenCentrality30to50L2Filtered" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_MinimumBiasHF1_AND_Centrality50_100" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0Cent50100 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent50to100L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuonOpenCentrality50to100L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent50to100L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuonOpenCentrality50to100L3Filter = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonOpenCentrality50to100L2Filtered" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0OSer16MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_OS_er16_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0OSer16 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiaser16L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuonL2PreFiltered0er16 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiaser16L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuonL3FilterOpener16 = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0er16" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_OS_er16to24_MinimumBiasHF1_AND" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0OSer16to24 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMuL1OpenMinBiaser16Fto24iltered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuonL2PreFiltered0er16to14 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMuL1OpenMinBiaser16Fto24iltered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuonL3FilterOpener16to24 = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0er16to14" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltL1sL1DoubleMu0 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0_10" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0noHF = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0NoMinBiasL1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDimuon0noMinBiasL2PreFiltered0 = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0NoMinBiasL1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDimuon0noMinBiasL3Filter = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuon0noMinBiasL2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltPreHIL3DoubleMu0Upsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDimuonL3FilterOpenUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltPreHIL3DoubleMu0Cent3050Upsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent3050L1FilteredUpsilon = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0MinBiasCent3050L2FilteredUpsilon = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent3050L1FilteredUpsilon" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent3050L3FilteredUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent3050L2FilteredUpsilon" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltPreHIL3DoubleMu0Cent50100Upsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent50100L1FilteredUpsilon = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0MinBiasCent50100L2FilteredUpsilon = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent50100L1FilteredUpsilon" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent50100L3FilteredUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent50100L2FilteredUpsilon" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0 = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "( L1_DoubleMu0_OS_MinimumBiasHF1_AND ) OR ( L1_DoubleMu0_10 )" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreHIL3DoubleMu0OSUpsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredUpsilon = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredUpsilon = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredUpsilon" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredUpsilon" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltPreHIL3DoubleMu0OSer16Upsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16L1FilteredUpsilon = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiaser16L2FilteredUpsilon = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16L1FilteredUpsilon" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16L3FilteredUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16L2FilteredUpsilon" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltPreHIL3DoubleMu0OSer16to24Upsilon = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16to24L1FilteredUpsilon = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiaser16to24L2FilteredUpsilon = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16to24L1FilteredUpsilon" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16to24L3FilteredUpsilon = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16to24L2FilteredUpsilon" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 15.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 7.0 )
)
process.hltPreHIL3DoubleMu0JpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDimuonL3FilterOpenJpsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0Cent3050JpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent3050L1FilteredJpsiPsi = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0MinBiasCent3050L2FilteredJpsiPsi = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent3050L1FilteredJpsiPsi" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent3050L3FilteredJpsiPsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent3050L2FilteredJpsiPsi" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0Cent50100JpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent50100L1FilteredJpsiPsi = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0MinBiasCent50100L2FilteredJpsiPsi = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent50100L1FilteredJpsiPsi" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0MinBiasCent50100L3FilteredJpsiPsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 0 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0MinBiasCent50100L2FilteredJpsiPsi" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0OSJpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredJpsi = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredJpsi = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredJpsi" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredJpsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredJpsi" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0OSer16JpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16L1FilteredJpsiPsi = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiaser16L2FilteredJpsiPsi = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16L1FilteredJpsiPsi" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16L3FilteredJpsiPsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16L2FilteredJpsiPsi" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0OSer16to24JpsiPsi = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16to24L1FilteredJpsiPsi = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiaser16to24L2FilteredJpsiPsi = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16to24L1FilteredJpsiPsi" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiaser16to24L3FilteredJpsiPsi = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiaser16to24L2FilteredJpsiPsi" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 4.2 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 2.2 )
)
process.hltPreHIL3DoubleMu0SS = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDimuonL3FilterOpenSS = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( 1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDimuonL2PreFiltered0" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltPreHIL3DoubleMu0OS = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1Filtered = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2Filtered = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L1Filtered" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3Filtered = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L2Filtered" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( False ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltPreHIL3DoubleMu0OSNoCowboy = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredNoCowboy = cms.EDFilter( "HLTMuonL1Filter",
    saveTags = cms.bool( True ),
    CSCTFtag = cms.InputTag( "unused" ),
    PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( "hltL1extraParticles" ),
    ExcludeSingleSegmentCSC = cms.bool( False )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredNoCowboy = cms.EDFilter( "HLTMuonL2PreFilter",
    saveTags = cms.bool( True ),
    MaxDr = cms.double( 9999.0 ),
    CutOnChambers = cms.bool( False ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredNoCowboy" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    SeedMapTag = cms.InputTag( "hltL2Muons" ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.vint32( 0 ),
    MinDxySig = cms.double( -1.0 ),
    MinNchambers = cms.vint32( 0 ),
    AbsEtaBins = cms.vdouble( 5.0 ),
    MaxDz = cms.double( 9999.0 ),
    CandTag = cms.InputTag( "hltL2MuonCandidates" ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MinDr = cms.double( -1.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinNstations = cms.vint32( 0 )
)
process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredNoCowboy = cms.EDFilter( "HLTMuonDimuonL3Filter",
    saveTags = cms.bool( True ),
    ChargeOpt = cms.int32( -1 ),
    MaxPtMin = cms.vdouble( 1.0E125 ),
    FastAccept = cms.bool( False ),
    CandTag = cms.InputTag( "hltHIL3MuonCandidates" ),
    PreviousCandTag = cms.InputTag( "hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredNoCowboy" ),
    MaxPtBalance = cms.double( 999999.0 ),
    MaxPtPair = cms.vdouble( 1.0E125 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtMin = cms.vdouble( 0.0 ),
    MaxInvMass = cms.vdouble( 300.0 ),
    MinPtMax = cms.vdouble( 0.0 ),
    BeamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    MaxDz = cms.double( 9999.0 ),
    MinPtPair = cms.vdouble( 0.0 ),
    MaxDr = cms.double( 20.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxDCAMuMu = cms.double( 999.0 ),
    MinNhits = cms.int32( 0 ),
    NSigmaPt = cms.double( 0.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxEta = cms.double( 2.5 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    CutCowboys = cms.bool( True ),
    MinInvMass = cms.vdouble( 0.0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltPreAnalyzerEndpath = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1GtTrigReport = cms.EDAnalyzer( "L1GtTrigReport",
    PrintVerbosity = cms.untracked.int32( 10 ),
    UseL1GlobalTriggerRecord = cms.bool( False ),
    PrintOutput = cms.untracked.int32( 3 ),
    L1GtRecordInputTag = cms.InputTag( "hltGtDigis" )
)
process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT' )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltCaloStage1Digis + process.hltCaloStage1LegacyFormatDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTPuAK4CaloJetsReconstructionSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltPuAK4CaloJets + process.hltPuAK4CaloJetsIDPassed )
process.HLTPuAK4CaloCorrectorProducersSequence = cms.Sequence( process.hltAK4CaloRelativeCorrector + process.hltAK4CaloAbsoluteCorrector + process.hltPuAK4CaloCorrector )
process.HLTPuAK4CaloJetsCorrectionSequence = cms.Sequence( process.hltFixedGridRhoFastjetAllCalo + process.HLTPuAK4CaloCorrectorProducersSequence + process.hltPuAK4CaloJetsCorrected + process.hltPuAK4CaloJetsCorrectedIDPassed )
process.HLTPuAK4CaloJetsSequence = cms.Sequence( process.HLTPuAK4CaloJetsReconstructionSequence + process.HLTPuAK4CaloJetsCorrectionSequence )
process.HLTDoHIEcalClusWithCleaningSequence = cms.Sequence( process.hltIslandBasicClustersHI + process.hltHiIslandSuperClustersHI + process.hltHiCorrectedIslandBarrelSuperClustersHI + process.hltHiCorrectedIslandEndcapSuperClustersHI + process.hltCleanedHiCorrectedIslandBarrelSuperClustersHI + process.hltRecoHIEcalWithCleaningCandidate )
process.HLTBeginSequenceBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTDoHILocalPixelSequence = cms.Sequence( process.hltHISiPixelDigis + process.hltHISiPixelClusters + process.hltHISiPixelClustersCache + process.hltHISiPixelRecHits )
process.HLTHIRecopixelvetexingSequence = cms.Sequence( process.hltHIPixelClusterVertices + process.hltHIPixelLayerTriplets + process.hltHIPixel3ProtoTracks + process.hltHIPixelMedianVertex + process.hltHISelectedProtoTracks + process.hltHIPixelAdaptiveVertex + process.hltHIBestAdaptiveVertex + process.hltHISelectedVertex )
process.HLTDoHILocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltHISiStripRawToClustersFacility + process.hltHISiStripClusters )
process.HLTHIIterativeTrackingIteration0 = cms.Sequence( process.hltHIPixel3PrimTracks + process.hltHIPixelTrackSeeds + process.hltHIPrimTrackCandidates + process.hltHIGlobalPrimTracks + process.hltHIIter0TrackSelectionHighPurity )
process.HLTHIIterativeTrackingIteration1 = cms.Sequence( process.hltHIIter1ClustersRefRemoval + process.hltHIIter1MaskedMeasurementTrackerEvent + process.hltHIDetachedPixelLayerTriplets + process.hltHIDetachedPixelTracks + process.hltHIDetachedPixelTrackSeeds + process.hltHIDetachedTrackCandidates + process.hltHIDetachedGlobalPrimTracks + process.hltHIIter1TrackSelectionHighPurity )
process.HLTHIIterativeTrackingIteration2 = cms.Sequence( process.hltHIIter2ClustersRefRemoval + process.hltHIIter2MaskedMeasurementTrackerEvent + process.hltHILowPtPixelLayerTriplets + process.hltHILowPtPixelTracks + process.hltHILowPtPixelTrackSeeds + process.hltHILowPtTrackCandidates + process.hltHILowPtGlobalPrimTracks + process.hltHIIter2TrackSelectionHighPurity )
process.HLTHIIterativeTrackingIteration3 = cms.Sequence( process.hltHIIter3ClustersRefRemoval + process.hltHIIter3MaskedMeasurementTrackerEvent + process.hltHIPixelLayerPairs + process.hltHIPixelPairSeeds + process.hltHIPixelPairTrackCandidates + process.hltHIPixelPairGlobalPrimTracks + process.hltHIIter3TrackSelectionHighPurity )
process.HLTDoLocalHfSequence = cms.Sequence( process.hltHcalDigis + process.hltHfreco + process.hltTowerMakerForHf )
process.HLTRecoMETHfSequence = cms.Sequence( process.HLTDoLocalHfSequence + process.hltMetForHf )
process.HLTDoHILocalPixelClustersSequence = cms.Sequence( process.hltHISiPixelDigis + process.hltHISiPixelClusters )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelClustersCache + process.hltSiPixelRecHits )
process.HLTRecopixelvertexingSequenceForUPC = cms.Sequence( process.hltPixelLayerTriplets + process.hltPixelTracksForUPC + process.hltPixelVerticesForUPC + process.hltTrimmedPixelVerticesForUPC )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTMuonLocalRecoSequence + process.hltL2OfflineMuonSeeds + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTHIL3muonTkCandidateSequence = cms.Sequence( process.HLTDoHILocalPixelSequence + process.HLTDoHILocalStripSequence + process.hltHIL3TrajSeedOIState + process.hltHIL3TrackCandidateFromL2OIState + process.hltHIL3TkTracksFromL2OIState + process.hltHIL3MuonsOIState + process.hltHIL3TrajSeedOIHit + process.hltHIL3TrackCandidateFromL2OIHit + process.hltHIL3TkTracksFromL2OIHit + process.hltHIL3MuonsOIHit + process.hltHIL3TkFromL2OICombination + process.hltHIPixelLayerTriplets + process.hltHIPixelLayerPairsNoSkip + process.hltHIMixedLayerPairs + process.hltHIL3TrajSeedIOHit + process.hltHIL3TrackCandidateFromL2IOHit + process.hltHIL3TkTracksFromL2IOHit + process.hltHIL3MuonsIOHit + process.hltHIL3TrajectorySeed + process.hltHIL3TrackCandidateFromL2 )
process.HLTHIL3muonrecoNocandSequence = cms.Sequence( process.HLTHIL3muonTkCandidateSequence + process.hltHIL3TkTracksMergeStep1 + process.hltHIL3TkTracksFromL2 + process.hltHIL3MuonsLinksCombination + process.hltHIL3Muons )
process.HLTHIL3muonrecoSequence = cms.Sequence( process.HLTHIL3muonrecoNocandSequence + process.hltHIL3MuonCandidates )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_Physics_v2 = cms.Path( process.HLTBeginSequence + process.hltPrePhysics + process.HLTEndSequence )
process.HLT_PuAK4CaloJet40_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet8BptxAND + process.hltPrePuAK4CaloJet40Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet60_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet16BptxAND + process.hltPrePuAK4CaloJet60Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28BptxAND + process.hltPrePuAK4CaloJet80Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet100_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet44BptxAND + process.hltPrePuAK4CaloJet100Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet110_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet44BptxAND + process.hltPrePuAK4CaloJet110Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet110Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet120_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet56BptxAND + process.hltPrePuAK4CaloJet120Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet120Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet40_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet8Cent3050 + process.hltPrePuAK4CaloJet40Eta2p1Cent3050 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet60_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet16Cent3050 + process.hltPrePuAK4CaloJet60Eta2p1Cent3050 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent3050 + process.hltPrePuAK4CaloJet80Eta2p1Cent3050 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet100_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent3050 + process.hltPrePuAK4CaloJet100Eta2p1Cent3050 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet110_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent3050 + process.hltPrePuAK4CaloJet110Eta2p1Cent3050 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet110Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet40_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet8Cent50100 + process.hltPrePuAK4CaloJet40Eta2p1Cent50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet40Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet60_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet16Cent50100 + process.hltPrePuAK4CaloJet60Eta2p1Cent50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet60Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent50100 + process.hltPrePuAK4CaloJet80Eta2p1Cent50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet100_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent50100 + process.hltPrePuAK4CaloJet100Eta2p1Cent50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet110_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28Cent50100 + process.hltPrePuAK4CaloJet110Eta2p1Cent50100 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet110Eta2p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_Jet35_Eta1p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28BptxAND + process.hltPrePuAK4CaloJet80Jet35Eta1p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta1p1 + process.hltDoublePuAK4CaloJet35Eta1p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_Jet35_Eta0p7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28BptxAND + process.hltPrePuAK4CaloJet80Jet35Eta0p7 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet80Eta0p7 + process.hltDoublePuAK4CaloJet35Eta0p7 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet100_Jet35_Eta1p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet44BptxAND + process.hltPrePuAK4CaloJet100Jet35Eta1p1 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta1p1 + process.hltDoublePuAK4CaloJet35Eta1p1 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet100_Jet35_Eta0p7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet44BptxAND + process.hltPrePuAK4CaloJet100Jet35Eta0p7 + process.HLTPuAK4CaloJetsSequence + process.hltSinglePuAK4CaloJet100Eta0p7 + process.hltDoublePuAK4CaloJet35Eta0p7 + process.HLTEndSequence )
process.HLT_PuAK4CaloJet80_45_45_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet28BptxAND + process.hltPrePuAK4CaloJet804545Eta2p1 + process.HLTPuAK4CaloJetsSequence + process.hltTriplePuAK4CaloJet45Eta2p1 + process.hltSinglePuAK4CaloJet80Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton10_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG3BptxAND + process.hltPreHISinglePhoton10Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton10Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton15_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG3BptxAND + process.hltPreHISinglePhoton15Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton15Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton20_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG3BptxAND + process.hltPreHISinglePhoton20Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton20Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton30_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7BptxAND + process.hltPreHISinglePhoton30Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton30Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton40_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG21BptxAND + process.hltPreHISinglePhoton40Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton40Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton50_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG21BptxAND + process.hltPreHISinglePhoton50Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton50Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton60_Eta2p1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG30BptxAND + process.hltPreHISinglePhoton60Eta2p1 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton60Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton30_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent50100 + process.hltPreHISinglePhoton30Eta2p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton30Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton40_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent50100 + process.hltPreHISinglePhoton40Eta2p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton40Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton50_Eta2p1_Cent50_100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent50100 + process.hltPreHISinglePhoton50Eta2p1Cent50100 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton50Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton30_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent3050 + process.hltPreHISinglePhoton30Eta2p1Cent3050 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton30Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton40_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent3050 + process.hltPreHISinglePhoton40Eta2p1Cent3050 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton40Eta2p1 + process.HLTEndSequence )
process.HLT_HISinglePhoton50_Eta2p1_Cent30_50_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG7Cent3050 + process.hltPreHISinglePhoton50Eta2p1Cent3050 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIPhoton50Eta2p1 + process.HLTEndSequence )
process.HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG3BptxAND + process.hltPreHIDoublePhoton15Eta1p5Mass501000 + process.HLTDoCaloSequence + process.HLTDoHIEcalClusWithCleaningSequence + process.hltHIDoublePhoton15Eta1p5 + process.hltHIDoublePhoton15Eta1p5Mass501000Filter + process.HLTEndSequence )
process.HLT_HIFullTrack12_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sMinBias + process.hltPreHIFullTrack12 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter12 + process.HLTEndSequence )
process.HLT_HIFullTrack30_L1Centrality010_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack12Centrality010 + process.hltPreHIFullTrack30L1Centrality010 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter30 + process.HLTEndSequence )
process.HLT_HIFullTrack30_L1Centrality1030_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack12Centrality1030 + process.hltPreHIFullTrack30L1Centrality1030 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter30 + process.HLTEndSequence )
process.HLT_HIFullTrack30_L1Centrality3050_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack12Centrality3050 + process.hltPreHIFullTrack30L1Centrality3050 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter30 + process.HLTEndSequence )
process.HLT_HIFullTrack30_L1Centrality50100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack12Centrality50100 + process.hltPreHIFullTrack30L1Centrality50100 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter30 + process.HLTEndSequence )
process.HLT_HIFullTrack45_L1Centrality010_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack20Centrality010 + process.hltPreHIFullTrack45L1Centrality010 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter45 + process.HLTEndSequence )
process.HLT_HIFullTrack45_L1Centrality1030_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack20Centrality1030 + process.hltPreHIFullTrack45L1Centrality1030 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter45 + process.HLTEndSequence )
process.HLT_HIFullTrack45_L1Centrality3050_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack20Centrality3050 + process.hltPreHIFullTrack45L1Centrality3050 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter45 + process.HLTEndSequence )
process.HLT_HIFullTrack45_L1Centrality50100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleTrack20Centrality50100 + process.hltPreHIFullTrack45L1Centrality50100 + process.HLTDoHILocalPixelSequence + process.HLTHIRecopixelvetexingSequence + process.HLTDoHILocalStripSequence + process.HLTHIIterativeTrackingIteration0 + process.HLTHIIterativeTrackingIteration1 + process.hltHIIter1Merged + process.HLTHIIterativeTrackingIteration2 + process.hltHIIter2Merged + process.HLTHIIterativeTrackingIteration3 + process.hltHIIter3Merged + process.hltHIFullTrackCandsForHITrackTrigger + process.hltHIFullTrackFilter45 + process.HLTEndSequence )
process.HLT_HIUCC100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sCentrality5 + process.hltPreHIUCC100 + process.HLTRecoMETHfSequence + process.hltGlobalSumETHfFilter4340 + process.HLTDoHILocalPixelClustersSequence + process.hltPixelActivityFilter56000 + process.HLTEndSequence )
process.HLT_HIUCC020_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sCentrality5 + process.hltPreHIUCC020 + process.HLTRecoMETHfSequence + process.hltGlobalSumETHfFilter4580 + process.HLTDoHILocalPixelClustersSequence + process.hltPixelActivityFilter59000 + process.HLTEndSequence )
process.HLT_HIUPCL1SingleMuOpenNotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1MuOpenNotMinimumBiasHF2AND + process.hltPreHIUPCL1SingleMuOpenNotHF2 + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_HIUPCSingleMuNotHF2Pixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1MuOpenNotMinimumBiasHF2AND + process.hltPreHIUPCSingleMuNotHF2PixelSingleTrack + process.hltL1MuOpenL1Filtered0 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequenceForUPC + process.hltGoodPixelTracksForUPC + process.hltPixelCandsForUPC + process.hltSinglePixelTrackForUPC + process.HLTEndSequence )
process.HLT_HIUPCL1DoubleMuOpenNotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMuOpenNotMinimumBiasHF2AND + process.hltPreHIUPCL1DoubleMuOpenNotHF2 + process.hltL1MuOpenL1Filtered2 + process.HLTEndSequence )
process.HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMuOpenNotMinimumBiasHF2AND + process.hltPreHIUPCDoubleMuNotHF2PixelSingleTrack + process.hltL1MuOpenL1Filtered2 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequenceForUPC + process.hltGoodPixelTracksForUPC + process.hltPixelCandsForUPC + process.hltSinglePixelTrackForUPC + process.HLTEndSequence )
process.HLT_HIUPCL1SingleEG2NotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1EG2NotMinimumBiasHF2AND + process.hltPreHIUPCL1SingleEG2NotHF2 + process.HLTEndSequence )
process.HLT_HIUPSingleEG2NotHF2Pixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1EG2NotMinimumBiasHF2AND + process.hltPreHIUPSingleEG2NotHF2PixelSingleTrack + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequenceForUPC + process.hltGoodPixelTracksForUPC + process.hltPixelCandsForUPC + process.hltSinglePixelTrackForUPC + process.HLTEndSequence )
process.HLT_HIUPCL1DoubleEG2NotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG2NotMinimumBiasHF2AND + process.hltPreHIUPCL1DoubleEG2NotHF2 + process.HLTEndSequence )
process.HLT_HIUPCDoubleEG2NotHF2Pixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG2NotMinimumBiasHF2AND + process.hltPreHIUPCDoubleEG2NotHF2PixelSingleTrack + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequenceForUPC + process.hltGoodPixelTracksForUPC + process.hltPixelCandsForUPC + process.hltSinglePixelTrackForUPC + process.HLTEndSequence )
process.HLT_HIUPCL1SingleEG5NotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1EG5NotMinimumBiasHF2AND + process.hltPreHIUPCL1SingleEG5NotHF2 + process.HLTEndSequence )
process.HLT_HIUPSingleEG5NotHF2Pixel_SingleTrack_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1EG5NotMinimumBiasHF2AND + process.hltPreHIUPSingleEG5NotHF2PixelSingleTrack + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequenceForUPC + process.hltGoodPixelTracksForUPC + process.hltPixelCandsForUPC + process.hltSinglePixelTrackForUPC + process.HLTEndSequence )
process.HLT_HIL2Mu3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu3MinBiasHF1AND + process.hltPreHIL2Mu3 + process.hltHIL1SingleMu3MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu3L2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu5MinBiasHF1AND + process.hltPreHIL2Mu7 + process.hltHIL1SingleMu5MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu7L2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu15_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu14MinBiasHF1AND + process.hltPreHIL2Mu15 + process.hltHIL1SingleMu14MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu15L2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu14MinBiasHF1AND + process.hltPreHIL2Mu20 + process.hltHIL1SingleMu14MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu20L2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu3_noHF_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu3noMinBias + process.hltPreHIL2Mu3noHF + process.hltHIL1SingleMu3noMinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu3noMinBiasL2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu20_noHF_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu14noMinBias + process.hltPreHIL2Mu20noHF + process.hltHIL1SingleMu14noMinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu20noMinBiasL2Filtered + process.HLTEndSequence )
process.HLT_HIL2Mu3_NHitQ_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu3MinBiasHF1AND + process.hltPreHIL2Mu3NHitQ + process.hltHIL1SingleMu3MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu3N1HitQL2Filtered + process.HLTEndSequence )
process.HLT_HIL3MuOpen_NotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMuOpenNotHF2 + process.hltPreHIL3MuOpenNotHF2 + process.hltHIL2MuOpenNotHF2L1Filtered + process.HLTL2muonrecoSequence + process.hltHIL2MuOpenNotHF2L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIL2MuOpenNotHF2L3Filtered + process.HLTEndSequence )
process.HLT_HIL3Mu3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu3MinBiasHF1AND + process.hltPreHIL3Mu3 + process.hltHIL1SingleMu3MinBiasFiltered + process.HLTL2muonrecoSequence + process.hltHIL2Mu3L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHISingleMu3L3Filtered + process.HLTEndSequence )
process.HLT_HIL3Mu5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu5MinBiasHF1AND + process.hltPreHIL3Mu5 + process.hltHISingleMu5L1Filtered + process.HLTL2muonrecoSequence + process.hltHISingleMu5L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHISingleMu5L3Filtered + process.HLTEndSequence )
process.HLT_HIL3Mu7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu7MinBiasHF1AND + process.hltPreHIL3Mu7 + process.hltHISingleMu7L1Filtered + process.HLTL2muonrecoSequence + process.hltHISingleMu7L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHISingleMu7L3Filtered + process.HLTEndSequence )
process.HLT_HIL3Mu14_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu14MinBiasHF1AND + process.hltPreHIL3Mu14 + process.hltHISingleMu14L1Filtered + process.HLTL2muonrecoSequence + process.hltHISingleMu14L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHISingleMu14L3Filtered + process.HLTEndSequence )
process.HLT_HIL1DoubleMu0_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0BptxAND + process.hltPreHIL1DoubleMu0 + process.hltL1fL1DoubleMu0HQL1Filtered0 + process.HLTEndSequence )
process.HLT_HIL2DoubleMu0_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0BptxAND + process.hltPreHIL2DoubleMu0 + process.hltHIDoubleMu0Level1PathL1Filtered + process.HLTL2muonrecoSequence + process.hltHIL2DoubleMu0L2Filtered + process.HLTEndSequence )
process.HLT_HIL2DoubleMu0_NHitQ_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0BptxAND + process.hltPreHIL2DoubleMu0NHitQ + process.hltHIDoubleMu0Level1PathL1Filtered + process.HLTL2muonrecoSequence + process.hltHIL2DoubleMu0L2N1HitsFiltered + process.HLTEndSequence )
process.HLT_HIL2DoubleMu3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0BptxAND + process.hltPreHIL2DoubleMu3 + process.hltHIDoubleMu0Level1PathL1Filtered + process.HLTL2muonrecoSequence + process.hltHIL2DoubleMu3L2Filtered + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1AND + process.hltPreHIL3DoubleMu0 + process.hltHIDoubleMu0MinBiasL1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpen + process.HLTEndSequence )
process.HLT_HIL3DoubleMu3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu3 + process.hltPreHIL3DoubleMu3 + process.hltHIDoubleMu3L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDoubleMu3L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu3L3Filtered + process.HLTEndSequence )
process.HLT_HIL3DoubleMuOpen_NotHF2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMuOpenNotFHF2 + process.hltPreHIL3DoubleMuOpenNotHF2 + process.hltHIDoubleMuOpenNotHF2L1Filter + process.HLTL2muonrecoSequence + process.hltHIDoubleMuOpenNotHF2L2Filter + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMuOpenNotHF2L3Filter + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_WdEta18_OS_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0WdEta18OSMinBiasHF1AND + process.hltPreHIL3DoubleMu0WdEta18OS + process.hltHIDoubleMu0WdEta18L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0WdEta18L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0WdEta18L3Filtered + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent3050_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50 + process.hltPreHIL3DoubleMu0Cent3050 + process.hltHIDoubleMu0MinBiasCentrality30to50L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonOpenCentrality30to50L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIDimuonOpenCentrality30to50L3Filter + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent50100_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100 + process.hltPreHIL3DoubleMu0Cent50100 + process.hltHIDoubleMu0MinBiasCent50to100L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonOpenCentrality50to100L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIDimuonOpenCentrality50to100L3Filter + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16 + process.hltHIDoubleMu0MinBiaser16L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0er16 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpener16 + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16to24_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16to24 + process.hltHIDoubleMuL1OpenMinBiaser16Fto24iltered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0er16to14 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpener16to24 + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_noHF_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0 + process.hltPreHIL3DoubleMu0noHF + process.hltHIDoubleMu0NoMinBiasL1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuon0noMinBiasL2PreFiltered0 + process.HLTHIL3muonrecoSequence + process.hltHIDimuon0noMinBiasL3Filter + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1AND + process.hltPreHIL3DoubleMu0Upsilon + process.hltHIDoubleMu0MinBiasL1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpenUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent3050_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50 + process.hltPreHIL3DoubleMu0Cent3050Upsilon + process.hltHIDoubleMu0MinBiasCent3050L1FilteredUpsilon + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0MinBiasCent3050L2FilteredUpsilon + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0MinBiasCent3050L3FilteredUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent50100_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100 + process.hltPreHIL3DoubleMu0Cent50100Upsilon + process.hltHIDoubleMu0MinBiasCent50100L1FilteredUpsilon + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0MinBiasCent50100L2FilteredUpsilon + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0MinBiasCent50100L3FilteredUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0 + process.hltPreHIL3DoubleMu0OSUpsilon + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredUpsilon + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredUpsilon + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16Upsilon + process.hltHIDoubleMu0OSMinBiaser16L1FilteredUpsilon + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16L2FilteredUpsilon + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16L3FilteredUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16to24_Upsilon_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16to24Upsilon + process.hltHIDoubleMu0OSMinBiaser16to24L1FilteredUpsilon + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16to24L2FilteredUpsilon + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16to24L3FilteredUpsilon + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1AND + process.hltPreHIL3DoubleMu0JpsiPsi + process.hltHIDoubleMu0MinBiasL1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpenJpsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent3050_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality30to50 + process.hltPreHIL3DoubleMu0Cent3050JpsiPsi + process.hltHIDoubleMu0MinBiasCent3050L1FilteredJpsiPsi + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0MinBiasCent3050L2FilteredJpsiPsi + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0MinBiasCent3050L3FilteredJpsiPsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_Cent50100_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1ANDCentrality50to100 + process.hltPreHIL3DoubleMu0Cent50100JpsiPsi + process.hltHIDoubleMu0MinBiasCent50100L1FilteredJpsiPsi + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0MinBiasCent50100L2FilteredJpsiPsi + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0MinBiasCent50100L3FilteredJpsiPsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0 + process.hltPreHIL3DoubleMu0OSJpsiPsi + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredJpsi + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredJpsi + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredJpsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16JpsiPsi + process.hltHIDoubleMu0OSMinBiaser16L1FilteredJpsiPsi + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16L2FilteredJpsiPsi + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16L3FilteredJpsiPsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_er16to24_JpsiPsi_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSer16to24MinBiasHF1AND + process.hltPreHIL3DoubleMu0OSer16to24JpsiPsi + process.hltHIDoubleMu0OSMinBiaser16to24L1FilteredJpsiPsi + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16to24L2FilteredJpsiPsi + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiaser16to24L3FilteredJpsiPsi + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_SS_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0MinBiasHF1AND + process.hltPreHIL3DoubleMu0SS + process.hltHIDoubleMu0MinBiasL1Filtered + process.HLTL2muonrecoSequence + process.hltHIDimuonL2PreFiltered0 + process.HLTHIL3muonrecoSequence + process.hltHIDimuonL3FilterOpenSS + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0 + process.hltPreHIL3DoubleMu0OS + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1Filtered + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2Filtered + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3Filtered + process.HLTEndSequence )
process.HLT_HIL3DoubleMu0_OS_NoCowboy_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMu0OSMinBiasHF1ANDORDoubleMu0 + process.hltPreHIL3DoubleMu0OSNoCowboy + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L1FilteredNoCowboy + process.HLTL2muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L2FilteredNoCowboy + process.HLTHIL3muonrecoSequence + process.hltHIDoubleMu0OSMinBiasORDoubleMu0L3FilteredNoCowboy + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.HLTAnalyzerEndpath = cms.EndPath( process.hltPreAnalyzerEndpath + process.hltL1GtTrigReport + process.hltTrigReport )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_Physics_v2, process.HLT_PuAK4CaloJet40_Eta2p1_v1, process.HLT_PuAK4CaloJet60_Eta2p1_v1, process.HLT_PuAK4CaloJet80_Eta2p1_v1, process.HLT_PuAK4CaloJet100_Eta2p1_v1, process.HLT_PuAK4CaloJet110_Eta2p1_v1, process.HLT_PuAK4CaloJet120_Eta2p1_v1, process.HLT_PuAK4CaloJet40_Eta2p1_Cent30_50_v1, process.HLT_PuAK4CaloJet60_Eta2p1_Cent30_50_v1, process.HLT_PuAK4CaloJet80_Eta2p1_Cent30_50_v1, process.HLT_PuAK4CaloJet100_Eta2p1_Cent30_50_v1, process.HLT_PuAK4CaloJet110_Eta2p1_Cent30_50_v1, process.HLT_PuAK4CaloJet40_Eta2p1_Cent50_100_v1, process.HLT_PuAK4CaloJet60_Eta2p1_Cent50_100_v1, process.HLT_PuAK4CaloJet80_Eta2p1_Cent50_100_v1, process.HLT_PuAK4CaloJet100_Eta2p1_Cent50_100_v1, process.HLT_PuAK4CaloJet110_Eta2p1_Cent50_100_v1, process.HLT_PuAK4CaloJet80_Jet35_Eta1p1_v1, process.HLT_PuAK4CaloJet80_Jet35_Eta0p7_v1, process.HLT_PuAK4CaloJet100_Jet35_Eta1p1_v1, process.HLT_PuAK4CaloJet100_Jet35_Eta0p7_v1, process.HLT_PuAK4CaloJet80_45_45_Eta2p1_v1, process.HLT_HISinglePhoton10_Eta2p1_v1, process.HLT_HISinglePhoton15_Eta2p1_v1, process.HLT_HISinglePhoton20_Eta2p1_v1, process.HLT_HISinglePhoton30_Eta2p1_v1, process.HLT_HISinglePhoton40_Eta2p1_v1, process.HLT_HISinglePhoton50_Eta2p1_v1, process.HLT_HISinglePhoton60_Eta2p1_v1, process.HLT_HISinglePhoton30_Eta2p1_Cent50_100_v1, process.HLT_HISinglePhoton40_Eta2p1_Cent50_100_v1, process.HLT_HISinglePhoton50_Eta2p1_Cent50_100_v1, process.HLT_HISinglePhoton30_Eta2p1_Cent30_50_v1, process.HLT_HISinglePhoton40_Eta2p1_Cent30_50_v1, process.HLT_HISinglePhoton50_Eta2p1_Cent30_50_v1, process.HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_v1, process.HLT_HIFullTrack12_v1, process.HLT_HIFullTrack30_L1Centrality010_v1, process.HLT_HIFullTrack30_L1Centrality1030_v1, process.HLT_HIFullTrack30_L1Centrality3050_v1, process.HLT_HIFullTrack30_L1Centrality50100_v1, process.HLT_HIFullTrack45_L1Centrality010_v1, process.HLT_HIFullTrack45_L1Centrality1030_v1, process.HLT_HIFullTrack45_L1Centrality3050_v1, process.HLT_HIFullTrack45_L1Centrality50100_v1, process.HLT_HIUCC100_v1, process.HLT_HIUCC020_v1, process.HLT_HIUPCL1SingleMuOpenNotHF2_v1, process.HLT_HIUPCSingleMuNotHF2Pixel_SingleTrack_v1, process.HLT_HIUPCL1DoubleMuOpenNotHF2_v1, process.HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrack_v1, process.HLT_HIUPCL1SingleEG2NotHF2_v1, process.HLT_HIUPSingleEG2NotHF2Pixel_SingleTrack_v1, process.HLT_HIUPCL1DoubleEG2NotHF2_v1, process.HLT_HIUPCDoubleEG2NotHF2Pixel_SingleTrack_v1, process.HLT_HIUPCL1SingleEG5NotHF2_v1, process.HLT_HIUPSingleEG5NotHF2Pixel_SingleTrack_v1, process.HLT_HIL2Mu3_v1, process.HLT_HIL2Mu7_v1, process.HLT_HIL2Mu15_v1, process.HLT_HIL2Mu20_v1, process.HLT_HIL2Mu3_noHF_v1, process.HLT_HIL2Mu20_noHF_v1, process.HLT_HIL2Mu3_NHitQ_v1, process.HLT_HIL3MuOpen_NotHF2_v1, process.HLT_HIL3Mu3_v1, process.HLT_HIL3Mu5_v1, process.HLT_HIL3Mu7_v1, process.HLT_HIL3Mu14_v1, process.HLT_HIL1DoubleMu0_v1, process.HLT_HIL2DoubleMu0_v1, process.HLT_HIL2DoubleMu0_NHitQ_v1, process.HLT_HIL2DoubleMu3_v1, process.HLT_HIL3DoubleMu0_v1, process.HLT_HIL3DoubleMu3_v1, process.HLT_HIL3DoubleMuOpen_NotHF2_v1, process.HLT_HIL3DoubleMu0_WdEta18_OS_v1, process.HLT_HIL3DoubleMu0_Cent3050_v1, process.HLT_HIL3DoubleMu0_Cent50100_v1, process.HLT_HIL3DoubleMu0_OS_er16_v1, process.HLT_HIL3DoubleMu0_OS_er16to24_v1, process.HLT_HIL3DoubleMu0_noHF_v1, process.HLT_HIL3DoubleMu0_Upsilon_v1, process.HLT_HIL3DoubleMu0_Cent3050_Upsilon_v1, process.HLT_HIL3DoubleMu0_Cent50100_Upsilon_v1, process.HLT_HIL3DoubleMu0_OS_Upsilon_v1, process.HLT_HIL3DoubleMu0_OS_er16_Upsilon_v1, process.HLT_HIL3DoubleMu0_OS_er16to24_Upsilon_v1, process.HLT_HIL3DoubleMu0_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_Cent3050_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_Cent50100_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_OS_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_OS_er16_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_OS_er16to24_JpsiPsi_v1, process.HLT_HIL3DoubleMu0_SS_v1, process.HLT_HIL3DoubleMu0_OS_v1, process.HLT_HIL3DoubleMu0_OS_NoCowboy_v1, process.HLTriggerFinalPath, process.HLTAnalyzerEndpath ))


# process.source = cms.Source( "PoolSource",
#     fileNames = cms.untracked.vstring(
#         'root://xrootd.unl.edu//store/user/mnguyen/Hydjet_Quenched_MinBias_5020GeV/HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI-RAW/6da45e4e90741bc03dbd9aec5f36c050/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_571_1_Nqu.root',
#     ),
#     inputCommands = cms.untracked.vstring(
#         'keep *'
#     ),
#     firstEvent = cms.untracked.uint32(62)

# )
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
                                "file:/mnt/hadoop/cms/store/user/richard/MBHydjet5020/Hydjet_Quenched_MinBias_5020GeV/HydjetMB5020_750_75X_mcRun2_HeavyIon_v1_RealisticHICollisions2011_STARTHI50_mc_RECOSIM_v3/150729_144407/0000/step3_101.root"

    ),
                            secondaryFileNames = cms.untracked.vstring("file:/mnt/hadoop/cms/store/user/mnguyen/Hydjet_Quenched_MinBias_5020GeV/HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI-RAW/6da45e4e90741bc03dbd9aec5f36c050/step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_571_1_Nqu.root"),
                            firstEvent = cms.untracked.uint32(62))

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 1 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:run2_mc_HIon')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    for pset in process.GlobalTag.toGet.value():
        pset.connect = pset.connect.value().replace('frontier://FrontierProd/', 'frontier://FrontierProd/')
    # fix for multi-run processing
    process.GlobalTag.RefreshEachRun = cms.untracked.bool( False )
    process.GlobalTag.ReconnectEachRun = cms.untracked.bool( False )

# customize the L1 emulator to run customiseL1EmulatorFromRaw with HLT to switchToSimStage1Digis
process.load( 'Configuration.StandardSequences.RawToDigi_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
#

# 2015 Run2 emulator
import L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT
process = L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT.customiseL1EmulatorFromRaw( process )

#
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )
# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimStage1Digis( process )

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
#process.load( "DQMServices.Core.DQMStore_cfi" )
#process.DQMStore.enableMultiThread = True

#process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#    fileName = cms.untracked.string("DQMIO.root")
#)

#process.DQMOutput = cms.EndPath( process.dqmOutput )

# add specific customizations
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process)

from L1Trigger.L1TCommon.customsPostLS1 import customiseSimL1EmulatorForPostLS1_HI
customiseSimL1EmulatorForPostLS1_HI(process)
process.load('HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi')
process.hltbitanalysis.HLTProcessName = cms.string('TEST')
process.hltbitanalysis.hltresults = cms.InputTag( 'TriggerResults','','TEST' )
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag('simGtDigis','','TEST')
process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag('gctDigis','','TEST')
process.hltbitanalysis.l1GctHFRingSums = cms.InputTag('gctDigis','','TEST')
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
#process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service('TFileService',
                                   fileName=cms.string('HiForest.root'))
process.L1UpgradeAnalyzer = cms.EDAnalyzer("l1t::L1UpgradeAnalyzer",
                                           InputLayer2Collection = cms.InputTag("simCaloStage1FinalDigis"),
                                           InputLayer2TauCollection = cms.InputTag("simCaloStage1FinalDigis:rlxTaus"),
                                           InputLayer2IsoTauCollection = cms.InputTag("simCaloStage1FinalDigis:isoTaus"),
                                           InputLayer2CaloSpareCollection = cms.InputTag("simCaloStage1FinalDigis:HFRingSums"),
                                           InputLayer1Collection = cms.InputTag("simRctUpgradeFormatDigis"),
                                           legacyRCTDigis = cms.InputTag("simRctDigis")
)
#process.L1UpgradeAnalyzerPath = cms.EndPath(process.L1UpgradeAnalyzer)

#### Begin paste of HiForest configuration here.
######
process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

process.GlobalTag.toGet.extend([
 cms.PSet(record = cms.string("HeavyIonRcd"),
tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v740x01_mc"),
connect = cms.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
label = cms.untracked.string("HFtowersHydjetDrum5")
 ),
])

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_PbPb2760(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs3PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs4PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5CaloJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akVs5PFJetSequence_PbPb_mc_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.jets.akPu5PFJetSequence_PbPb_mc_cff')

process.jetSequences = cms.Sequence(process.akPu3CaloJetSequence +
                                    process.akVs3CaloJetSequence +
                                    process.akVs3PFJetSequence +
                                    process.akPu3PFJetSequence +

                                    process.akPu4CaloJetSequence +
                                    process.akVs4CaloJetSequence +
                                    process.akVs4PFJetSequence +
                                    process.akPu4PFJetSequence

                                    # process.akPu5CaloJetSequence +
                                    # process.akVs5CaloJetSequence +
                                    # process.akVs5PFJetSequence +
                                    # process.akPu5PFJetSequence

                                    )

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(False) #the gen info dataformat has changed in 73X, we need to update hiEvtAnalyzer code
#process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

process.anaTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])

process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity')
process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = False
process.pixelTrack.doPFMatching = False

process.anaTrack.doSimVertex = True
process.anaTrack.doSimTrack = True
# process.ppTrack.fillSimTrack = True

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("hiGeneralTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.genParticleSrc = cms.InputTag("genParticles")
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectronsTmp")

# process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
# process.hltMuTree.doGen = cms.untracked.bool(True)
# process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
# process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("akVs3PFJets")
# process.globalMuons.TrackerCollectionLabel = "hiGeneralTracks"
# process.muons.TrackExtractorPSet.inputTrackCollection = "hiGeneralTracks"
# process.muons.inputCollectionLabels = ["hiGeneralTracks", "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

# HYDJET RECO file didn't have ak2GenJets and ak6GenJets as input, so removed them
# and ran our own hiGenJets sequence
#from RecoHI.HiJetAlgos.HiGenJets_cff import ak3HiGenJets, ak4HiGenJets
#from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJets
#genParticlesForJets.ignoreParticleIDs += cms.vuint32( 12,14,16)

#process.hiSelectGenJets = cms.Sequence(
#    genParticlesForJets +
#    ak3HiGenJets +
#    ak4HiGenJets
#)

process.anaTrack.doSimTrack = cms.untracked.bool(False)

process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")

process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")

process.ana_step = cms.Path(process.L1UpgradeAnalyzer *
                            process.heavyIon*
                            #process.hltanalysis *
#temp                            process.hltobject *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            #process.hiGenJetsCleaned*
                            process.quickTrackAssociatorByHits*
                            #process.tpRecoAssocGeneralTracks + #used in HiPFJetAnalyzer
                            #process.hiSelectGenJets +
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.pfcandAnalyzer +
                            process.rechitAna +
#temp                            process.hltMuTree +
                            process.HiForest +
                            # process.cutsTPForFak +
                            # process.cutsTPForEff +
                            process.anaTrack
                            #process.pixelTrack
                            )
process.hltAnaPath = cms.EndPath(process.hltbitanalysis)

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.phltJetHI = cms.Path( process.hltJetHI )
process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
# process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter ) #should be put back in later
#process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.skimanalysis.hltresults = cms.InputTag("TriggerResults", "", "TEST")
process.pAna = cms.EndPath(process.skimanalysis)

process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.ana_step, process.phltJetHI, process.pcollisionEventSelection, process.phfCoincFilter, process.phfCoincFilter3, process.pprimaryVertexFilter, process.phltPixelClusterShapeFilter, process.phiEcalRecHitSpikeFilter, process.pAna, process.hltAnaPath])

from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('BeamSpotObjectsRcd'),
                                                            tag= cms.string('RealisticHICollisions2011_STARTHI50_mc')
                                                            )),
                                connect =cms.string('frontier://FrontierProd/CMS_COND_31X_BEAMSPOT')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")
