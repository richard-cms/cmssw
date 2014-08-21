#!/bin/sh

# First Step is GEN-SIM
#specific to forward
cmsDriver.py Configuration/genproductions/HI/photon_analysis/Pyquen_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_pPb_5020GeV_cfi --filein="dbs:/Hijing_PPb502_MinimumBias/HiWinter13-pa-START53_V10-v1/GEN-SIM" --fileout file:pPb_forward_AllQCDPhoton120_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions  STARTHI53_V27::All --himix --processName HISIGNAL --python_filename cfg_forward_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 20 --beamspot Match8TeVCollisionPPbBoost

#specific to reverse
#cmsDriver.py Configuration/genproductions/HI/photon_analysis/Pyquen_Unquenched_AllQCDPhoton120_PhotonFilter35GeV_eta3_TuneZ2_reversepPb_5020GeV_cfi --filein="dbs:/Hijing_PPb502_MinimumBias/HiWinter13-pa-START53_V10-v2/GEN-SIM" --fileout file:pPb_forward_AllQCDPhoton120_GENSIM.root --eventcontent=RAWSIM --datatier GEN-SIM --step GEN,SIM --conditions  STARTHI53_V27::All --himix --processName HISIGNAL --python_filename cfg_forward_1.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 20 --beamspot Match8TeVCollisionPPbBoost --customise_commands 'process.VtxSmeared.Beta=cms.double(0.434)'

cmsRun -e -j cfg_forward_1_rt.xml cfg_forward_1.py

# Second Step is DIGI2RAW
cmsDriver.py step1 --filein file:pPb_forward_AllQCDPhoton120_GENSIM.root --fileout file:pPb_forward_AllQCDPhoton120_GENSIMRAW.root --eventcontent RAWSIM --datatier GEN-SIM-RAW --step DIGI,L1,DIGI2RAW,HLT:PIon --conditions  STARTHI53_V27::All --himix --no_exec --python_filename cfg_forward_2.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 20
cmsRun -e -j cfg_forward_2_rt.xml cfg_forward_2.py

# Third Step is RECO/validation
#bad version
#cmsDriver.py step2 --filein file:pPb_forward_AllQCDPhoton120_GENSIMRAW.root --fileout file:pPb_forward_AllQCDPhoton120_RECO.root --eventcontent RECODEBUG,DQM --datatier GEN-SIM-RECO,DQM --step GEN:pgen,RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC --customise_commands 'process.genParticles.src="hiSignal" \n process.basicGenParticleValidation.hepmcCollection = cms.InputTag("hiSignal")' --conditions STARTHI53_V27::All --no_exec --python_filename cfg_forward_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 20

# good version
cmsDriver.py step2 --filein file:pPb_forward_AllQCDPhoton120_GENSIMRAW.root --fileout file:pPb_forward_AllQCDPhoton120_RECO.root --eventcontent RECOSIM,DQM --datatier GEN-SIM-RECO,DQM --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC --himix --conditions STARTHI53_V27::All --no_exec --python_filename cfg_forward_3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 20

cmsRun -e -j cfg_forward_3_rt.xml cfg_forward_3.py

echo GEN-SIM step
grep "TotalEvents" cfg_forward_1_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_forward_1_rt.xml
grep "PeakValueRss" cfg_forward_1_rt.xml
grep "AvgEventTime" cfg_forward_1_rt.xml
grep "AvgEventCPU" cfg_forward_1_rt.xml
grep "TotalJobCPU" cfg_forward_1_rt.xml

echo DIGI2RAW step
grep "TotalEvents" cfg_forward_2_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_forward_2_rt.xml
grep "PeakValueRss" cfg_forward_2_rt.xml
grep "AvgEventTime" cfg_forward_2_rt.xml
grep "AvgEventCPU" cfg_forward_2_rt.xml
grep "TotalJobCPU" cfg_forward_2_rt.xml

echo RECO/Validation step
grep "TotalEvents" cfg_forward_3_rt.xml
grep "Timing-tstoragefile-write-totalMegabytes" cfg_forward_3_rt.xml
grep "PeakValueRss" cfg_forward_3_rt.xml
grep "AvgEventTime" cfg_forward_3_rt.xml
grep "AvgEventCPU" cfg_forward_3_rt.xml
grep "TotalJobCPU" cfg_forward_3_rt.xml
