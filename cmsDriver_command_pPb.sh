#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Configuration/genproductions/HI/Pyquen_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_5020GeV_cfi --filein="dbs:/Hijing_PPb502_MinimumBias/HiWinter13-pa-START53_V10-v1/GEN-SIM" --fileout file:pPb_forward_AllQCDPhoton120_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions  STARTHI53_V27::All --himix --processName HISIGNAL --python_filename cfg1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 40 --beamspot Match8TeVCollisionPPbBoost
cmsRun -e -j cfg1_rt.xml cfg1.py

# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:pPb_forward_AllQCDPhoton120_GENSIM.root --fileout file:pPb_forward_AllQCDPhoton120_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon --conditions  STARTHI53_V27::All --himix --no_exec --python_filename cfg2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 40
cmsRun -e -j cfg2_rt.xml cfg2.py

# Third Step is RECO
cmsDriver.py step2 --filein file:pPb_forward_AllQCDPhoton120_GENSIMRAW.root --fileout file:pPb_forward_AllQCDPhoton120RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_V27::All --himix --no_exec --python_filename cfg3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 40
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
