#include <iostream>
#include "CondTools/L1TriggerExt/interface/L1ObjectKeysOnlineProdBaseExt.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

class L1TCaloStage1ObjectKeysOnlineProdHI : public L1ObjectKeysOnlineProdBaseExt {
public:
    virtual void fillObjectKeys( ReturnType pL1TriggerKey ) override ;

    L1TCaloStage1ObjectKeysOnlineProdHI(const edm::ParameterSet&);
    ~L1TCaloStage1ObjectKeysOnlineProdHI(void){}
};

L1TCaloStage1ObjectKeysOnlineProdHI::L1TCaloStage1ObjectKeysOnlineProdHI(const edm::ParameterSet& iConfig)
  : L1ObjectKeysOnlineProdBaseExt( iConfig ){}


void L1TCaloStage1ObjectKeysOnlineProdHI::fillObjectKeys( ReturnType pL1TriggerKey ){

    std::string s1calol2Key = pL1TriggerKey->subsystemKey( L1TriggerKeyExt::kS1CALOL2 ) ;

    std::string stage1CaloSchema = "CMS_S1CALOL2" ;

    if( !s1calol2Key.empty() ) {
        std::string mp7_hi_conf_key, hi_algo_regs_key;

        // select MP7_HI_CONF_KEY from CMS_S1CALOL2.S1CALOL2_CONF where S1CALOL2_CONF_KEY = objectKey ;
        l1t::OMDSReader::QueryResults mp7_hi_conf_key_result =
            m_omdsReader.basicQuery( "MP7_HI_CONF_KEY",
                                     stage1CaloSchema,
                                     "S1CALOL2_CONF",
                                     "S1CALOL2_CONF.S1CALOL2_CONF_KEY",
                                     m_omdsReader.singleAttribute(s1calol2Key)
                                   ) ;

        if( mp7_hi_conf_key_result.queryFailed() || mp7_hi_conf_key_result.numberRows() != 1 ){
            edm::LogError( "L1-O2O" ) << "Cannot get MP7_HI_CONF_KEY" ;
            return ;
        }

        if( !mp7_hi_conf_key_result.fillVariable( "MP7_HI_CONF_KEY", mp7_hi_conf_key) ) mp7_hi_conf_key = "";


        pL1TriggerKey->add( "L1TCaloStage1ParamsRcd",
//                            "l1t::CaloParams",
                            "CaloParams",
			    mp7_hi_conf_key ) ;

    }
}


//define this as a plug-in
DEFINE_FWK_EVENTSETUP_MODULE(L1TCaloStage1ObjectKeysOnlineProdHI);
