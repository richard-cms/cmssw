#!/bin/sh

# First Step is GEN-SIM
cmsDriver.py Configuration/genproductions/python/HI/photon_analysis/Pythia_AllQCDPhoton170_PhotonFilter35GeV_eta3_TuneZ2_2760GeV_cfi.py --fileout file:JEC_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_LV1::All --scenario HeavyIons --processName GENERATOR --beamspot RealisticHI2011Collision --python_filename cfg_JEC_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_JEC_1_rt.xml cfg_JEC_1.py

# Second Step is DIGI2RAW
# RAWDEBUG
cmsDriver.py step1 --filein file:JEC_GENSIM.root --fileout file:JEC_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon --conditions STARTHI53_LV1::All --scenario HeavyIons --beamspot RealisticHI2011Collision --no_exec --python_filename cfg_JEC_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_JEC_2_rt.xml cfg_JEC_2.py

# Third Step is RECO
#RECODEBUG
cmsDriver.py step2 --filein file:JEC_GENSIMRAW.root --fileout file:JEC_RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --scenario HeavyIons --beamspot RealisticHI2011Collision --no_exec --python_filename cfg_JEC_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 --inputCommands "keep *,drop *_g4SimHits_*_*"

cmsRun -e -j cfg_JEC_3_rt.xml cfg_JEC_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_JEC_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_JEC_1_rt.xml
grep "PeakValueRss" cfg_JEC_1_rt.xml
grep "AvgEventTime" cfg_JEC_1_rt.xml
grep "AvgEventCPU" cfg_JEC_1_rt.xml
grep "TotalJobCPU" cfg_JEC_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_JEC_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_JEC_2_rt.xml
grep "PeakValueRss" cfg_JEC_2_rt.xml
grep "AvgEventTime" cfg_JEC_2_rt.xml
grep "AvgEventCPU" cfg_JEC_2_rt.xml
grep "TotalJobCPU" cfg_JEC_2_rt.xml

echo RECO step
grep "TotalEvents" cfg_JEC_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_JEC_3_rt.xml
grep "PeakValueRss" cfg_JEC_3_rt.xml
grep "AvgEventTime" cfg_JEC_3_rt.xml
grep "AvgEventCPU" cfg_JEC_3_rt.xml
grep "TotalJobCPU" cfg_JEC_3_rt.xml
