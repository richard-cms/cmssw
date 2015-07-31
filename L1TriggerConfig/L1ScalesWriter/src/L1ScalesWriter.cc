#include "L1TriggerConfig/L1ScalesWriter/interface/L1ScalesWriter.h"
#include <iomanip>
#include <iostream>

#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "CondFormats/DataRecord/interface/L1GctJetFinderParamsRcd.h"
#include "CondFormats/L1TObjects/interface/L1GctJetFinderParams.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"

void L1ScalesWriter::analyze(const edm::Event& iEvent, const edm::EventSetup& evSetup){

    edm::ESHandle<L1GctJetFinderParams> handle1;
    evSetup.get<L1GctJetFinderParamsRcd>().get( handle1 ) ;
    boost::shared_ptr<L1GctJetFinderParams> ptr1(new L1GctJetFinderParams(*(handle1.product ())));

    edm::Service<cond::service::PoolDBOutputService> poolDb;
    if( poolDb.isAvailable() ){
        cond::Time_t firstSinceTime = poolDb->beginOfTime();
        poolDb->writeOne(ptr1.get(),firstSinceTime,"L1GctJetFinderParamsRcd");
    }

}
