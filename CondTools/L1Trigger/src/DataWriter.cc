#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "CondTools/L1Trigger/interface/DataWriter.h"

#include "CondTools/L1Trigger/interface/Exception.h"
#include "CondCore/MetaDataService/interface/MetaData.h"
#include "CondCore/IOVService/interface/IOVProxy.h"
#include "CondCore/DBCommon/interface/Exception.h"

#include "CondCore/CondDB/interface/Serialization.h"

#include <utility>
#include <iostream>
using namespace std;

namespace l1t
{
  DataWriter::DataWriter(){}
  DataWriter::~DataWriter(){}



std::string
DataWriter::writePayload( const edm::EventSetup& setup,
			  const std::string& recordType )
{
  cout << "calling writePayload, was passed recordType" << recordType << "\n";

  WriterFactory* factory = WriterFactory::get();
  std::auto_ptr<WriterProxy> writer(factory->create( recordType + "@Writer" )) ;
  if( writer.get() == 0 )
    {
      throw cond::Exception( "DataWriter: could not create WriterProxy with name "
			     + recordType + "@Writer" ) ;
    }

  edm::Service<cond::service::PoolDBOutputService> poolDb;
  if (!poolDb.isAvailable())
    {
      throw cond::Exception( "DataWriter: PoolDBOutputService not available."
			     ) ;
    }

  // 2010-02-16: Move session and transaction to WriterProxy::save().  Otherwise, if another transaction is
  // started while WriterProxy::save() is called (e.g. in a ESProducer like L1ConfigOnlineProdBase), the
  // transaction here will become read-only.
//   cond::DbSession session = poolDb->session();
  
  cond::persistency::TransactionScope tr(poolDb->session().transaction());
//   // if throw transaction will unroll
//   tr.start(false);

  cout << "calling writer->save( setup )...\n";

  // update key to have new payload registered for record-type pair.
  //  std::string payloadToken = writer->save( setup, session ) ;
  std::string payloadToken = writer->save( setup ) ;

  cout << recordType << " PAYLOAD TOKEN "
       << payloadToken << "\n";
  cout << "exiting writePayload" << "\n";
  tr.close();

  return payloadToken ;
}

void
DataWriter::writeKeyList( L1TriggerKeyList* keyList,
			  edm::RunNumber_t sinceRun,
			  bool logTransactions )
{
  edm::Service<cond::service::PoolDBOutputService> poolDb;
  if( !poolDb.isAvailable() )
    {
      throw cond::Exception( "DataWriter: PoolDBOutputService not available."
			     ) ;
    }

  cout << "about to call 1.\n";

  cond::persistency::Session session = poolDb->session();
  cond::persistency::TransactionScope tr(session.transaction());
  //tr.start( false );


  cout << "about to call 2.\n";
  
  // Write L1TriggerKeyList payload and save payload token before committing
  boost::shared_ptr<L1TriggerKeyList> pointer(keyList);
  std::string payloadToken = session.storePayload(*pointer );

			
  // Commit before calling updateIOV(), otherwise PoolDBOutputService gets
  // confused.
  //tr.commit ();
  tr.close ();

  cout << "about to call 3 \n";
  
  // Set L1TriggerKeyList IOV
  updateIOV( "L1TriggerKeyListRcd",
	     payloadToken,
	     sinceRun,
	     logTransactions ) ;

  cout << "about to call 3 \n";
}

bool
DataWriter::updateIOV( const std::string& esRecordName,
		       const std::string& payloadToken,
		       edm::RunNumber_t sinceRun,
		       bool logTransactions )
{
  cout << " CALLING updateIOV... 1\n";

  cout << esRecordName << " PAYLOAD TOKEN " << payloadToken ;
			       

  edm::Service<cond::service::PoolDBOutputService> poolDb;
  if (!poolDb.isAvailable())
    {
      throw cond::Exception( "DataWriter: PoolDBOutputService not available."
			     ) ;
    }

  bool iovUpdated = true ;

  if( poolDb->isNewTagRequest( esRecordName ) )
    {
      sinceRun = poolDb->beginOfTime() ;
      poolDb->createNewIOV( payloadToken,
			    sinceRun,
			    poolDb->endOfTime(),
			    esRecordName,
			    logTransactions ) ;
    }
  else
    {	
      cond::TagInfo tagInfo ;
      poolDb->tagInfo( esRecordName, tagInfo ) ;

      if( sinceRun == 0 ) // find last since and add 1
	{
	  sinceRun = tagInfo.lastInterval.first ;
	  ++sinceRun ;
	}

      if( tagInfo.lastPayloadToken != payloadToken )
	{
	  poolDb->appendSinceTime( payloadToken,
				   sinceRun,
				   esRecordName,
				   logTransactions ) ;
	}
      else
	{
	  iovUpdated = false ;
	  cout << "IOV already up to date." ;
	}
    }

  if( iovUpdated )
    {
      cout << esRecordName << " "
				   << poolDb->tag( esRecordName )
				   << " SINCE " << sinceRun ;
    }

  return iovUpdated ;
}

std::string
DataWriter::payloadToken( const std::string& recordName,
			  edm::RunNumber_t runNumber )
{
  cout << " CALLING payloadToken... 1\n";

  edm::Service<cond::service::PoolDBOutputService> poolDb;
  if( !poolDb.isAvailable() )
    {
      throw cond::Exception( "DataWriter: PoolDBOutputService not available."
			     ) ;
    }

  // Get tag corresponding to EventSetup record name.
  std::string iovTag = poolDb->tag( recordName ) ;

  // Get IOV token for tag.
  cond::persistency::Session session = poolDb->session();
  cond::persistency::IOVProxy iov = session.readIov( iovTag );
  session.transaction().start();

  std::string payloadToken("");
  auto iP = iov.find( runNumber );
  if( iP != iov.end() ){
    payloadToken = (*iP).payloadId; 
  }
  session.transaction().commit() ;
  return payloadToken ;
}

std::string
DataWriter::lastPayloadToken( const std::string& recordName )
{
  cout << " CALLING lastPayloadToken... 1\n";
  edm::Service<cond::service::PoolDBOutputService> poolDb;
  if( !poolDb.isAvailable() )
    {
      throw cond::Exception( "DataWriter: PoolDBOutputService not available."
			     ) ;
    }

  cond::TagInfo tagInfo ;
  poolDb->tagInfo( recordName, tagInfo ) ;
  return tagInfo.lastPayloadToken ;
}

bool
DataWriter::fillLastTriggerKeyList( L1TriggerKeyList& output )
{
  cout << " CALLING fillLastPayloadToken... 1\n";

  std::string keyListToken =
    lastPayloadToken( "L1TriggerKeyListRcd" ) ;
  if( keyListToken.empty() )
    {
      cout << "EMPTY!!!" << "\n";
      return false ;
    }
  else
    {
      cout << "NOT EMPTY!!!\n";
      cout << "Calling readObject!!!\n";
      readObject( keyListToken, output ) ;
      return true ;
    }
}

} // ns
