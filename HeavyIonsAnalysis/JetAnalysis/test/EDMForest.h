//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Aug  4 22:51:03 2014 by ROOT version 5.32/00
// from TTree Events/
// found on file: EDMForest.root
//////////////////////////////////////////////////////////

#ifndef EDMForest_h
#define EDMForest_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <vector>

// Header file for the classes stored in the TTree if any.
using namespace std;

// Fixed size dimensions of array or collections stored in the TTree if any.
const Int_t kMaxfloat_akPu3PFJetAnalyzer_b_HiForest = 1;
const Int_t kMaxfloat_akPu3PFJetAnalyzer_hf_HiForest = 1;
const Int_t kMaxfloat_akPu3PFJetAnalyzer_pthat_HiForest = 1;
const Int_t kMaxfloat_akPu3PFJetAnalyzer_vx_HiForest = 1;
const Int_t kMaxfloat_akPu3PFJetAnalyzer_vy_HiForest = 1;
const Int_t kMaxfloat_akPu3PFJetAnalyzer_vz_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_bMult_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_beamId1_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_beamId2_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_bin_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_evt_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_lumi_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_nHLTBit_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_nIP_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_nL1ABit_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_nL1TBit_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_ngen_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_nref_HiForest = 1;
const Int_t kMaxint_akPu3PFJetAnalyzer_run_HiForest = 1;
const Int_t kMaxbools_akPu3PFJetAnalyzer_hltBit_HiForest = 1;
const Int_t kMaxbools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest = 1;
const Int_t kMaxbools_akPu3PFJetAnalyzer_l1ABit_HiForest = 1;
const Int_t kMaxbools_akPu3PFJetAnalyzer_l1TBit_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_apprHPD_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_apprRBX_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bEta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bPhi_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bVx_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bVy_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_bVz_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_chargedHardSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_chargedMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_chargedSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrcsvMva_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrfr01_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrmuByPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrprob_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrprobb_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_eMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_eSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ecalSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fEB_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fEE_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fHB_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fHE_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fHFOOT_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fHO_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fHPD_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fLS_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fLong_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fRBX_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fShort_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fSubDet1_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fSubDet2_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fSubDet3_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_fSubDet4_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_genChargedSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_genHardSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_gendphijt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_gendrjt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_geneta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_genphi_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_genpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_geny_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_hcalSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ip2d_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ip2dSig_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ip3d_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ip3dSig_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipChi2_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipDxy_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipDz_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipEta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipProb0_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipProb1_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ipPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jteta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jtm_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jtphi_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jtpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jtpu_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_jty_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_matchedPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_matchedPu_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_matchedR_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_matchedRawPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_muMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_muSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_mudr_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_mue_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_mueta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_muphi_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_mupt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_muptrel_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrprob_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_neutralMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_neutralSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_pdiscrprob_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_photonHardSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_photonMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_photonSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_rawpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refdphijt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refdrjt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refeta_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refpartonpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refphi_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_refy_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_restrictedEMF_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_signalChargedSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_signalHardSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_svtxdl_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_svtxdls_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_svtxm_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_svtxpt_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_trackHardSum_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_trackMax_HiForest = 1;
const Int_t kMaxfloats_akPu3PFJetAnalyzer_trackSum_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_bChg_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_bJetIndex_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_bPdg_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_bStatus_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_chargedHardN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_chargedN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_eN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_genmatchindex_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_gensubid_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_ipJetIndex_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_ipNHit_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_muN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_muchg_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_n2RPC_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_n3RPC_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_n90_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nECAL_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nHCAL_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nIPtrk_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nRPC_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_neutralN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nselIPtrk_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_nsvtx_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_photonHardN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_photonN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_refpartonflavor_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_subid_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_svtxntrk_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_trackHardN_HiForest = 1;
const Int_t kMaxints_akPu3PFJetAnalyzer_trackN_HiForest = 1;

class EDMForest {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   //edm::EventAuxiliary *EventAuxiliary;
   //vector<edm::StoredProductProvenance> *EventProductProvenance;
   //vector<edm::Hash<1> > *EventSelections;
   vector<unsigned short> *BranchListIndexes;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_b_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_b_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_b_HiForest_obj;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_hf_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_hf_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_hf_HiForest_obj;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_pthat_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_pthat_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_pthat_HiForest_obj;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_vx_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_vx_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_vx_HiForest_obj;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_vy_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_vy_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_vy_HiForest_obj;
 //edm::Wrapper<float> *float_akPu3PFJetAnalyzer_vz_HiForest_;
   Bool_t          float_akPu3PFJetAnalyzer_vz_HiForest_present;
   Float_t         float_akPu3PFJetAnalyzer_vz_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_bMult_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_bMult_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_bMult_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_beamId1_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_beamId1_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_beamId1_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_beamId2_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_beamId2_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_beamId2_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_bin_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_bin_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_bin_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_evt_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_evt_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_evt_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_lumi_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_lumi_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_lumi_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_nHLTBit_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_nHLTBit_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_nHLTBit_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_nIP_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_nIP_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_nIP_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_nL1ABit_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_nL1ABit_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_nL1ABit_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_nL1TBit_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_nL1TBit_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_nL1TBit_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_ngen_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_ngen_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_ngen_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_nref_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_nref_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_nref_HiForest_obj;
 //edm::Wrapper<int> *int_akPu3PFJetAnalyzer_run_HiForest_;
   Bool_t          int_akPu3PFJetAnalyzer_run_HiForest_present;
   Int_t           int_akPu3PFJetAnalyzer_run_HiForest_obj;
 //edm::Wrapper<vector<bool> > *bools_akPu3PFJetAnalyzer_hltBit_HiForest_;
   Bool_t          bools_akPu3PFJetAnalyzer_hltBit_HiForest_present;
   vector<bool>    bools_akPu3PFJetAnalyzer_hltBit_HiForest_obj;
 //edm::Wrapper<vector<bool> > *bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_;
   Bool_t          bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_present;
   vector<bool>    bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_obj;
 //edm::Wrapper<vector<bool> > *bools_akPu3PFJetAnalyzer_l1ABit_HiForest_;
   Bool_t          bools_akPu3PFJetAnalyzer_l1ABit_HiForest_present;
   vector<bool>    bools_akPu3PFJetAnalyzer_l1ABit_HiForest_obj;
 //edm::Wrapper<vector<bool> > *bools_akPu3PFJetAnalyzer_l1TBit_HiForest_;
   Bool_t          bools_akPu3PFJetAnalyzer_l1TBit_HiForest_present;
   vector<bool>    bools_akPu3PFJetAnalyzer_l1TBit_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_apprHPD_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_apprHPD_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_apprHPD_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_apprRBX_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_apprRBX_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_apprRBX_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bEta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bEta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bEta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bPhi_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bPhi_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bPhi_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bVx_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bVx_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bVx_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bVy_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bVy_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bVy_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_bVz_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_bVz_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_bVz_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_chargedMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_chargedMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_chargedMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_chargedSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_chargedSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_chargedSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrfr01_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrfr01_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrfr01_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrprob_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrprob_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrprob_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrprobb_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrprobb_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrprobb_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_eMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_eMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_eMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_eSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_eSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_eSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ecalSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ecalSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ecalSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fEB_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fEB_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fEB_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fEE_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fEE_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fEE_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fHB_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fHB_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fHB_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fHE_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fHE_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fHE_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fHO_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fHO_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fHO_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fHPD_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fHPD_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fHPD_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fLS_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fLS_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fLS_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fLong_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fLong_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fLong_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fRBX_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fRBX_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fRBX_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fShort_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fShort_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fShort_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_genHardSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_genHardSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_genHardSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_gendphijt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_gendphijt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_gendphijt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_gendrjt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_gendrjt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_gendrjt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_geneta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_geneta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_geneta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_genphi_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_genphi_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_genphi_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_genpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_genpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_genpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_geny_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_geny_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_geny_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_hcalSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_hcalSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_hcalSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ip2d_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ip2d_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ip2d_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ip3d_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ip3d_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ip3d_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipChi2_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipChi2_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipChi2_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipDxy_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipDxy_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipDxy_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipDz_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipDz_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipDz_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipEta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipEta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipEta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipProb0_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipProb0_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipProb0_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipProb1_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipProb1_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipProb1_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ipPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ipPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ipPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jteta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jteta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jteta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jtm_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jtm_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jtm_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jtphi_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jtphi_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jtphi_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jtpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jtpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jtpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jtpu_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jtpu_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jtpu_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_jty_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_jty_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_jty_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_matchedPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_matchedPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_matchedPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_matchedPu_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_matchedPu_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_matchedPu_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_matchedR_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_matchedR_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_matchedR_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_muMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_muMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_muMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_muSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_muSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_muSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_mudr_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_mudr_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_mudr_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_mue_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_mue_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_mue_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_mueta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_mueta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_mueta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_muphi_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_muphi_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_muphi_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_mupt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_mupt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_mupt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_muptrel_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_muptrel_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_muptrel_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_neutralMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_neutralMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_neutralMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_neutralSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_neutralSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_neutralSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_photonMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_photonMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_photonMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_photonSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_photonSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_photonSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_rawpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_rawpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_rawpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refdphijt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refdphijt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refdphijt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refdrjt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refdrjt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refdrjt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refeta_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refeta_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refeta_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refphi_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refphi_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refphi_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_refy_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_refy_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_refy_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_svtxdl_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_svtxdl_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_svtxdl_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_svtxdls_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_svtxdls_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_svtxdls_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_svtxm_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_svtxm_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_svtxm_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_svtxpt_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_svtxpt_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_svtxpt_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_trackMax_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_trackMax_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_trackMax_HiForest_obj;
 //edm::Wrapper<vector<float> > *floats_akPu3PFJetAnalyzer_trackSum_HiForest_;
   Bool_t          floats_akPu3PFJetAnalyzer_trackSum_HiForest_present;
   vector<float>   floats_akPu3PFJetAnalyzer_trackSum_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_bChg_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_bChg_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_bChg_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_bPdg_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_bPdg_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_bPdg_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_bStatus_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_bStatus_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_bStatus_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_chargedN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_chargedN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_chargedN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_eN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_eN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_eN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_gensubid_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_gensubid_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_gensubid_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_ipNHit_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_ipNHit_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_ipNHit_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_muN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_muN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_muN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_muchg_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_muchg_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_muchg_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_n2RPC_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_n2RPC_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_n2RPC_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_n3RPC_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_n3RPC_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_n3RPC_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_n90_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_n90_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_n90_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nECAL_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nECAL_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nECAL_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nHCAL_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nHCAL_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nHCAL_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nRPC_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nRPC_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nRPC_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_neutralN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_neutralN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_neutralN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_nsvtx_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_nsvtx_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_nsvtx_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_photonHardN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_photonHardN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_photonHardN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_photonN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_photonN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_photonN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_subid_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_subid_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_subid_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_trackHardN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_trackHardN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_trackHardN_HiForest_obj;
 //edm::Wrapper<vector<int> > *ints_akPu3PFJetAnalyzer_trackN_HiForest_;
   Bool_t          ints_akPu3PFJetAnalyzer_trackN_HiForest_present;
   vector<int>     ints_akPu3PFJetAnalyzer_trackN_HiForest_obj;

   // List of branches
   TBranch        *b_EventAuxiliary;   //!
   TBranch        *b_EventProductProvenance;   //!
   TBranch        *b_EventSelections;   //!
   TBranch        *b_BranchListIndexes;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_b_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_b_HiForest_obj;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_hf_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_hf_HiForest_obj;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_pthat_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_pthat_HiForest_obj;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vx_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vx_HiForest_obj;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vy_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vy_HiForest_obj;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vz_HiForest_present;   //!
   TBranch        *b_float_akPu3PFJetAnalyzer_vz_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_bMult_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_bMult_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_beamId1_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_beamId1_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_beamId2_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_beamId2_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_bin_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_bin_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_evt_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_evt_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_lumi_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_lumi_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nHLTBit_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nHLTBit_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nIP_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nIP_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nL1ABit_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nL1ABit_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nL1TBit_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nL1TBit_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_ngen_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_ngen_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nref_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_nref_HiForest_obj;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_run_HiForest_present;   //!
   TBranch        *b_int_akPu3PFJetAnalyzer_run_HiForest_obj;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_hltBit_HiForest_present;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_hltBit_HiForest_obj;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_present;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_obj;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_l1ABit_HiForest_present;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_l1ABit_HiForest_obj;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_l1TBit_HiForest_present;   //!
   TBranch        *b_bools_akPu3PFJetAnalyzer_l1TBit_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_apprHPD_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_apprHPD_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_apprRBX_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_apprRBX_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bEta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bEta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bPhi_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bPhi_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVx_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVx_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVy_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVy_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVz_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_bVz_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_chargedSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrfr01_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrfr01_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrprob_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrprob_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrprobb_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrprobb_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_eMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_eMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_eSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_eSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ecalSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ecalSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fEB_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fEB_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fEE_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fEE_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHB_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHB_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHE_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHE_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHO_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHO_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHPD_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fHPD_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fLS_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fLS_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fLong_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fLong_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fRBX_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fRBX_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fShort_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fShort_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genHardSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genHardSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_gendphijt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_gendphijt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_gendrjt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_gendrjt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_geneta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_geneta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genphi_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genphi_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_genpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_geny_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_geny_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_hcalSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_hcalSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip2d_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip2d_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip3d_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip3d_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipChi2_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipChi2_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDxy_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDxy_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDz_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipDz_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipEta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipEta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipProb0_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipProb0_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipProb1_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipProb1_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ipPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jteta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jteta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtm_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtm_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtphi_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtphi_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtpu_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jtpu_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jty_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_jty_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedPu_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedPu_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedR_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedR_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mudr_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mudr_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mue_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mue_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mueta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mueta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muphi_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muphi_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mupt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_mupt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muptrel_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_muptrel_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_neutralMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_neutralMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_neutralSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_neutralSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_photonSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_rawpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_rawpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refdphijt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refdphijt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refdrjt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refdrjt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refeta_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refeta_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refphi_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refphi_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refy_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_refy_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxdl_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxdl_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxdls_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxdls_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxm_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxm_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxpt_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_svtxpt_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackMax_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackMax_HiForest_obj;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackSum_HiForest_present;   //!
   TBranch        *b_floats_akPu3PFJetAnalyzer_trackSum_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bChg_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bChg_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bPdg_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bPdg_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bStatus_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_bStatus_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_chargedN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_chargedN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_eN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_eN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_gensubid_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_gensubid_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHit_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHit_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_muN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_muN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_muchg_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_muchg_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n2RPC_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n2RPC_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n3RPC_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n3RPC_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n90_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_n90_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nECAL_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nECAL_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nHCAL_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nHCAL_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nRPC_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nRPC_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_neutralN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_neutralN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nsvtx_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_nsvtx_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_photonHardN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_photonHardN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_photonN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_photonN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_subid_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_subid_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_trackHardN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_trackHardN_HiForest_obj;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_trackN_HiForest_present;   //!
   TBranch        *b_ints_akPu3PFJetAnalyzer_trackN_HiForest_obj;   //!

   EDMForest(TTree *tree=0);
   virtual ~EDMForest();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef EDMForest_cxx
EDMForest::EDMForest(TTree *tree) : fChain(0)
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("EDMForest.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("EDMForest.root");
      }
      f->GetObject("Events",tree);

   }
   Init(tree);
}

EDMForest::~EDMForest()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t EDMForest::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t EDMForest::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void EDMForest::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   //EventAuxiliary = 0;
   //EventProductProvenance = 0;
   //EventSelections = 0;
   BranchListIndexes = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   //fChain->SetBranchAddress("EventAuxiliary", &EventAuxiliary, &b_EventAuxiliary);
   //fChain->SetBranchAddress("EventProductProvenance", &EventProductProvenance, &b_EventProductProvenance);
   //fChain->SetBranchAddress("EventSelections", &EventSelections, &b_EventSelections);
   fChain->SetBranchAddress("BranchListIndexes", &BranchListIndexes, &b_BranchListIndexes);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_b_HiForest.present", &float_akPu3PFJetAnalyzer_b_HiForest_present, &b_float_akPu3PFJetAnalyzer_b_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_b_HiForest.obj", &float_akPu3PFJetAnalyzer_b_HiForest_obj, &b_float_akPu3PFJetAnalyzer_b_HiForest_obj);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_hf_HiForest.present", &float_akPu3PFJetAnalyzer_hf_HiForest_present, &b_float_akPu3PFJetAnalyzer_hf_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_hf_HiForest.obj", &float_akPu3PFJetAnalyzer_hf_HiForest_obj, &b_float_akPu3PFJetAnalyzer_hf_HiForest_obj);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_pthat_HiForest.present", &float_akPu3PFJetAnalyzer_pthat_HiForest_present, &b_float_akPu3PFJetAnalyzer_pthat_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_pthat_HiForest.obj", &float_akPu3PFJetAnalyzer_pthat_HiForest_obj, &b_float_akPu3PFJetAnalyzer_pthat_HiForest_obj);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vx_HiForest.present", &float_akPu3PFJetAnalyzer_vx_HiForest_present, &b_float_akPu3PFJetAnalyzer_vx_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vx_HiForest.obj", &float_akPu3PFJetAnalyzer_vx_HiForest_obj, &b_float_akPu3PFJetAnalyzer_vx_HiForest_obj);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vy_HiForest.present", &float_akPu3PFJetAnalyzer_vy_HiForest_present, &b_float_akPu3PFJetAnalyzer_vy_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vy_HiForest.obj", &float_akPu3PFJetAnalyzer_vy_HiForest_obj, &b_float_akPu3PFJetAnalyzer_vy_HiForest_obj);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vz_HiForest.present", &float_akPu3PFJetAnalyzer_vz_HiForest_present, &b_float_akPu3PFJetAnalyzer_vz_HiForest_present);
   fChain->SetBranchAddress("float_akPu3PFJetAnalyzer_vz_HiForest.obj", &float_akPu3PFJetAnalyzer_vz_HiForest_obj, &b_float_akPu3PFJetAnalyzer_vz_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_bMult_HiForest.present", &int_akPu3PFJetAnalyzer_bMult_HiForest_present, &b_int_akPu3PFJetAnalyzer_bMult_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_bMult_HiForest.obj", &int_akPu3PFJetAnalyzer_bMult_HiForest_obj, &b_int_akPu3PFJetAnalyzer_bMult_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_beamId1_HiForest.present", &int_akPu3PFJetAnalyzer_beamId1_HiForest_present, &b_int_akPu3PFJetAnalyzer_beamId1_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_beamId1_HiForest.obj", &int_akPu3PFJetAnalyzer_beamId1_HiForest_obj, &b_int_akPu3PFJetAnalyzer_beamId1_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_beamId2_HiForest.present", &int_akPu3PFJetAnalyzer_beamId2_HiForest_present, &b_int_akPu3PFJetAnalyzer_beamId2_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_beamId2_HiForest.obj", &int_akPu3PFJetAnalyzer_beamId2_HiForest_obj, &b_int_akPu3PFJetAnalyzer_beamId2_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_bin_HiForest.present", &int_akPu3PFJetAnalyzer_bin_HiForest_present, &b_int_akPu3PFJetAnalyzer_bin_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_bin_HiForest.obj", &int_akPu3PFJetAnalyzer_bin_HiForest_obj, &b_int_akPu3PFJetAnalyzer_bin_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_evt_HiForest.present", &int_akPu3PFJetAnalyzer_evt_HiForest_present, &b_int_akPu3PFJetAnalyzer_evt_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_evt_HiForest.obj", &int_akPu3PFJetAnalyzer_evt_HiForest_obj, &b_int_akPu3PFJetAnalyzer_evt_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_lumi_HiForest.present", &int_akPu3PFJetAnalyzer_lumi_HiForest_present, &b_int_akPu3PFJetAnalyzer_lumi_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_lumi_HiForest.obj", &int_akPu3PFJetAnalyzer_lumi_HiForest_obj, &b_int_akPu3PFJetAnalyzer_lumi_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nHLTBit_HiForest.present", &int_akPu3PFJetAnalyzer_nHLTBit_HiForest_present, &b_int_akPu3PFJetAnalyzer_nHLTBit_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nHLTBit_HiForest.obj", &int_akPu3PFJetAnalyzer_nHLTBit_HiForest_obj, &b_int_akPu3PFJetAnalyzer_nHLTBit_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nIP_HiForest.present", &int_akPu3PFJetAnalyzer_nIP_HiForest_present, &b_int_akPu3PFJetAnalyzer_nIP_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nIP_HiForest.obj", &int_akPu3PFJetAnalyzer_nIP_HiForest_obj, &b_int_akPu3PFJetAnalyzer_nIP_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nL1ABit_HiForest.present", &int_akPu3PFJetAnalyzer_nL1ABit_HiForest_present, &b_int_akPu3PFJetAnalyzer_nL1ABit_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nL1ABit_HiForest.obj", &int_akPu3PFJetAnalyzer_nL1ABit_HiForest_obj, &b_int_akPu3PFJetAnalyzer_nL1ABit_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nL1TBit_HiForest.present", &int_akPu3PFJetAnalyzer_nL1TBit_HiForest_present, &b_int_akPu3PFJetAnalyzer_nL1TBit_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nL1TBit_HiForest.obj", &int_akPu3PFJetAnalyzer_nL1TBit_HiForest_obj, &b_int_akPu3PFJetAnalyzer_nL1TBit_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_ngen_HiForest.present", &int_akPu3PFJetAnalyzer_ngen_HiForest_present, &b_int_akPu3PFJetAnalyzer_ngen_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_ngen_HiForest.obj", &int_akPu3PFJetAnalyzer_ngen_HiForest_obj, &b_int_akPu3PFJetAnalyzer_ngen_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nref_HiForest.present", &int_akPu3PFJetAnalyzer_nref_HiForest_present, &b_int_akPu3PFJetAnalyzer_nref_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_nref_HiForest.obj", &int_akPu3PFJetAnalyzer_nref_HiForest_obj, &b_int_akPu3PFJetAnalyzer_nref_HiForest_obj);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_run_HiForest.present", &int_akPu3PFJetAnalyzer_run_HiForest_present, &b_int_akPu3PFJetAnalyzer_run_HiForest_present);
   fChain->SetBranchAddress("int_akPu3PFJetAnalyzer_run_HiForest.obj", &int_akPu3PFJetAnalyzer_run_HiForest_obj, &b_int_akPu3PFJetAnalyzer_run_HiForest_obj);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_hltBit_HiForest.present", &bools_akPu3PFJetAnalyzer_hltBit_HiForest_present, &b_bools_akPu3PFJetAnalyzer_hltBit_HiForest_present);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_hltBit_HiForest.obj", &bools_akPu3PFJetAnalyzer_hltBit_HiForest_obj, &b_bools_akPu3PFJetAnalyzer_hltBit_HiForest_obj);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest.present", &bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_present, &b_bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_present);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest.obj", &bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_obj, &b_bools_akPu3PFJetAnalyzer_ipIsHitL1_HiForest_obj);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_l1ABit_HiForest.present", &bools_akPu3PFJetAnalyzer_l1ABit_HiForest_present, &b_bools_akPu3PFJetAnalyzer_l1ABit_HiForest_present);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_l1ABit_HiForest.obj", &bools_akPu3PFJetAnalyzer_l1ABit_HiForest_obj, &b_bools_akPu3PFJetAnalyzer_l1ABit_HiForest_obj);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_l1TBit_HiForest.present", &bools_akPu3PFJetAnalyzer_l1TBit_HiForest_present, &b_bools_akPu3PFJetAnalyzer_l1TBit_HiForest_present);
   fChain->SetBranchAddress("bools_akPu3PFJetAnalyzer_l1TBit_HiForest.obj", &bools_akPu3PFJetAnalyzer_l1TBit_HiForest_obj, &b_bools_akPu3PFJetAnalyzer_l1TBit_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_apprHPD_HiForest.present", &floats_akPu3PFJetAnalyzer_apprHPD_HiForest_present, &b_floats_akPu3PFJetAnalyzer_apprHPD_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_apprHPD_HiForest.obj", &floats_akPu3PFJetAnalyzer_apprHPD_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_apprHPD_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_apprRBX_HiForest.present", &floats_akPu3PFJetAnalyzer_apprRBX_HiForest_present, &b_floats_akPu3PFJetAnalyzer_apprRBX_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_apprRBX_HiForest.obj", &floats_akPu3PFJetAnalyzer_apprRBX_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_apprRBX_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bEta_HiForest.present", &floats_akPu3PFJetAnalyzer_bEta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bEta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bEta_HiForest.obj", &floats_akPu3PFJetAnalyzer_bEta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bEta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bPhi_HiForest.present", &floats_akPu3PFJetAnalyzer_bPhi_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bPhi_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bPhi_HiForest.obj", &floats_akPu3PFJetAnalyzer_bPhi_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bPhi_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bPt_HiForest.present", &floats_akPu3PFJetAnalyzer_bPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_bPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVx_HiForest.present", &floats_akPu3PFJetAnalyzer_bVx_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bVx_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVx_HiForest.obj", &floats_akPu3PFJetAnalyzer_bVx_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bVx_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVy_HiForest.present", &floats_akPu3PFJetAnalyzer_bVy_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bVy_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVy_HiForest.obj", &floats_akPu3PFJetAnalyzer_bVy_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bVy_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVz_HiForest.present", &floats_akPu3PFJetAnalyzer_bVz_HiForest_present, &b_floats_akPu3PFJetAnalyzer_bVz_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_bVz_HiForest.obj", &floats_akPu3PFJetAnalyzer_bVz_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_bVz_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest.present", &floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_chargedHardSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedMax_HiForest.present", &floats_akPu3PFJetAnalyzer_chargedMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_chargedMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_chargedMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_chargedMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedSum_HiForest.present", &floats_akPu3PFJetAnalyzer_chargedSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_chargedSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_chargedSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_chargedSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_chargedSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest.present", &floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrcsvMva_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest.present", &floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrcsvSimple_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrfr01_HiForest.present", &floats_akPu3PFJetAnalyzer_discrfr01_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrfr01_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrfr01_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrfr01_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrfr01_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest.present", &floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrmuByIp3_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest.present", &floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrmuByPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrprob_HiForest.present", &floats_akPu3PFJetAnalyzer_discrprob_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrprob_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrprob_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrprob_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrprob_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrprobb_HiForest.present", &floats_akPu3PFJetAnalyzer_discrprobb_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrprobb_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrprobb_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrprobb_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrprobb_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest.present", &floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrssvHighEff_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest.present", &floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrssvHighPur_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest.present", &floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrtcHighEff_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest.present", &floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_present, &b_floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest.obj", &floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_discrtcHighPur_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_eMax_HiForest.present", &floats_akPu3PFJetAnalyzer_eMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_eMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_eMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_eMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_eMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_eSum_HiForest.present", &floats_akPu3PFJetAnalyzer_eSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_eSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_eSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_eSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_eSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ecalSum_HiForest.present", &floats_akPu3PFJetAnalyzer_ecalSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ecalSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ecalSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_ecalSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ecalSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fEB_HiForest.present", &floats_akPu3PFJetAnalyzer_fEB_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fEB_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fEB_HiForest.obj", &floats_akPu3PFJetAnalyzer_fEB_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fEB_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fEE_HiForest.present", &floats_akPu3PFJetAnalyzer_fEE_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fEE_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fEE_HiForest.obj", &floats_akPu3PFJetAnalyzer_fEE_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fEE_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHB_HiForest.present", &floats_akPu3PFJetAnalyzer_fHB_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fHB_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHB_HiForest.obj", &floats_akPu3PFJetAnalyzer_fHB_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fHB_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHE_HiForest.present", &floats_akPu3PFJetAnalyzer_fHE_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fHE_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHE_HiForest.obj", &floats_akPu3PFJetAnalyzer_fHE_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fHE_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHFOOT_HiForest.present", &floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHFOOT_HiForest.obj", &floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fHFOOT_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHO_HiForest.present", &floats_akPu3PFJetAnalyzer_fHO_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fHO_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHO_HiForest.obj", &floats_akPu3PFJetAnalyzer_fHO_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fHO_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHPD_HiForest.present", &floats_akPu3PFJetAnalyzer_fHPD_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fHPD_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fHPD_HiForest.obj", &floats_akPu3PFJetAnalyzer_fHPD_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fHPD_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fLS_HiForest.present", &floats_akPu3PFJetAnalyzer_fLS_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fLS_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fLS_HiForest.obj", &floats_akPu3PFJetAnalyzer_fLS_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fLS_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fLong_HiForest.present", &floats_akPu3PFJetAnalyzer_fLong_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fLong_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fLong_HiForest.obj", &floats_akPu3PFJetAnalyzer_fLong_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fLong_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fRBX_HiForest.present", &floats_akPu3PFJetAnalyzer_fRBX_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fRBX_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fRBX_HiForest.obj", &floats_akPu3PFJetAnalyzer_fRBX_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fRBX_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fShort_HiForest.present", &floats_akPu3PFJetAnalyzer_fShort_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fShort_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fShort_HiForest.obj", &floats_akPu3PFJetAnalyzer_fShort_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fShort_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet1_HiForest.present", &floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet1_HiForest.obj", &floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fSubDet1_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet2_HiForest.present", &floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet2_HiForest.obj", &floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fSubDet2_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet3_HiForest.present", &floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet3_HiForest.obj", &floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fSubDet3_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet4_HiForest.present", &floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_present, &b_floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_fSubDet4_HiForest.obj", &floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_fSubDet4_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genChargedSum_HiForest.present", &floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genChargedSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_genChargedSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genHardSum_HiForest.present", &floats_akPu3PFJetAnalyzer_genHardSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_genHardSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genHardSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_genHardSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_genHardSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_gendphijt_HiForest.present", &floats_akPu3PFJetAnalyzer_gendphijt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_gendphijt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_gendphijt_HiForest.obj", &floats_akPu3PFJetAnalyzer_gendphijt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_gendphijt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_gendrjt_HiForest.present", &floats_akPu3PFJetAnalyzer_gendrjt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_gendrjt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_gendrjt_HiForest.obj", &floats_akPu3PFJetAnalyzer_gendrjt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_gendrjt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_geneta_HiForest.present", &floats_akPu3PFJetAnalyzer_geneta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_geneta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_geneta_HiForest.obj", &floats_akPu3PFJetAnalyzer_geneta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_geneta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genphi_HiForest.present", &floats_akPu3PFJetAnalyzer_genphi_HiForest_present, &b_floats_akPu3PFJetAnalyzer_genphi_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genphi_HiForest.obj", &floats_akPu3PFJetAnalyzer_genphi_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_genphi_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genpt_HiForest.present", &floats_akPu3PFJetAnalyzer_genpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_genpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_genpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_genpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_genpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_geny_HiForest.present", &floats_akPu3PFJetAnalyzer_geny_HiForest_present, &b_floats_akPu3PFJetAnalyzer_geny_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_geny_HiForest.obj", &floats_akPu3PFJetAnalyzer_geny_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_geny_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_hcalSum_HiForest.present", &floats_akPu3PFJetAnalyzer_hcalSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_hcalSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_hcalSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_hcalSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_hcalSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip2d_HiForest.present", &floats_akPu3PFJetAnalyzer_ip2d_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ip2d_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip2d_HiForest.obj", &floats_akPu3PFJetAnalyzer_ip2d_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ip2d_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip2dSig_HiForest.present", &floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip2dSig_HiForest.obj", &floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ip2dSig_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip3d_HiForest.present", &floats_akPu3PFJetAnalyzer_ip3d_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ip3d_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip3d_HiForest.obj", &floats_akPu3PFJetAnalyzer_ip3d_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ip3d_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip3dSig_HiForest.present", &floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ip3dSig_HiForest.obj", &floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ip3dSig_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipChi2_HiForest.present", &floats_akPu3PFJetAnalyzer_ipChi2_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipChi2_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipChi2_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipChi2_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipChi2_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest.present", &floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipClosest2Jet_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest.present", &floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipDist2Jet_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest.present", &floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipDist2JetSig_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDxy_HiForest.present", &floats_akPu3PFJetAnalyzer_ipDxy_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipDxy_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDxy_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipDxy_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipDxy_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDz_HiForest.present", &floats_akPu3PFJetAnalyzer_ipDz_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipDz_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipDz_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipDz_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipDz_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipEta_HiForest.present", &floats_akPu3PFJetAnalyzer_ipEta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipEta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipEta_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipEta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipEta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipProb0_HiForest.present", &floats_akPu3PFJetAnalyzer_ipProb0_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipProb0_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipProb0_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipProb0_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipProb0_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipProb1_HiForest.present", &floats_akPu3PFJetAnalyzer_ipProb1_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipProb1_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipProb1_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipProb1_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipProb1_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipPt_HiForest.present", &floats_akPu3PFJetAnalyzer_ipPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ipPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ipPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_ipPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ipPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jteta_HiForest.present", &floats_akPu3PFJetAnalyzer_jteta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jteta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jteta_HiForest.obj", &floats_akPu3PFJetAnalyzer_jteta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jteta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtm_HiForest.present", &floats_akPu3PFJetAnalyzer_jtm_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jtm_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtm_HiForest.obj", &floats_akPu3PFJetAnalyzer_jtm_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jtm_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtphi_HiForest.present", &floats_akPu3PFJetAnalyzer_jtphi_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jtphi_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtphi_HiForest.obj", &floats_akPu3PFJetAnalyzer_jtphi_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jtphi_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtpt_HiForest.present", &floats_akPu3PFJetAnalyzer_jtpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jtpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_jtpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jtpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtpu_HiForest.present", &floats_akPu3PFJetAnalyzer_jtpu_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jtpu_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jtpu_HiForest.obj", &floats_akPu3PFJetAnalyzer_jtpu_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jtpu_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jty_HiForest.present", &floats_akPu3PFJetAnalyzer_jty_HiForest_present, &b_floats_akPu3PFJetAnalyzer_jty_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_jty_HiForest.obj", &floats_akPu3PFJetAnalyzer_jty_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_jty_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedPt_HiForest.present", &floats_akPu3PFJetAnalyzer_matchedPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_matchedPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_matchedPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_matchedPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedPu_HiForest.present", &floats_akPu3PFJetAnalyzer_matchedPu_HiForest_present, &b_floats_akPu3PFJetAnalyzer_matchedPu_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedPu_HiForest.obj", &floats_akPu3PFJetAnalyzer_matchedPu_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_matchedPu_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedR_HiForest.present", &floats_akPu3PFJetAnalyzer_matchedR_HiForest_present, &b_floats_akPu3PFJetAnalyzer_matchedR_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedR_HiForest.obj", &floats_akPu3PFJetAnalyzer_matchedR_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_matchedR_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest.present", &floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_matchedRawPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muMax_HiForest.present", &floats_akPu3PFJetAnalyzer_muMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_muMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_muMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_muMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muSum_HiForest.present", &floats_akPu3PFJetAnalyzer_muSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_muSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_muSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_muSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mudr_HiForest.present", &floats_akPu3PFJetAnalyzer_mudr_HiForest_present, &b_floats_akPu3PFJetAnalyzer_mudr_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mudr_HiForest.obj", &floats_akPu3PFJetAnalyzer_mudr_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_mudr_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mue_HiForest.present", &floats_akPu3PFJetAnalyzer_mue_HiForest_present, &b_floats_akPu3PFJetAnalyzer_mue_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mue_HiForest.obj", &floats_akPu3PFJetAnalyzer_mue_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_mue_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mueta_HiForest.present", &floats_akPu3PFJetAnalyzer_mueta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_mueta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mueta_HiForest.obj", &floats_akPu3PFJetAnalyzer_mueta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_mueta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muphi_HiForest.present", &floats_akPu3PFJetAnalyzer_muphi_HiForest_present, &b_floats_akPu3PFJetAnalyzer_muphi_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muphi_HiForest.obj", &floats_akPu3PFJetAnalyzer_muphi_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_muphi_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mupt_HiForest.present", &floats_akPu3PFJetAnalyzer_mupt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_mupt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_mupt_HiForest.obj", &floats_akPu3PFJetAnalyzer_mupt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_mupt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muptrel_HiForest.present", &floats_akPu3PFJetAnalyzer_muptrel_HiForest_present, &b_floats_akPu3PFJetAnalyzer_muptrel_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_muptrel_HiForest.obj", &floats_akPu3PFJetAnalyzer_muptrel_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_muptrel_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrcsvSimple_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrmuByPt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrprob_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrprobb_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrssvHighEff_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrssvHighPur_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrtcHighEff_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest.present", &floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_present, &b_floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest.obj", &floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_ndiscrtcHighPur_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_neutralMax_HiForest.present", &floats_akPu3PFJetAnalyzer_neutralMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_neutralMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_neutralMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_neutralMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_neutralMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_neutralSum_HiForest.present", &floats_akPu3PFJetAnalyzer_neutralSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_neutralSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_neutralSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_neutralSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_neutralSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest.present", &floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_present, &b_floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest.obj", &floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_pdiscrcsvSimple_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest.present", &floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_present, &b_floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest.obj", &floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_pdiscrprob_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest.present", &floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_present, &b_floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest.obj", &floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_pdiscrprobb_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonHardSum_HiForest.present", &floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonHardSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_photonHardSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonMax_HiForest.present", &floats_akPu3PFJetAnalyzer_photonMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_photonMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_photonMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_photonMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonSum_HiForest.present", &floats_akPu3PFJetAnalyzer_photonSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_photonSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_photonSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_photonSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_photonSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_rawpt_HiForest.present", &floats_akPu3PFJetAnalyzer_rawpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_rawpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_rawpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_rawpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_rawpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refdphijt_HiForest.present", &floats_akPu3PFJetAnalyzer_refdphijt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refdphijt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refdphijt_HiForest.obj", &floats_akPu3PFJetAnalyzer_refdphijt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refdphijt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refdrjt_HiForest.present", &floats_akPu3PFJetAnalyzer_refdrjt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refdrjt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refdrjt_HiForest.obj", &floats_akPu3PFJetAnalyzer_refdrjt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refdrjt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refeta_HiForest.present", &floats_akPu3PFJetAnalyzer_refeta_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refeta_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refeta_HiForest.obj", &floats_akPu3PFJetAnalyzer_refeta_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refeta_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refpartonpt_HiForest.present", &floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refpartonpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refpartonpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refphi_HiForest.present", &floats_akPu3PFJetAnalyzer_refphi_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refphi_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refphi_HiForest.obj", &floats_akPu3PFJetAnalyzer_refphi_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refphi_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refpt_HiForest.present", &floats_akPu3PFJetAnalyzer_refpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_refpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refy_HiForest.present", &floats_akPu3PFJetAnalyzer_refy_HiForest_present, &b_floats_akPu3PFJetAnalyzer_refy_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_refy_HiForest.obj", &floats_akPu3PFJetAnalyzer_refy_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_refy_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest.present", &floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_present, &b_floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest.obj", &floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_restrictedEMF_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest.present", &floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_signalChargedSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_signalHardSum_HiForest.present", &floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_signalHardSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_signalHardSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxdl_HiForest.present", &floats_akPu3PFJetAnalyzer_svtxdl_HiForest_present, &b_floats_akPu3PFJetAnalyzer_svtxdl_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxdl_HiForest.obj", &floats_akPu3PFJetAnalyzer_svtxdl_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_svtxdl_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxdls_HiForest.present", &floats_akPu3PFJetAnalyzer_svtxdls_HiForest_present, &b_floats_akPu3PFJetAnalyzer_svtxdls_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxdls_HiForest.obj", &floats_akPu3PFJetAnalyzer_svtxdls_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_svtxdls_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxm_HiForest.present", &floats_akPu3PFJetAnalyzer_svtxm_HiForest_present, &b_floats_akPu3PFJetAnalyzer_svtxm_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxm_HiForest.obj", &floats_akPu3PFJetAnalyzer_svtxm_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_svtxm_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest.present", &floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_present, &b_floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest.obj", &floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_svtxnormchi2_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxpt_HiForest.present", &floats_akPu3PFJetAnalyzer_svtxpt_HiForest_present, &b_floats_akPu3PFJetAnalyzer_svtxpt_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_svtxpt_HiForest.obj", &floats_akPu3PFJetAnalyzer_svtxpt_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_svtxpt_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackHardSum_HiForest.present", &floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackHardSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_trackHardSum_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackMax_HiForest.present", &floats_akPu3PFJetAnalyzer_trackMax_HiForest_present, &b_floats_akPu3PFJetAnalyzer_trackMax_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackMax_HiForest.obj", &floats_akPu3PFJetAnalyzer_trackMax_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_trackMax_HiForest_obj);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackSum_HiForest.present", &floats_akPu3PFJetAnalyzer_trackSum_HiForest_present, &b_floats_akPu3PFJetAnalyzer_trackSum_HiForest_present);
   fChain->SetBranchAddress("floats_akPu3PFJetAnalyzer_trackSum_HiForest.obj", &floats_akPu3PFJetAnalyzer_trackSum_HiForest_obj, &b_floats_akPu3PFJetAnalyzer_trackSum_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bChg_HiForest.present", &ints_akPu3PFJetAnalyzer_bChg_HiForest_present, &b_ints_akPu3PFJetAnalyzer_bChg_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bChg_HiForest.obj", &ints_akPu3PFJetAnalyzer_bChg_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_bChg_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bJetIndex_HiForest.present", &ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_present, &b_ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bJetIndex_HiForest.obj", &ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_bJetIndex_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bPdg_HiForest.present", &ints_akPu3PFJetAnalyzer_bPdg_HiForest_present, &b_ints_akPu3PFJetAnalyzer_bPdg_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bPdg_HiForest.obj", &ints_akPu3PFJetAnalyzer_bPdg_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_bPdg_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bStatus_HiForest.present", &ints_akPu3PFJetAnalyzer_bStatus_HiForest_present, &b_ints_akPu3PFJetAnalyzer_bStatus_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_bStatus_HiForest.obj", &ints_akPu3PFJetAnalyzer_bStatus_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_bStatus_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_chargedHardN_HiForest.present", &ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_chargedHardN_HiForest.obj", &ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_chargedHardN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_chargedN_HiForest.present", &ints_akPu3PFJetAnalyzer_chargedN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_chargedN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_chargedN_HiForest.obj", &ints_akPu3PFJetAnalyzer_chargedN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_chargedN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_eN_HiForest.present", &ints_akPu3PFJetAnalyzer_eN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_eN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_eN_HiForest.obj", &ints_akPu3PFJetAnalyzer_eN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_eN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_genmatchindex_HiForest.present", &ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_present, &b_ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_genmatchindex_HiForest.obj", &ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_genmatchindex_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_gensubid_HiForest.present", &ints_akPu3PFJetAnalyzer_gensubid_HiForest_present, &b_ints_akPu3PFJetAnalyzer_gensubid_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_gensubid_HiForest.obj", &ints_akPu3PFJetAnalyzer_gensubid_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_gensubid_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest.present", &ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_present, &b_ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest.obj", &ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_ipJetIndex_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHit_HiForest.present", &ints_akPu3PFJetAnalyzer_ipNHit_HiForest_present, &b_ints_akPu3PFJetAnalyzer_ipNHit_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHit_HiForest.obj", &ints_akPu3PFJetAnalyzer_ipNHit_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_ipNHit_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest.present", &ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_present, &b_ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest.obj", &ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_ipNHitPixel_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest.present", &ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_present, &b_ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest.obj", &ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_ipNHitStrip_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_muN_HiForest.present", &ints_akPu3PFJetAnalyzer_muN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_muN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_muN_HiForest.obj", &ints_akPu3PFJetAnalyzer_muN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_muN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_muchg_HiForest.present", &ints_akPu3PFJetAnalyzer_muchg_HiForest_present, &b_ints_akPu3PFJetAnalyzer_muchg_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_muchg_HiForest.obj", &ints_akPu3PFJetAnalyzer_muchg_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_muchg_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n2RPC_HiForest.present", &ints_akPu3PFJetAnalyzer_n2RPC_HiForest_present, &b_ints_akPu3PFJetAnalyzer_n2RPC_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n2RPC_HiForest.obj", &ints_akPu3PFJetAnalyzer_n2RPC_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_n2RPC_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n3RPC_HiForest.present", &ints_akPu3PFJetAnalyzer_n3RPC_HiForest_present, &b_ints_akPu3PFJetAnalyzer_n3RPC_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n3RPC_HiForest.obj", &ints_akPu3PFJetAnalyzer_n3RPC_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_n3RPC_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n90_HiForest.present", &ints_akPu3PFJetAnalyzer_n90_HiForest_present, &b_ints_akPu3PFJetAnalyzer_n90_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_n90_HiForest.obj", &ints_akPu3PFJetAnalyzer_n90_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_n90_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nECAL_HiForest.present", &ints_akPu3PFJetAnalyzer_nECAL_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nECAL_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nECAL_HiForest.obj", &ints_akPu3PFJetAnalyzer_nECAL_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nECAL_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nHCAL_HiForest.present", &ints_akPu3PFJetAnalyzer_nHCAL_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nHCAL_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nHCAL_HiForest.obj", &ints_akPu3PFJetAnalyzer_nHCAL_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nHCAL_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nIPtrk_HiForest.present", &ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nIPtrk_HiForest.obj", &ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nIPtrk_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nRPC_HiForest.present", &ints_akPu3PFJetAnalyzer_nRPC_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nRPC_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nRPC_HiForest.obj", &ints_akPu3PFJetAnalyzer_nRPC_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nRPC_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_neutralN_HiForest.present", &ints_akPu3PFJetAnalyzer_neutralN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_neutralN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_neutralN_HiForest.obj", &ints_akPu3PFJetAnalyzer_neutralN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_neutralN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest.present", &ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest.obj", &ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nselIPtrk_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nsvtx_HiForest.present", &ints_akPu3PFJetAnalyzer_nsvtx_HiForest_present, &b_ints_akPu3PFJetAnalyzer_nsvtx_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_nsvtx_HiForest.obj", &ints_akPu3PFJetAnalyzer_nsvtx_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_nsvtx_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_photonHardN_HiForest.present", &ints_akPu3PFJetAnalyzer_photonHardN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_photonHardN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_photonHardN_HiForest.obj", &ints_akPu3PFJetAnalyzer_photonHardN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_photonHardN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_photonN_HiForest.present", &ints_akPu3PFJetAnalyzer_photonN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_photonN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_photonN_HiForest.obj", &ints_akPu3PFJetAnalyzer_photonN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_photonN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest.present", &ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_present, &b_ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest.obj", &ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_refpartonflavor_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest.present", &ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_present, &b_ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest.obj", &ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_refpartonflavorForB_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_subid_HiForest.present", &ints_akPu3PFJetAnalyzer_subid_HiForest_present, &b_ints_akPu3PFJetAnalyzer_subid_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_subid_HiForest.obj", &ints_akPu3PFJetAnalyzer_subid_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_subid_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_svtxntrk_HiForest.present", &ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_present, &b_ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_svtxntrk_HiForest.obj", &ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_svtxntrk_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_trackHardN_HiForest.present", &ints_akPu3PFJetAnalyzer_trackHardN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_trackHardN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_trackHardN_HiForest.obj", &ints_akPu3PFJetAnalyzer_trackHardN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_trackHardN_HiForest_obj);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_trackN_HiForest.present", &ints_akPu3PFJetAnalyzer_trackN_HiForest_present, &b_ints_akPu3PFJetAnalyzer_trackN_HiForest_present);
   fChain->SetBranchAddress("ints_akPu3PFJetAnalyzer_trackN_HiForest.obj", &ints_akPu3PFJetAnalyzer_trackN_HiForest_obj, &b_ints_akPu3PFJetAnalyzer_trackN_HiForest_obj);
   Notify();
}

Bool_t EDMForest::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void EDMForest::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t EDMForest::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return entry;
}
#endif // #ifdef EDMForest_cxx
