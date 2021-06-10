#include "niederreiter_keygen.h"

#include "H_Q_matrices_generation.h"
#include "gf2x_arith_mod_xPplusOne.h"
#include "randombytes.h"

#include <string.h>
/*----------------------------------------------------------------------------*/
/* Implementation that should never be optimized out by the compiler */
static inline void zeroize( void *v, size_t n )
{
   volatile unsigned char *p = v;
   while( n-- ) *p++ = 0;
} // end zeroize

/*----------------------------------------------------------------------------*/

void OQS_NAMESPACE_key_gen_niederreiter(publicKeyNiederreiter_t  *const pk,
                                        privateKeyNiederreiter_t *const sk)
{
   unsigned char prng_seed[TRNG_BYTE_LENGTH];
   AES_XOF_struct niederreiter_keys_expander;
   memset(&niederreiter_keys_expander, 0x00, sizeof(AES_XOF_struct));

   randombytes(sk->LongTermSeed, TRNG_BYTE_LENGTH);

   randombytes(prng_seed, TRNG_BYTE_LENGTH);
   OQS_NAMESPACE_seedexpander_from_trng(&niederreiter_keys_expander, prng_seed);

   OQS_NAMESPACE_generateHPosOnes(sk->HPosOnes, &niederreiter_keys_expander);

   DIGIT Ln0dense[NUM_DIGITS_GF2X_ELEMENT] = {0x00};
   gf2x_mod_densify_VT(Ln0dense,sk->HPosOnes[N0-1],V);

   DIGIT Ln0Inv[NUM_DIGITS_GF2X_ELEMENT] = {0x00};
   GF2X_DIGIT_MOD_INVERSE(Ln0Inv, Ln0dense);

   for (int i = 0; i < N0-1; i++) {
      OQS_NAMESPACE_gf2x_mod_mul_dense_to_sparse(pk->Mtr+i*NUM_DIGITS_GF2X_ELEMENT,
                                   Ln0Inv,
                                   sk->HPosOnes[i],
                                   V);
   }
   for (int i = 0; i < N0-1; i++) {
      OQS_NAMESPACE_gf2x_transpose_in_place(pk->Mtr+i*NUM_DIGITS_GF2X_ELEMENT);
   }

   OQS_NAMESPACE_transposeHPosOnes(sk->HtrPosOnes, (const POSITION_T(*)[V])sk->HPosOnes);
} // end key_gen_niederreiter

/*----------------------------------------------------------------------------*/

void OQS_NAMESPACE_publicKey_deletion_niederreiter(publicKeyNiederreiter_t   *const pk)
{

   zeroize(pk,sizeof(publicKeyNiederreiter_t));
} // publicKey_deletion_niederreiter

/*----------------------------------------------------------------------------*/

void OQS_NAMESPACE_privateKey_deletion_niederreiter(privateKeyNiederreiter_t *const sk)
{
   zeroize(sk, sizeof(privateKeyNiederreiter_t));
} // privateKey_deletion_niederreiter

/*----------------------------------------------------------------------------*/
