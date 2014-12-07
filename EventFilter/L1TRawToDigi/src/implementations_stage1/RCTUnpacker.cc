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
        bool even;

        RCTInfoFactory rctInfoFactory;

        std::vector<RCTInfo> rctInfo;
        rctInfoFactory.decodeCapturedLinkID(block.header().getID(), crate, counter_, even);
        
        
        std::cout<<"block.header().getID()"<<block.header().getID()<<std::endl;

        std::vector <uint32_t> uint;
        uint.reserve(6);

        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);


        std::cout<<"uint word 0="<<std::hex<<uint[0]<<std::endl;
        std::cout<<"uint word 1="<<std::hex<<uint[1]<<std::endl;
        std::cout<<"uint word 2="<<std::hex<<uint[2]<<std::endl;
        std::cout<<"uint word 3="<<std::hex<<uint[3]<<std::endl;
        std::cout<<"uint word 4="<<std::hex<<uint[4]<<std::endl;
        std::cout<<"uint word 5="<<std::hex<<uint[5]<<std::endl;

        rctInfoFactory.produce(uint,uint,rctInfo);


        std::cout<<"--------------- crate id="<<crate<<", is even="<<even<<std::endl;

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
