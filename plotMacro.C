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

void plotMacro()
{
  TString filenames[3] = {
    "Pyquen_EmEnrichedDijet_PtHat30_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_numEvent1000.root",
    "Pyquen_EmEnrichedDijet_PtHat80_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_numEvent1000.root",
    "Pyquen_EmEnrichedDijet_PtHat170_PartonPt0_ParticlePt60_eta30_TuneZ2_Unquenched_2760GeV_numEvent1000.root"
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

  TString labels[9] = {"PtHat30","PtHat30_frag", "PtHat30_bkg",
		       "PtHat80","PtHat80_frag", "PtHat80_bkg",
		       "PtHat170","PtHat170_frag", "PtHat170_bkg"};

  TH1D *hists[3][3];
  //TCut idcuts[3] = {"", "momId<22", "momId>22"};
  const Double_t maxEt = 300;
  const Int_t nBins = 100;

  for(int i = 0; i < 3; ++i)
  {
    for(int j = 0; j < 3; ++j)
    {
      hists[i][j] = new TH1D(labels[i*3+j],";((photon || pi0 || eta) && status == 1) leading et (GeV);Count",nBins,0,maxEt);
    }

    for(int entry = 0; entry < trees[i]->GetEntries(); ++entry)
    {
      //find leading photons
      trees[i]->GetEntry(entry);

      double maxet = -1;
      int index = -1;
      for(int photon = 0; photon < gens[i]->nPar; photon++)
      {
	if(gens[i]->status[photon] != 1) continue;
	Int_t id = gens[i]->id[photon];
	//if( notMeson(id) ) continue;
	if(! isPhotonPiEta(id) ) continue;
	//if(id != 22) continue;
	if(TMath::Abs(gens[i]->eta[photon]) > 3) continue;
	if (gens[i]->et[photon] > maxet)
	{
	  maxet = gens[i]->et[photon];
	  index = photon;
	}
      }

      if(index > -1)
      {
	hists[i][0]->Fill(maxet);
	if(TMath::Abs(gens[i]->momId[index]) < 22){
	  hists[i][1]->Fill(maxet);
	} else if (TMath::Abs(gens[i]->momId[index]) > 22) {
	  hists[i][2]->Fill(maxet);
	}
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
  TString savename[3] = {"pthat30_ParticlePt60.pdf", "pthat80_ParticlePt60.pdf", "pthat170_ParticlePt60.pdf"};
  Int_t colors[3] = {1, kBlue, kRed};
  for(int i = 0; i < 3; ++i)
  {
    c[i] = new TCanvas();
    leg[i] = new TLegend(0.6,0.6,0.8,0.8);
    leg[i]->SetFillColor(0);
    leg[i]->SetTextFont(43);
    leg[i]->SetTextSize(20);
    for(int j = 0; j < 3; j++)
    {
      hists[i][j]->SetLineColor(colors[j]);
      if(j==0)
	hists[i][j]->Draw();
      else
	hists[i][j]->Draw("same");

      leg[i]->AddEntry(hists[i][j],hists[i][j]->GetName(),"l");
    }
    c[i]->SetLogy();
    leg[i]->Draw();

    c[i]->SaveAs(savename[i]);

    //files[i]->Close();
    //delete gens[i];
  }
}

//221, -221, 331, -331, 223,-223, 211, -211, 111, 311,11, -11

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

bool isPhotonPiEta(Int_t id){
  if(id != 22)
    if(id != 111)
      if(id != 221)
	return false;

  return true;
}

int main()
{
  plotMacro();
  return 0;
}
