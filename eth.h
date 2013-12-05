// Copyright (c) 2013 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.

#ifndef EOS_ETH_H
#define EOS_ETH_H

#include <stddef.h>
#include <eos/types.h>

#include <Arnet/EthAddr.h> //= eos_internal

namespace eos {

class eth_addr_t {
 public:
   // Default constructor
   eth_addr_t();
   // Construct an address from one of three string forms:
   // xx:xx:xx:xx:xx:xx, xx-xx-xx-xx-xx-xx, or xxxx.xxxx.xxxx
   explicit eth_addr_t(char const *name);
   eth_addr_t(const Arnet::EthAddr &); //= eos_internal

   void to_string(char *namebuf, size_t namebuf_size);

   bool operator !() const;
   bool operator==(eth_addr_t const & other);
   bool operator!=(eth_addr_t const & other);
   Arnet::EthAddr ethAddr_; //= hide

 //=> private:
   //=> uint32_t words_[3];

};

};


#endif // EOS_ETH_H
