#ifndef RCTInfoFactory_hh
#define RCTInfoFactory_hh

#include "EventFilter/L1TRawToDigi/interface/RCTInfo.hh"
#include <iostream>
#include <fstream>
#include <vector>

class RCTInfo;

class RCTInfoFactory {

public:

  RCTInfoFactory() {;}
  ~RCTInfoFactory() {;}

  bool decodeCapturedLinkID(unsigned int capturedValue, unsigned int & crateNumber, unsigned int & linkNumber, bool & even);

  bool produce(const std::vector <unsigned int> evenFiberData, 
	       const std::vector <unsigned int> oddFiberData,
	       std::vector <RCTInfo> &rctInfo);

  //Two Helper Functions
  unsigned int GetRegTenBits(RCTInfo rctInfo, unsigned int j, unsigned int k);
  unsigned int GetElectronTenBits(unsigned int Card, unsigned int Region, unsigned int Rank);

private:

  // No copy constructor is needed
  RCTInfoFactory(const RCTInfoFactory&);

  // No equality operator is needed
  const RCTInfoFactory& operator=(const RCTInfoFactory&);

};

#endif
