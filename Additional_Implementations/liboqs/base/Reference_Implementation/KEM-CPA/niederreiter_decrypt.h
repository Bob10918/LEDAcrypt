#pragma once

#include "niederreiter.h"
#include "gf2x_limbs.h"

/*----------------------------------------------------------------------------*/

int OQS_NAMESPACE_decrypt_niederreiter_indcpa(unsigned char *const ss,                   /* output */
                                              const unsigned char *const ct,             /* input */
                                              const unsigned char *const tag,            /* input */
                                              const privateKeyNiederreiter_t *const sk);  /* input */
// return 1 always -- due to the IND-CCA2 construction employed also in this IND-CPA primitive

/*----------------------------------------------------------------------------*/
