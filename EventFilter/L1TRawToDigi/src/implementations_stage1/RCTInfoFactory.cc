#include <vector>
#include <iostream>
#include <iomanip>
#include <string>
#include <stdint.h>
#include <stdio.h>
#include <cstdlib>
#include <string.h>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;
#include "EventFilter/L1TRawToDigi/interface/RCTInfo.hh"

#include "EventFilter/L1TRawToDigi/interface/RCTInfoFactory.hh"

bool RCTInfoFactory::decodeCapturedLinkID(unsigned int capturedValue, unsigned int & crateNumber, unsigned int & linkNumber, bool & even)
{

  crateNumber = ( capturedValue >> 8 ) & 0xFF;
  //if crateNumber not valid set to 0xFF
  if(crateNumber > 17)
    crateNumber = 0xFF;

  linkNumber = ( capturedValue ) & 0xFF;
  //if linkNumber not valid set to 0xFF
  if(linkNumber > 12)
    linkNumber = 0xFF;

  //currently 0-5 are odd and 6-11 are even
  if(linkNumber>5)
    even=true;
  else
    even=false;

  return true;
  };

/*
 * Extract RCT Object Info from oRSC Output Fibers
 * Primarily intended for use on CTP7/MP7
 */

bool RCTInfoFactory::produce(const std::vector <unsigned int> evenFiberData, 
			     const std::vector <unsigned int> oddFiberData,
			     std::vector <RCTInfo> &rctInfoData) {

  // Ensure that there is data to process
  unsigned int nWordsToProcess = evenFiberData.size();
  unsigned int remainder = nWordsToProcess%6;
  if(nWordsToProcess != oddFiberData.size()) {
    std::cerr << "RCTInfoFactory::produce -- even and odd fiber sizes are different!" << std::endl;
    return false;
  }
  if(nWordsToProcess == 0|| nWordsToProcess/6 == 0) {
    std::cerr << "RCTInfoFactory::produce -- evenFiberData is null :(" << std::endl;
    return false;
  }
  else if((nWordsToProcess % 6) != 0) {
    //std::cerr << "RCTInfoFactory::produce -- Correct protocol expects 6x32-bit words! "<< nWordsToProcess << " Remainder of "<< nWordsToProcess % 6 << std::endl;
    nWordsToProcess=nWordsToProcess-remainder;
  }

  // Extract RCTInfo

  unsigned int nBXToProcess = nWordsToProcess / 6;

  for(unsigned int iBX = 0; iBX < nBXToProcess; iBX++) {
    RCTInfo rctInfo;
    // We extract into rctInfo the data from RCT crate
    // Bit field description can be found in the spreadsheet:
    // https://twiki.cern.ch/twiki/pub/CMS/ORSCOperations/oRSCFiberDataSpecificationV5.xlsx
    // Even fiber bits contain 4x4 region information
    rctInfo.rgnEt[0][0]  = (evenFiberData[iBX * 6 + 0] & 0x0003FF00) >>  8;
    rctInfo.rgnEt[0][1]  = (evenFiberData[iBX * 6 + 0] & 0x0FFC0000) >> 18;
    rctInfo.rgnEt[1][0]  = (evenFiberData[iBX * 6 + 0] & 0xF0000000) >> 28;
    rctInfo.rgnEt[1][0] |= (evenFiberData[iBX * 6 + 1] & 0x0000003F) <<  4;
    rctInfo.rgnEt[1][1]  = (evenFiberData[iBX * 6 + 1] & 0x0000FFC0) >>  6;
    rctInfo.rgnEt[2][0]  = (evenFiberData[iBX * 6 + 1] & 0x03FF0000) >> 16;
    rctInfo.rgnEt[2][1]  = (evenFiberData[iBX * 6 + 1] & 0xFC000000) >> 26;
    rctInfo.rgnEt[2][1] |= (evenFiberData[iBX * 6 + 2] & 0x0000000F) <<  6;
    rctInfo.rgnEt[3][0]  = (evenFiberData[iBX * 6 + 2] & 0x00003FF0) >>  4;
    rctInfo.rgnEt[3][1]  = (evenFiberData[iBX * 6 + 2] & 0x00FFC000) >> 14;
    rctInfo.rgnEt[4][0]  = (evenFiberData[iBX * 6 + 2] & 0xFF000000) >> 24;
    rctInfo.rgnEt[4][0] |= (evenFiberData[iBX * 6 + 3] & 0x00000003) <<  8;
    rctInfo.rgnEt[4][1]  = (evenFiberData[iBX * 6 + 3] & 0x00000FFC) >>  2;
    rctInfo.rgnEt[5][0]  = (evenFiberData[iBX * 6 + 3] & 0x003FF000) >> 12;
    rctInfo.rgnEt[5][1]  = (evenFiberData[iBX * 6 + 3] & 0xFFC00000) >> 22;
    rctInfo.rgnEt[6][0]  = (evenFiberData[iBX * 6 + 4] & 0x000003FF) >>  0;
    rctInfo.rgnEt[6][1]  = (evenFiberData[iBX * 6 + 4] & 0x000FFC00) >> 10;
    rctInfo.tBits  = (evenFiberData[iBX * 6 + 4] & 0xFFF00000) >> 20;
    rctInfo.tBits |= (evenFiberData[iBX * 6 + 5] & 0x00000003) << 12; 
    rctInfo.oBits  = (evenFiberData[iBX * 6 + 5] & 0x0000FFFC) >>  2;
    rctInfo.c4BC0  = (evenFiberData[iBX * 6 + 5] & 0x000C0000) >> 18;
    rctInfo.c5BC0  = (evenFiberData[iBX * 6 + 5] & 0x00300000) >> 20;
    rctInfo.c6BC0  = (evenFiberData[iBX * 6 + 5] & 0x00C00000) >> 22;
    // Odd fiber bits contain 2x1, HF and other miscellaneous information
    rctInfo.hfEt[0][0]  = (oddFiberData[iBX * 6 + 0] & 0x0000FF00) >>  8;
    rctInfo.hfEt[0][1]  = (oddFiberData[iBX * 6 + 0] & 0x00FF0000) >> 16;
    rctInfo.hfEt[1][0]  = (oddFiberData[iBX * 6 + 0] & 0xFF000000) >> 24;
    rctInfo.hfEt[1][1]  = (oddFiberData[iBX * 6 + 1] & 0x000000FF) >>  0;
    rctInfo.hfEt[0][2]  = (oddFiberData[iBX * 6 + 1] & 0x0000FF00) >>  8;
    rctInfo.hfEt[0][3]  = (oddFiberData[iBX * 6 + 1] & 0x00FF0000) >> 16;
    rctInfo.hfEt[1][2]  = (oddFiberData[iBX * 6 + 1] & 0xFF000000) >> 24;
    rctInfo.hfEt[1][3]  = (oddFiberData[iBX * 6 + 2] & 0x000000FF) >>  0;
    rctInfo.hfQBits     = (oddFiberData[iBX * 6 + 2] & 0x0000FF00) >>  8;
    rctInfo.ieRank[0]   = (oddFiberData[iBX * 6 + 2] & 0x003F0000) >> 16;
    rctInfo.ieRegn[0]   = (oddFiberData[iBX * 6 + 2] & 0x00400000) >> 22;
    rctInfo.ieCard[0]   = (oddFiberData[iBX * 6 + 2] & 0x03800000) >> 23; 
    rctInfo.ieRank[1]   = (oddFiberData[iBX * 6 + 2] & 0xFC000000) >> 26;
    rctInfo.ieRegn[1]   = (oddFiberData[iBX * 6 + 3] & 0x00000001) >>  0;
    rctInfo.ieCard[1]   = (oddFiberData[iBX * 6 + 3] & 0x0000000E) >>  1;
    rctInfo.ieRank[2]   = (oddFiberData[iBX * 6 + 3] & 0x000003F0) >>  4;
    rctInfo.ieRegn[2]   = (oddFiberData[iBX * 6 + 3] & 0x00000400) >> 10;
    rctInfo.ieCard[2]   = (oddFiberData[iBX * 6 + 3] & 0x00003800) >> 11;
    rctInfo.ieRank[3]   = (oddFiberData[iBX * 6 + 3] & 0x000FC000) >> 14;
    rctInfo.ieRegn[3]   = (oddFiberData[iBX * 6 + 3] & 0x00100000) >> 20;
    rctInfo.ieCard[3]   = (oddFiberData[iBX * 6 + 3] & 0x00E00000) >> 21;
    rctInfo.neRank[0]   = (oddFiberData[iBX * 6 + 3] & 0x3F000000) >> 24; 
    rctInfo.neRegn[0]   = (oddFiberData[iBX * 6 + 3] & 0x40000000) >> 30;
    rctInfo.neCard[0]   = (oddFiberData[iBX * 6 + 3] & 0x80000000) >> 31; 
    rctInfo.neCard[0]  |= (oddFiberData[iBX * 6 + 4] & 0x00000003) <<  1; 
    rctInfo.neRank[1]   = (oddFiberData[iBX * 6 + 4] & 0x000000FC) >>  2;
    rctInfo.neRegn[1]   = (oddFiberData[iBX * 6 + 4] & 0x00000100) >>  8;
    rctInfo.neCard[1]   = (oddFiberData[iBX * 6 + 4] & 0x00000E00) >>  9;
    rctInfo.neRank[2]   = (oddFiberData[iBX * 6 + 4] & 0x0003F000) >> 12;
    rctInfo.neRegn[2]   = (oddFiberData[iBX * 6 + 4] & 0x00040000) >> 18;
    rctInfo.neCard[2]   = (oddFiberData[iBX * 6 + 4] & 0x00380000) >> 19;
    rctInfo.neRank[3]   = (oddFiberData[iBX * 6 + 4] & 0x0FC00000) >> 22;
    rctInfo.neRegn[3]   = (oddFiberData[iBX * 6 + 4] & 0x10000000) >> 28;
    rctInfo.neCard[3]   = (oddFiberData[iBX * 6 + 4] & 0xE0000000) >> 29;
    rctInfo.mBits       = (oddFiberData[iBX * 6 + 5] & 0x00003FFF) >>  0;
    rctInfo.c1BC0       = (oddFiberData[iBX * 6 + 5] & 0x00030000) >> 16;
    rctInfo.c2BC0       = (oddFiberData[iBX * 6 + 5] & 0x000C0000) >> 18;
    rctInfo.c3BC0       = (oddFiberData[iBX * 6 + 5] & 0x00300000) >> 20;
    unsigned int oddFiberc4BC0 = (oddFiberData[iBX * 6 + 5] & 0x00C00000) >> 22;
    if(oddFiberc4BC0 != rctInfo.c4BC0) {
      std::cerr << "Even and odd fibers do not agree on cable 4 BC0 mark :(" << std::endl;
    }

    //Adding in extra function to make comparison of the region tau and overflow bits easier
    for(int i = 0; i < 7; i++) 
      for(int j = 0; j < 2; j++) 
	rctInfo.rgnEtTenBit[i][j] = GetRegTenBits(rctInfo, i, j);

    for(int j = 0; j <4; j++){
      rctInfo.ieTenBit[j] = GetElectronTenBits( rctInfo.ieCard[j] , rctInfo.ieRegn[j] , rctInfo.ieRank[j] );
      rctInfo.neTenBit[j] = GetElectronTenBits( rctInfo.neCard[j] , rctInfo.neRegn[j] , rctInfo.neRank[j] );
    }

    rctInfoData.push_back(rctInfo);
  }
  return true;

}

unsigned int RCTInfoFactory::GetElectronTenBits(unsigned int Card, unsigned int Region, unsigned int Rank)
{
/* 
 * Function to return the 10 bits from electron ET
 * 3 bits Card   1 bit Region   6 bits Rank
 * Combine them and return an unsigned int
 */
  unsigned int ElectronBits;

  ElectronBits  = Card<<1;
  ElectronBits |= Region;
  ElectronBits = ElectronBits<<6;
  ElectronBits |= Rank;

  return ElectronBits;
}

unsigned int RCTInfoFactory::GetRegTenBits(RCTInfo rctInfo, unsigned int j, unsigned int k)
{

  /*
   * Shift bit to get correct tauBit/overflowBit 
   * RC       6     5     4     3     2     1     0
   * Region   1  0  1  0  1  0  1  0  1  0  1  0  1  0
   * Bit #   13 12 11 10  9  8  7  6  5  4  3  2  1  0
   * The tau bit and obit go in the 9th and 8th (respectively) place of the Region Bits
   */

  unsigned int bit=j*2+k; 
  unsigned int tbit=(((rctInfo.tBits>>bit)&0x1)<<1);
  unsigned int obit=((rctInfo.oBits>>bit)&0x1);
  unsigned int RegTenBits=(tbit|obit)<<10;

  RegTenBits |= rctInfo.rgnEt[j][k];

  return RegTenBits;
}

