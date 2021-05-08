#include "niederreiter_keygen.h"
#include "niederreiter_encrypt.h"
#include "niederreiter_decrypt.h"
#include "rng.h"
#include "fips202.h"
#include <string.h>

/*----------------------------------------------------------------------------*/
/* Generates a keypair - pk is the public key and
 *                       sk is the secret key.
 */
int OQS_NAMESPACE_crypto_kem_keypair( unsigned char *pk,
                                      unsigned char *sk )
{

    OQS_NAMESPACE_key_gen_niederreiter((publicKeyNiederreiter_t *) pk,
                                       (privateKeyNiederreiter_t *) sk);
   return 0;
} // end crypto_kem_keypair

/*----------------------------------------------------------------------------*/
/* Encrypt - pk is the public key,
 *           ct is a key encapsulation message (ciphertext),
 *           ss is the shared secret.
 */
int OQS_NAMESPACE_crypto_kem_enc( unsigned char *ct,
                                  unsigned char *ss,
                                  const unsigned char *pk )
{

    OQS_NAMESPACE_encrypt_niederreiter_indcpa((unsigned char *const) ct,
                                               (unsigned char *const) (ct+NUM_DIGITS_GF2X_ELEMENT*DIGIT_SIZE_B),
                                               (unsigned char *const) ss,
                                               (const publicKeyNiederreiter_t *const) pk);

   return 0; // NIST convention: 0 == no encryption failure
} // end crypto_kem_enc

/*----------------------------------------------------------------------------*/
/* Decrypt - ct is a key encapsulation message (ciphertext),
 *           sk is the private key,
 *           ss is the shared secret
 */
int OQS_NAMESPACE_crypto_kem_dec( unsigned char *ss,
                                  const unsigned char *ct,
                                  const unsigned char *sk )
{
   int decryption_ok;
   decryption_ok = (1 == OQS_NAMESPACE_decrypt_niederreiter_indcpa((unsigned char *const) ss,
                                                                   (const unsigned char *const) ct,
                                                                   (const unsigned char *const) (ct+NUM_DIGITS_GF2X_ELEMENT*DIGIT_SIZE_B),
                                                                   (const privateKeyNiederreiter_t *const) sk));
   if (decryption_ok == 1) {
      return 0; // NIST convention: 0 == no decryption failure
   } else
      return -1; // NIST convention: -1 == decryption failure
} // end crypto_kem_dec
