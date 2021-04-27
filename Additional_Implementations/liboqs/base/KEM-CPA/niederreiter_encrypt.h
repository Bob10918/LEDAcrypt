#pragma once

#include "niederreiter.h"
#include "gf2x_limbs.h"

void OQS_NAMESPACE_encrypt_niederreiter_indcpa(unsigned char *const ct,  /* ciphertext - output    */
                                               unsigned char *const tag, /* tag for message confirmation - output */
                                               unsigned char *const ss,  /* shared secret - output */
                                               const publicKeyNiederreiter_t *const pk);
