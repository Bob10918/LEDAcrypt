#ifndef NIEDERREITER_KEYGEN_H
#define NIEDERREITER_KEYGEN_H

#include "niederreiter.h"
#include "rng.h"

void OQS_NAMESPACE_key_gen_niederreiter(publicKeyNiederreiter_t   *const pk,
                                                       privateKeyNiederreiter_t *const sk);

void OQS_NAMESPACE_publicKey_deletion_niederreiter(publicKeyNiederreiter_t    *const pk);
void OQS_NAMESPACE_privateKey_deletion_niederreiter(privateKeyNiederreiter_t *const sk);

#endif