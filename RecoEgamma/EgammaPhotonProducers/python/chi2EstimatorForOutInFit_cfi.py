import FWCore.ParameterSet.Config as cms

import TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer_cfi
Chi2MeasurementEstimatorForOutIn = TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer_cfi.Chi2MeasurementEstimator.clone()
Chi2MeasurementEstimatorForOutIn.ComponentName = 'Chi2ForOutIn'
Chi2MeasurementEstimatorForOutIn.MaxChi2 = 500.
Chi2MeasurementEstimatorForOutIn.nSigma = 3.

