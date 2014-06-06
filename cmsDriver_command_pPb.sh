#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Configuration/GenProduction/Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt35_eta30_TuneZ2_Unquenched_2760GeV_cfi --filein="dbs:/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HiFall13-STARTHI53_V28-v2/GEN-SIM" --fileout file:GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_LV1::All --scenario HeavyIons --himix --processName HISIGNAL --python_filename cfg1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
cmsRun -e -j cfg1_rt.xml cfg1.py
echo GEN-SIM step
echo 100 were run
grep "TotalEvents" cfg1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg1_rt.xml
grep "PeakValueRss" cfg1_rt.xml
grep "AvgEventTime" cfg1_rt.xml
grep "AvgEventCPU" cfg1_rt.xml
grep "TotalJobCPU" cfg1_rt.xml


# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:GENSIM.root --fileout file:GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
cmsRun -e -j cfg2_rt.xml cfg2.py
echo DIGI2RAW step
echo 100 events were ran
grep "TotalEvents" cfg2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg2_rt.xml
grep "PeakValueRss" cfg2_rt.xml
grep "AvgEventTime" cfg2_rt.xml
grep "AvgEventCPU" cfg2_rt.xml
grep "TotalJobCPU" cfg2_rt.xml

# Third Step is RECO
cmsDriver.py step2 --filein file:GENSIMRAW.root --fileout file:RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
cmsRun -e -j cfg3_rt.xml cfg3.py
echo RECO step
echo 100 events were ran
grep "TotalEvents" cfg3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg3_rt.xml
grep "PeakValueRss" cfg3_rt.xml
grep "AvgEventTime" cfg3_rt.xml
grep "AvgEventCPU" cfg3_rt.xml
grep "TotalJobCPU" cfg3_rt.xml
