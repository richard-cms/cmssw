#include "FWCore/Framework/interface/MakerMacros.h"
#include "EventFilter/L1TRawToDigi/interface/Unpacker.h"

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

        std::vector <uint32_t> uint;
        uint.reserve(6);

        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        uint.push_back(block.payload()[i++]);
        
        std::cout<<"uint word 0"<<uint[0]<<std::endl;
        std::cout<<"uint word 1"<<uint[1]<<std::endl;
        std::cout<<"uint word 2"<<uint[2]<<std::endl;
        std::cout<<"uint word 3"<<uint[3]<<std::endl;
        std::cout<<"uint word 4"<<uint[4]<<std::endl;
        std::cout<<"uint word 5"<<uint[5]<<std::endl;

      }
        return true;

    }
  }
}

DEFINE_L1T_UNPACKER(l1t::stage1::RCTUnpacker);
