#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Configuration/GenProduction/HI/Pyquen_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_5020GeV_cfi --filein="dbs:/Hijing_PPb502_MinimumBias/HiWinter13-pa-START53_V10-v2/GEN-SIM" --fileout file:pPb_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions  STARTHI53_V27::All --himix --processName HISIGNAL --python_filename cfg_pPb1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 40 --beamspot Match8TeVCollisionPPbBoost
cmsRun -e -j cfg_pPb1_rt.xml cfg_pPb1.py

# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:pPb_GENSIM.root --fileout file:pPb_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon --conditions  STARTHI53_V27::All --himix --no_exec --python_filename cfg_pPb2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 40
cmsRun -e -j cfg_pPb2_rt.xml cfg_pPb2.py

# Third Step is RECO
cmsDriver.py step2 --filein file:pPb_GENSIMRAW.root --fileout file:pPb_RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_V27::All --himix --no_exec --python_filename cfg_pPb3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 40
cmsRun -e -j cfg_pPb3_rt.xml cfg_pPb3.py

echo GEN-SIM step
grep "TotalEvents" cfg_pPb1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb1_rt.xml
grep "PeakValueRss" cfg_pPb1_rt.xml
grep "AvgEventTime" cfg_pPb1_rt.xml
grep "AvgEventCPU" cfg_pPb1_rt.xml
grep "TotalJobCPU" cfg_pPb1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_pPb2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb2_rt.xml
grep "PeakValueRss" cfg_pPb2_rt.xml
grep "AvgEventTime" cfg_pPb2_rt.xml
grep "AvgEventCPU" cfg_pPb2_rt.xml
grep "TotalJobCPU" cfg_pPb2_rt.xml

echo RECO step
grep "TotalEvents" cfg_pPb3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb3_rt.xml
grep "PeakValueRss" cfg_pPb3_rt.xml
grep "AvgEventTime" cfg_pPb3_rt.xml
grep "AvgEventCPU" cfg_pPb3_rt.xml
grep "TotalJobCPU" cfg_pPb3_rt.xml
