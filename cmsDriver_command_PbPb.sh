#!/bin/sh

# First Step is GEN-SIM
#cmsDriver.py Configuration/genproductions/python/HI/photon_analysis/Pyquen_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_2760GeV_cfi.py --filein="dbs:/Hydjet1p8_TuneDrum_Quenched_MinBias_2760GeV/HiFall13-STARTHI53_V28-v2/GEN-SIM" --fileout file:PbPb_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_LV1::All --scenario HeavyIons --himix --processName HISIGNAL --python_filename cfg_PbPb_1.py --no_exec --beamspot MatchHI --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

#cmsRun -e -j cfg_PbPbDebug_1_rt.xml cfg_PbPbDebug_1.py

# Second Step is DIGI2RAW
# RAWSIM
#cmsDriver.py step1 --filein file:PbPb_GENSIM.root --fileout file:PbPb_GENSIMRAW.root --eventcontent RAWSIM --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg_PbPb_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

# RAWDEBUG
#cmsDriver.py step1 --filein file:PbPb_GENSIM.root --fileout file:PbPbDEBUG_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg_PbPb_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
#cmsRun -e -j cfg_PbPb_2_rt.xml cfg_PbPb_2.py

# Third Step is RECO
#RECOSIM
#cmsDriver.py step2 --filein file:PbPb_GENSIMRAW.root --fileout file:PbPb_RECO.root --eventcontent RECOSIM --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg_PbPb_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 --inputCommands "keep *,drop *_g4SimHits_*_*"
#RECODEBUG
cmsDriver.py step2 --filein file:PbPbDEBUG_GENSIMRAW.root --fileout file:PbPbDEBUG_RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --himix --scenario HeavyIons --no_exec --python_filename cfg_PbPb_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 --inputCommands "keep *,drop *_g4SimHits_*_*"

cmsRun -e -j cfg_PbPb_3_rt.xml cfg_PbPb_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_PbPb_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_1_rt.xml
grep "PeakValueRss" cfg_PbPb_1_rt.xml
grep "AvgEventTime" cfg_PbPb_1_rt.xml
grep "AvgEventCPU" cfg_PbPb_1_rt.xml
grep "TotalJobCPU" cfg_PbPb_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_PbPb_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_2_rt.xml
grep "PeakValueRss" cfg_PbPb_2_rt.xml
grep "AvgEventTime" cfg_PbPb_2_rt.xml
grep "AvgEventCPU" cfg_PbPb_2_rt.xml
grep "TotalJobCPU" cfg_PbPb_2_rt.xml

echo RECO step
grep "TotalEvents" cfg_PbPb_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_3_rt.xml
grep "PeakValueRss" cfg_PbPb_3_rt.xml
grep "AvgEventTime" cfg_PbPb_3_rt.xml
grep "AvgEventCPU" cfg_PbPb_3_rt.xml
grep "TotalJobCPU" cfg_PbPb_3_rt.xml
