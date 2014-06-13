#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Configuration/GenProduction/HI/Pyquen_Unquenched_EmEnrichedDijet170_ParticleFilter35GeV_eta3_TuneZ2_2760GeV_cfi --filein="dbs:/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HiFall13-STARTHI53_V28-v2/GEN-SIM" --fileout file:PbPb_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_LV1::All --scenario HeavyIons --himix --processName HISIGNAL --python_filename cfg1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 50
cmsRun -e -j cfg1_rt.xml cfg1.py

# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:PbPb_GENSIM.root --fileout file:PbPb_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 50
cmsRun -e -j cfg2_rt.xml cfg2.py

# Third Step is RECO
cmsDriver.py step2 --filein file:PbPb_GENSIMRAW.root --fileout file:PbPb_RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 50
cmsRun -e -j cfg3_rt.xml cfg3.py

echo GEN-SIM step
grep "TotalEvents" cfg1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg1_rt.xml
grep "PeakValueRss" cfg1_rt.xml
grep "AvgEventTime" cfg1_rt.xml
grep "AvgEventCPU" cfg1_rt.xml
grep "TotalJobCPU" cfg1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg2_rt.xml
grep "PeakValueRss" cfg2_rt.xml
grep "AvgEventTime" cfg2_rt.xml
grep "AvgEventCPU" cfg2_rt.xml
grep "TotalJobCPU" cfg2_rt.xml

echo RECO step
grep "TotalEvents" cfg3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg3_rt.xml
grep "PeakValueRss" cfg3_rt.xml
grep "AvgEventTime" cfg3_rt.xml
grep "AvgEventCPU" cfg3_rt.xml
grep "TotalJobCPU" cfg3_rt.xml
