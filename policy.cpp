// Copyright (c) 2014 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.

#include "eos/policy.h"

namespace eos {

policy_map_mgr::policy_map_mgr() {
}

policy_map_mgr::~policy_map_mgr() {
}

policy_map_action_t::~policy_map_action_t() {
}

policy_map_handler::policy_map_handler(policy_map_mgr * mgr) : base_handler(mgr) {
}

void
policy_map_handler::on_policy_map_sync_fail(policy_map_key_t const & key,
                                            std::string const & message) {
   // TODO: no op impl.
}

void
policy_map_handler::on_policy_map_sync(policy_map_key_t const & key) {
   // TODO: no op impl.
}

}
