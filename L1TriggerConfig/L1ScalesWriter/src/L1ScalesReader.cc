#include "L1TriggerConfig/L1ScalesWriter/interface/L1ScalesReader.h"
#include <iomanip>
#include <iostream>

#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "CondFormats/DataRecord/interface/L1RCTParametersRcd.h"
#include "CondFormats/L1TObjects/interface/L1RCTParameters.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CondCore/CondDB/interface/Session.h"

#include <iostream>
using namespace std;

void L1ScalesReader::analyze(const edm::Event& iEvent, const edm::EventSetup& evSetup){

    edm::ESHandle<L1RCTParameters> handle1;
    evSetup.get<L1RCTParametersRcd>().get( handle1 ) ;
    boost::shared_ptr<L1RCTParameters> ptr1(new L1RCTParameters(*(handle1.product ())));

    cout<<"L1RCTParameters: "<<endl;
    cout<<"  eGammaECalScaleFactors(): "<<ptr1->eGammaECalScaleFactors().size()<<endl;
    for(unsigned int i=0; i<ptr1->eGammaECalScaleFactors().size(); i++){
        cout<<"   "<<ptr1->eGammaECalScaleFactors()[i]<<", "<<endl;
    }

    cout<<"  eGammaHCalScaleFactors(): "<<ptr1->eGammaHCalScaleFactors().size()<<endl;
    for(unsigned int i=0; i<ptr1->eGammaHCalScaleFactors().size(); i++){
        cout<<"   "<<ptr1->eGammaHCalScaleFactors()[i]<<", "<<endl;
    }

}

