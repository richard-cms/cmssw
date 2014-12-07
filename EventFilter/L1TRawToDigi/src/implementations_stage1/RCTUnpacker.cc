#include "FWCore/Framework/interface/MakerMacros.h"
#include "EventFilter/L1TRawToDigi/interface/Unpacker.h"
#include "EventFilter/L1TRawToDigi/interface/RCTInfo.hh"
#include "EventFilter/L1TRawToDigi/interface/RCTInfoFactory.hh"

#include "DataFormats/L1CaloTrigger/interface/L1CaloEmCand.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegion.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegionDetId.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"


#include <iostream>
#include <fstream>

#include "CaloCollections.h"

namespace l1t {
  namespace stage1 {
    class RCTUnpacker : public Unpacker {
      public:
        virtual bool unpack(const Block& block, UnpackerCollections *coll) override;
      private:
        unsigned int counter_ = 0;
    };
  }
}

// Implementation

namespace l1t {
  namespace stage1 {
    bool RCTUnpacker::unpack(const Block& block, UnpackerCollections *coll){

      int nBX = int(ceil(block.header().getSize() / 6.)); 

      // Find the first and last BXs
      int firstBX = -(ceil((double)nBX/2.)-1);
      int lastBX;
      if (nBX % 2 == 0) {
        lastBX = ceil((double)nBX/2.)+1;
      } else {
        lastBX = ceil((double)nBX/2.);
      }

      // Initialise index
      int unsigned i = 0;

      for (int bx=firstBX; bx<lastBX; bx++){

        unsigned int crate;
        bool even=0;

        RCTInfoFactory rctInfoFactory;
        std::vector<RCTInfo> rctInfo;
        std::vector <uint32_t> uint;
        uint.reserve(6);
        
        int mp7link=(int)(block.header().getID()/2);
        int indexfromMP7tooRSC[36]={0,1,18,19,16,17,34,35,2,3,20,21,14,15,32,33,4,5,22,23,12,13,30,31,6,7,24,25,10,11,28,29,8,9,26,27};

        int oRSClink=indexfromMP7tooRSC[mp7link];
        crate=(int)(oRSClink/2);
        if (oRSClink%2==0) even=true;
        else even=false;


        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);


        //std::cout<<"uint word 0="<<std::hex<<uint[0]<<std::endl;
        //std::cout<<"uint word 1="<<std::hex<<uint[1]<<std::endl;
        //std::cout<<"uint word 2="<<std::hex<<uint[2]<<std::endl;
        //std::cout<<"uint word 3="<<std::hex<<uint[3]<<std::endl;
        //std::cout<<"uint word 4="<<std::hex<<uint[4]<<std::endl;
        //std::cout<<"uint word 5="<<std::hex<<uint[5]<<std::endl;

        rctInfoFactory.produce(uint,uint,rctInfo);
        
        std::cout<<"mp7link"<<mp7link<<std::endl;
        std::cout<<"--------------- mp7 link ="<<mp7link<<"RCT crate id="<<crate<<", RCT crate even="<<even<<std::endl;

        if(!even) {

          for(int j = 0; j < 4; j++) {

            std::cout <<"index="<<j<<", neRank="<<rctInfo.at(0).neRank[j]<<", neRegn="<<rctInfo.at(0).neRegn[j]<<", neCard="<<rctInfo.at(0).neCard[j]<<std::endl;
            std::cout <<"index="<<j<<", ieRank="<<rctInfo.at(0).ieRank[j]<<", neRegn="<<rctInfo.at(0).ieRegn[j]<<", neCard="<<rctInfo.at(0).ieCard[j]<<std::endl;

          }
          for(int j = 0; j < 2; j++) {
            for(int k = 0; k < 4; k++) {
              std::cout <<"region HF ="<<j<<", card="<<k<<", rgnEt="<<rctInfo.at(0).hfEt[j][k]<<std::endl;
            }
          }
        }// end if odd

        else{
          for(int j = 0; j < 7; j++) {
            for(int k = 0; k < 2; k++) {
              std::cout <<"region="<<j<<", card="<<k<<", rgnEt="<<rctInfo.at(0).rgnEt[j][k]<<std::endl;
            }
          }
        }// end if even
      }// end of loop over BX
      return true;
    }
  }
}

DEFINE_L1T_UNPACKER(l1t::stage1::RCTUnpacker);
