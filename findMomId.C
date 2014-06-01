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

void findMomId()
{
  TString filenames[3] = {
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt0_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt15_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root",
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_cfi_numEvent1000.root"
  };

  TFile *files[3];
  TTree *trees[3];
  genpana *gens[3];
  for(int i = 0; i < 3; ++i)
  {
    files[i] = TFile::Open(filenames[i]);
    trees[i] = (TTree*)files[i]->Get("genpana/photon");
    gens[i] = new genpana(trees[i]);
  }

  TString labels[3*7] = {"Pt0_pi","Pt0_eta", "Pt0_eta1", "Pt0_omega","Pt0_cpi","Pt0_e","Pt0_K",
			"Pt15_pi","Pt15_eta", "Pt15_eta1", "Pt15_omega","Pt15_cpi","Pt15_e","Pt15_K",
			"Pt60_pi","Pt60_eta", "Pt60_eta1", "Pt60_omega","Pt60_cpi","Pt60_e","Pt60_K"};

  TH1D *hists[3][7];
  //TCut idcuts[3] = {"", "momId<22", "momId>22"};
  const Double_t maxEt = 200;
  const Int_t nBins = 50;

  for(int i = 0; i < 3; ++i) //file
  {
    for(int j = 0; j < 7; ++j) //particle
    {
      hists[i][j] = new TH1D(labels[i*7+j],";leading particle et;Count",nBins,0,maxEt);
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
	if( notInConfig(id) ) continue;
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

  TCanvas *c[3];
  TLegend *leg[3];
  TString savename[3] = {"pthat30_momId.pdf", "pthat80_momId.pdf", "pthat170_momId.pdf"};
  Int_t colors[7] = {1, kBlue, kRed, 40, 41, 42, 43};
  for(int i = 0; i < 3; ++i)
  {
    c[i] = new TCanvas();
    leg[i] = new TLegend(0.6,0.6,0.8,0.8);
    leg[i]->SetFillColor(0);
    leg[i]->SetTextFont(43);
    leg[i]->SetTextSize(20);
    for(int j = 0; j < 7; j++)
    {
      hists[i][j]->SetLineColor(colors[j]);
      if(j==0){
	hists[i][j]->SetMaximum(200);
	hists[i][j]->Draw();
      }else{
	hists[i][j]->Add(hists[i][j-1]);
	hists[i][j]->Draw("same");
      }

      leg[i]->AddEntry(hists[i][j],hists[i][j]->GetName(),"l");
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
  findMomId();
  return 0;
}
