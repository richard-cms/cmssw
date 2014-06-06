#include <TFile.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TH1D.h>
#include <TLegend.h>
#include <TMath.h>

class genpana{
public:
  Int_t nPar;
  Float_t et[1500];
  Float_t eta[1500];
  Int_t id[1500];
  Int_t momId[1500];
  Int_t status[1500];

  genpana(TTree *tree)
  {
    initTree(tree);
  }

private:
  void initTree(TTree *tree){
    tree->SetBranchAddress("nPar",&nPar);
    tree->SetBranchAddress("et",et);
    tree->SetBranchAddress("eta",eta);
    tree->SetBranchAddress("id",id);
    tree->SetBranchAddress("momId",momId);
    tree->SetBranchAddress("status",status);
  }
};

bool notMeson(Int_t id);
bool isPhotonPiEta(Int_t id);
int getHisto(int id);
bool notInConfig(Int_t id);
bool notInConfig2(Int_t id);

void stackPlotConfigParticles()
{
  const int nFILES = 2;
  TString filenames[nFILES] = {
    //"Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt0_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt35_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat80_PartonPt0_ParticlePt0_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat80_PartonPt0_ParticlePt35_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat80_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt0_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt35_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    //"Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root"
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt35_eta30_TuneZ2_Unquenched_2760GeV_cfi_2_numEvent1000.root"
  };

  TFile *files[nFILES];
  TTree *trees[nFILES];
  genpana *gens[nFILES];
  for(int i = 0; i < nFILES; ++i)
  {
    files[i] = TFile::Open(filenames[i]);
    trees[i] = (TTree*)files[i]->Get("genpana/photon");
    gens[i] = new genpana(trees[i]);
  }

  const int nPART = 7;
  TString labels[nFILES*nPART] = {
    //"30_0_pi","30_0_eta", "30_0_eta1", "30_0_omega","30_0_cpi","30_0_e","30_0_K",
    //"30_35_pi","30_35_eta", "30_35_eta1", "30_35_omega","30_35_cpi","30_35_e","30_35_K",
    //"30_60_pi","30_60_eta", "30_60_eta1", "30_60_omega","30_60_cpi","30_60_e","30_60_K",
    //"80_0_pi","80_0_eta", "80_0_eta1", "80_0_omega","80_0_cpi","80_0_e","80_0_K",
    //"80_35_pi","80_35_eta", "80_35_eta1", "80_35_omega","80_35_cpi","80_35_e","80_35_K",
    //"80_60_pi","80_60_eta", "80_60_eta1", "80_60_omega","80_60_cpi","80_60_e","80_60_K",
    //"170_0_pi","170_0_eta", "170_0_eta1", "170_0_omega","170_0_cpi","170_0_e","170_0_K",
    "170_35_pi","170_35_eta", "170_35_eta1", "170_35_omega","170_35_cpi","170_35_e","170_35_K",
    "170_60_pi","170_60_eta", "170_60_eta1", "170_60_omega","170_60_cpi","170_60_e","170_60_K"
  };

  TH1D *hists[nFILES][nPART];
  const Double_t maxEt = 200;
  const Int_t nBins = 50;

  for(int i = 0; i < nFILES; ++i)
  {
    for(int j = 0; j < nPART; ++j)
    {
      hists[i][j] = new TH1D(labels[i*nPART+j],";leading particle from config et;Count",nBins,0,maxEt);
    }

    for(int entry = 0; entry < trees[i]->GetEntries(); ++entry)
    {
      //find leading photons
      trees[i]->GetEntry(entry);

      double maxet = -1;
      int index = -1;
      int id = -999;
      for(int photon = 0; photon < gens[i]->nPar; photon++)
      {
	//if(gens[i]->status[photon] != 1) continue;
	id = gens[i]->id[photon];
	if( notInConfig2(id) ) continue;
	//if(id != ids[j]) continue;
	//if(id != 22) continue;
	//if(TMath::Abs(gens[i]->eta[photon]) > 3) continue;
	if (gens[i]->et[photon] > maxet)
	{
	  maxet = gens[i]->et[photon];
	  index = photon;
	}
      }

      if(index > -1)
      {
	//hists[i][j]->Fill(gens[i]->momId[index]);
	int j = getHisto(gens[i]->id[index]);
	if(j != -1)
	  hists[i][j]->Fill(maxet);
	else
	  printf("unexpected id: %d\n",gens[i]->id[index]);
	//hists[i][0]->Fill(gens[i]->eta[index]);
	// if(TMath::Abs(gens[i]->momId[index]) < 22){
	//   hists[i][1]->Fill(maxet);
	// } else if (TMath::Abs(gens[i]->momId[index]) > 22) {
	//   hists[i][2]->Fill(maxet);
	// }
	// hists[i][0]->Fill(gens[i]->eta[index]);
	// if(gens[i]->momId[index] < 22){
	//   hists[i][1]->Fill(gens[i]->eta[index]);
	// } else if (gens[i]->momId[index] > 22) {
	//   hists[i][2]->Fill(gens[i]->eta[index]);
	// }
      }
    }
  }

  TCanvas *c[nFILES];
  TLegend *leg[nFILES];
  //TString savename[nFILES] = {"pthat30_momId.pdf", "pthat80_momId.pdf", "pthat170_momId.pdf"};
  Int_t colors[nPART] = {1, 2, 3, 4, 90, 8, 9};
  for(int i = 0; i < nFILES; ++i)
  {
    c[i] = new TCanvas();
    leg[i] = new TLegend(0.6,0.4,0.8,0.8);
    leg[i]->SetFillColor(0);
    leg[i]->SetTextFont(43);
    leg[i]->SetTextSize(20);
    // for(int j = 0; j < nPART; j++)
    // {
    //   hists[i][j]->SetLineColor(colors[j]);
    //   if(j==0){
    // 	hists[i][j]->SetMaximum(200);
    // 	hists[i][j]->Draw();
    //   }else{
    // 	hists[i][j]->Add(hists[i][j-1]);
    // 	hists[i][j]->Draw("same");
    //   }

    //   leg[i]->AddEntry(hists[i][j],hists[i][j]->GetName(),"l");
    // }

    //add histos for stackplot
    for(int j = 0; j<nPART; j++)
    {
      if(j!=0)
	hists[i][j]->Add(hists[i][j-1]);
      leg[i]->AddEntry(hists[i][j],hists[i][j]->GetName(),"f");
    }

    hists[i][0]->SetMaximum(hists[i][nPART-1]->GetMaximum()*1.5);
    hists[i][0]->Draw();

    for(int j = nPART-1; j >= 0; j--)
    {
      hists[i][j]->SetLineColor(colors[j]);
      hists[i][j]->SetFillStyle(1001);
      hists[i][j]->SetFillColor(colors[j]);
      hists[i][j]->Draw("same");
    }

    //c[i]->SetLogy();
    leg[i]->Draw();

    //c[i]->SaveAs(savename[i]);

    //files[i]->Close();
    //delete gens[i];
  }
}

bool notMeson(Int_t id){
  if(id != 221)
    if(id != -221)
      if(id != 331)
	if(id != -331)
	  if(id != 223)
	    if(id != -223)
	      if(id != 211)
		if(id != -211)
		  if(id != 111)
		    if(id != 311)
		      if(id != 11)
			if(id != -11)
			  if(id != 22)
			    return true;

  return false;
}

bool notInConfig(Int_t id){
  if(id != 221)
    if(id != 331)
      if(id != 223)
	if(id != 211)
	  if(id != -211)
	    if(id != 111)
	      if(id != 311)
		if(id != 11)
		  if(id != -11)
		    return true;
  return false;
}

bool notInConfig2(Int_t id){
  if(id != 221)
    if(id != 331)
      if(id != 223)
	if(id != 111)
	  return true;
  return false;
}


int getHisto(int id){
  if(id == 111)
    return 0;
  if(id == 221)
    return 1;
  if(id == 331)
    return 2;
  if(id == 223)
    return 3;
  if(id == 211 || id==-211)
    return 4;
  if(id == 11 || id == -11)
    return 5;
  if(id == 311)
    return 6;
  return -1;
}

bool isPhotonPiEta(Int_t id){
  if(id != 22)
    if(id != 111)
      if(id != 211)
	return false;

  return true;
}

int main()
{
  stackPlotConfigParticles();
  return 0;
}
