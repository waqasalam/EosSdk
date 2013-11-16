// Copyright (c) 2013 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.

<<= TacModule("Agent::CAgent");
<<= TacModule("EthIntf::EthIntf");
<<= TacModule("Sysdb::EntityManager");

// Fwd.h contains forward declarations for non-TACC types.
<<= CppInlineInclude("Fwd.h");

EosSdk : Tac::Namespace {

SDK : extern Tac::Type {
   `allowsIndirectRef;
}

Handlers : extern Tac::Type {
   `allowsIndirectRef;
}

IntfHandler : extern Tac::Type {
   `allowsIndirectRef;
}

EthPhyIntfHandler : extern Tac::Type {
   `allowsIndirectRef;
}

EthIntfConfigSm : Tac::Type(handler, intfId, ethIntfConfig) : Tac::Constrainer {
   tacFwkActivity = 0;
   handler : IntfHandler::RawPtr;
   intfId : Arnet::IntfId;
   ethIntfConfig : in Interface::EthIntfConfig::PtrConst;

   handleDescription : extern invasive void();
   ethIntfConfig::description => handleDescription();
   handleAdminEnabled : extern invasive void();
   ethIntfConfig::adminEnabledStateLocal => handleAdminEnabled();
   handleAdminDisabledReason : extern invasive void();
   ethIntfConfig::enabledStateReason => handleAdminDisabledReason();
}

EthIntfStatusSm : Tac::Type(handler, intfId, ethIntfStatus) : Tac::Constrainer {
   tacFwkActivity = 0;
   handler : IntfHandler::RawPtr;
   intfId : Arnet::IntfId;
   ethIntfStatus : in Interface::EthIntfStatus::PtrConst;
   // TBD
}

EthPhyIntfConfigSm : Tac::Type(handler, intfId,
                               ethPhyIntfConfig) : Tac::Constrainer {
   tacFwkActivity = 0;
   handler : EthPhyIntfHandler::RawPtr;
   intfId : Arnet::IntfId;
   ethPhyIntfConfig : in Interface::EthPhyIntfConfig::PtrConst;
   // TBD
}

EthPhyIntfStatusSm : Tac::Type(handler, intfId
                               ethPhyIntfStatus) : Tac::Constrainer {
   tacFwkActivity = 0;
   handler : EthPhyIntfHandler::RawPtr;
   intfId : Arnet::IntfId;
   ethPhyIntfStatus : in Interface::EthPhyIntfStatus::PtrConst;
   // TBD
}

SdkSm : Tac::Type(sdk,
                  name,
                  handlers,
                  ethIntfConfigDir,
                  ethIntfStatusDir,
                  ethPhyIntfConfigDir,
                  ethPhyIntfStatusDir) : Tac::Constrainer {
   tacFwkActivity = 0;

   sdk : SDK::RawPtr;
   name : Tac::Name;
   handlers : Handlers::RawPtr;

   ethIntfConfigDir : in Interface::EthIntfConfigDir::PtrConst;
   handleEthIntfConfigDir : extern invasive void(intfId : Arnet::IntfId);
   ethIntfConfigDir::intfConfig[intfId] => handleEthIntfConfigDir(intfId);
   ethIntfConfigSm : EthIntfConfigSm[intfId];

   ethIntfStatusDir : in Interface::EthIntfStatusDir::PtrConst;
   handleEthIntfStatusDir : extern invasive void(intfId : Arnet::IntfId);
   ethIntfStatusDir::intfStatus[intfId] => handleEthIntfStatusDir(intfId);
   ethIntfStatusSm : EthIntfConfigSm[intfId];

   ethPhyIntfConfigDir : in Interface::EthPhyIntfConfigDir::PtrConst;
   handleEthPhyIntfConfigDir : extern invasive void(intfId : Arnet::IntfId);
   ethPhyIntfConfigDir::intfConfig[intfId] => handleEthPhyIntfConfigDir(intfId);
   ethPhyIntfConfigSm : EthIntfConfigSm[intfId];

   ethPhyIntfStatusDir : in Interface::EthPhyIntfStatusDir::PtrConst;
   handleEthPhyIntfStatusDir : extern invasive void(intfId : Arnet::IntfId);
   ethPhyIntfStatusDir::intfStatus[intfId] => handleEthPhyIntfStatusDir(intfId);
   ethPhyIntfStatusSm : EthIntfConfigSm[intfId];
}

Agent : Tac::Type( name ) : AgentBase::CAgent {
   `allowsNotifiee=false;
   `hasFactoryFunction;
   `allowsDirInstantiation;

   ethIntfConfigDir : Interface::EthIntfConfigDir::PtrConst;
   ethIntfStatusDir : Interface::EthIntfStatusDir::PtrConst;
   ethPhyIntfConfigDir : Interface::EthPhyIntfConfigDir::PtrConst;
   ethPhyIntfStatusDir : Interface::EthPhyIntfStatusDir::PtrConst;

   sdk : SDK::RawPtr;
   sdkSm : SdkSm[name];

   doInit : extern invasive overriding void();
   doMountsComplete : extern invasive overriding void(
         mountStatus : Sysdb::MountStatus,
         em : Sysdb::EntityManager::Ptr);
}

}  // namespace EosSdk

<<= CppBlock("EosSdkAgent.tin");
