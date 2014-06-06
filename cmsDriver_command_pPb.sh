#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Generator/genproductions/HI/Pyquen_Unquenched_AllQCDPhoton170_PhotonFilter35GeV_eta3_TuneZ2_5020GeV_cfi.py --filein /Hijing_PPb502_MinimumBias/HiWinter13-pa-START53_V10-v1/GEN-SIM --fileout file:GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions  STARTHI53_V27::All --scenario HeavyIons --himix --processName HISIGNAL --python_filename cfg_pPb1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100 --beamspot Match8TeVCollisionPPbBoost
cmsRun -e -j cfg_pPb1_rt.xml cfg_pPb1.py
echo GEN-SIM step
echo 100 were run
grep "TotalEvents" cfg_pPb1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb1_rt.xml
grep "PeakValueRss" cfg_pPb1_rt.xml
grep "AvgEventTime" cfg_pPb1_rt.xml
grep "AvgEventCPU" cfg_pPb1_rt.xml
grep "TotalJobCPU" cfg_pPb1_rt.xml


# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:GENSIM.root --fileout file:GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon,RAW2DIGI,L1Reco --conditions  STARTHI53_V27::All --himix --scenario HeavyIons --no_exec --python_filename cfg_pPb2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
cmsRun -e -j cfg_pPb2_rt.xml cfg_pPb2.py
echo DIGI2RAW step
echo 100 events were ran
grep "TotalEvents" cfg_pPb2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb2_rt.xml
grep "PeakValueRss" cfg_pPb2_rt.xml
grep "AvgEventTime" cfg_pPb2_rt.xml
grep "AvgEventCPU" cfg_pPb2_rt.xml
grep "TotalJobCPU" cfg_pPb2_rt.xml

# Third Step is RECO
cmsDriver.py step2 --filein file:GENSIMRAW.root --fileout file:RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_V27::All --himix --scenario HeavyIons --no_exec --python_filename cfg_pPb3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
cmsRun -e -j cfg_pPb3_rt.xml cfg_pPb3.py
echo RECO step
echo 100 events were ran
grep "TotalEvents" cfg_pPb3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb3_rt.xml
grep "PeakValueRss" cfg_pPb3_rt.xml
grep "AvgEventTime" cfg_pPb3_rt.xml
grep "AvgEventCPU" cfg_pPb3_rt.xml
grep "TotalJobCPU" cfg_pPb3_rt.xml
