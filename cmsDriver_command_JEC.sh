#!/bin/sh

#############################
## PbPb JEC #################
#############################

# First Step is GEN-SIM
cmsDriver.py Configuration/genproductions/python/HI/photon_analysis/Pyquen_JEC_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_2760GeV_cfi.py --fileout file:PbPb_JEC_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_LV1::All --scenario HeavyIons --processName GENERATOR --beamspot RealisticHI2011Collision --python_filename cfg_PbPb_JEC_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_PbPb_JEC_1_rt.xml cfg_PbPb_JEC_1.py

# Second Step is DIGI2RAW
# RAWDEBUG
cmsDriver.py step1 --filein file:PbPb_JEC_GENSIM.root --fileout file:PbPb_JEC_GENSIMRAW.root --eventcontent RAWDEBUG --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:HIon --conditions STARTHI53_LV1::All --scenario HeavyIons --no_exec --python_filename cfg_PbPb_JEC_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_PbPb_JEC_2_rt.xml cfg_PbPb_JEC_2.py

# Third Step is RECO
#RECODEBUG
cmsDriver.py step2 --filein file:PbPb_JEC_GENSIMRAW.root --fileout file:PbPb_JEC_RECO.root --eventcontent RECODEBUG --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_LV1::All --scenario HeavyIons --no_exec --python_filename cfg_PbPb_JEC_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 --inputCommands "keep *,drop *_g4SimHits_*_*"

cmsRun -e -j cfg_PbPb_JEC_3_rt.xml cfg_PbPb_JEC_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_PbPb_JEC_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_JEC_1_rt.xml
grep "PeakValueRss" cfg_PbPb_JEC_1_rt.xml
grep "AvgEventTime" cfg_PbPb_JEC_1_rt.xml
grep "AvgEventCPU" cfg_PbPb_JEC_1_rt.xml
grep "TotalJobCPU" cfg_PbPb_JEC_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_PbPb_JEC_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_JEC_2_rt.xml
grep "PeakValueRss" cfg_PbPb_JEC_2_rt.xml
grep "AvgEventTime" cfg_PbPb_JEC_2_rt.xml
grep "AvgEventCPU" cfg_PbPb_JEC_2_rt.xml
grep "TotalJobCPU" cfg_PbPb_JEC_2_rt.xml

echo RECO step
grep "TotalEvents" cfg_PbPb_JEC_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_PbPb_JEC_3_rt.xml
grep "PeakValueRss" cfg_PbPb_JEC_3_rt.xml
grep "AvgEventTime" cfg_PbPb_JEC_3_rt.xml
grep "AvgEventCPU" cfg_PbPb_JEC_3_rt.xml
grep "TotalJobCPU" cfg_PbPb_JEC_3_rt.xml

#############################
## pPb JEC #################
#############################

# First Step is GEN-SIM
cmsDriver.py Configuration/genproductions/python/HI/photon_analysis/Pyquen_JEC_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_pPb_5020GeV_cfi.py --fileout file:pPb_JEC_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_V27::All --processName GENERATOR --beamspot Realistic8TeVCollisionPPbBoost --python_filename cfg_pPb_JEC_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_pPb_JEC_1_rt.xml cfg_pPb_JEC_1.py

# Second Step is DIGI2RAW
# RAWDEBUG
cmsDriver.py step1 --filein file:pPb_JEC_GENSIM.root --fileout file:pPb_JEC_GENSIMRAW.root --eventcontent RAWSIM --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon --conditions STARTHI53_V27::All --no_exec --python_filename cfg_pPb_JEC_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

#cmsRun -e -j cfg_pPb_JEC_2_rt.xml cfg_pPb_JEC_2.py

# Third Step is RECO
#RECODEBUG
cmsDriver.py step2 --filein file:pPb_JEC_GENSIMRAW.root --fileout file:pPb_JEC_RECO.root --eventcontent RECOSIM --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_V27::All --no_exec --python_filename cfg_pPb_JEC_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_pPb_JEC_3_rt.xml cfg_pPb_JEC_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_pPb_JEC_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb_JEC_1_rt.xml
grep "PeakValueRss" cfg_pPb_JEC_1_rt.xml
grep "AvgEventTime" cfg_pPb_JEC_1_rt.xml
grep "AvgEventCPU" cfg_pPb_JEC_1_rt.xml
grep "TotalJobCPU" cfg_pPb_JEC_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_pPb_JEC_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb_JEC_2_rt.xml
grep "PeakValueRss" cfg_pPb_JEC_2_rt.xml
grep "AvgEventTime" cfg_pPb_JEC_2_rt.xml
grep "AvgEventCPU" cfg_pPb_JEC_2_rt.xml
grep "TotalJobCPU" cfg_pPb_JEC_2_rt.xml

echo RECO step
grep "TotalEvents" cfg_pPb_JEC_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pPb_JEC_3_rt.xml
grep "PeakValueRss" cfg_pPb_JEC_3_rt.xml
grep "AvgEventTime" cfg_pPb_JEC_3_rt.xml
grep "AvgEventCPU" cfg_pPb_JEC_3_rt.xml
grep "TotalJobCPU" cfg_pPb_JEC_3_rt.xml


#############################
## pp JEC #################
#############################

# First Step is GEN-SIM
cmsDriver.py Configuration/genproductions/python/HI/photon_analysis/Pyquen_JEC_pp_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_2760GeV_cfi.py --fileout file:pp_JEC_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions STARTHI53_V28::All --processName GENERATOR --beamspot Realistic2p76TeV2013Collision --python_filename cfg_pp_JEC_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_pp_JEC_1_rt.xml cfg_pp_JEC_1.py

# Second Step is DIGI2RAW
# RAWDEBUG
cmsDriver.py step1 --filein file:pp_JEC_GENSIM.root --fileout file:pp_JEC_GENSIMRAW.root --eventcontent RAWSIM --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon --conditions STARTHI53_V28::All --no_exec --python_filename cfg_pp_JEC_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_pp_JEC_2_rt.xml cfg_pp_JEC_2.py

# Third Step is RECO
#RECODEBUG
cmsDriver.py step2 --filein file:pp_JEC_GENSIMRAW.root --fileout file:pp_JEC_RECO.root --eventcontent RECOSIM --datatier GEN-SIM-RECO --step RAW2DIGI,L1Reco,RECO --conditions STARTHI53_V28::All --no_exec --python_filename cfg_pp_JEC_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsRun -e -j cfg_pp_JEC_3_rt.xml cfg_pp_JEC_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_pp_JEC_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pp_JEC_1_rt.xml
grep "PeakValueRss" cfg_pp_JEC_1_rt.xml
grep "AvgEventTime" cfg_pp_JEC_1_rt.xml
grep "AvgEventCPU" cfg_pp_JEC_1_rt.xml
grep "TotalJobCPU" cfg_pp_JEC_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_pp_JEC_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pp_JEC_2_rt.xml
grep "PeakValueRss" cfg_pp_JEC_2_rt.xml
grep "AvgEventTime" cfg_pp_JEC_2_rt.xml
grep "AvgEventCPU" cfg_pp_JEC_2_rt.xml
grep "TotalJobCPU" cfg_pp_JEC_2_rt.xml

echo RECO step
grep "TotalEvents" cfg_pp_JEC_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_pp_JEC_3_rt.xml
grep "PeakValueRss" cfg_pp_JEC_3_rt.xml
grep "AvgEventTime" cfg_pp_JEC_3_rt.xml
grep "AvgEventCPU" cfg_pp_JEC_3_rt.xml
grep "TotalJobCPU" cfg_pp_JEC_3_rt.xml
