#ifndef OQS_NAMESPACE_API_H
#define OQS_NAMESPACE_API_H

#include <stddef.h>
#include <stdint.h>


#define OQS_NAMESPACE_CRYPTO_ALGNAME "LEDAcrypt"

/* required bytes of input randomness */
#define  OQS_NAMESPACE_CRYPTO_RANDOMBYTES GENERATOR_CRYPTO_RANDOMBYTES      //TRNG_BYTE_LENGTH

/* size in bytes of the secret key */
#define  OQS_NAMESPACE_CRYPTO_SECRETKEYBYTES GENERATOR_CRYPTO_SECRETKEYBYTES     //(TRNG_BYTE_LENGTH*2)+2

/* size in bytes of the public key */
#define  OQS_NAMESPACE_CRYPTO_PUBLICKEYBYTES GENERATOR_CRYPTO_PUBLICKEYBYTES    // DIGIT Mtr[(N0-1)*[(P+DIGIT_b-1)/DIGIT_b]]

/* size in bytes of the shared secret */
#define  OQS_NAMESPACE_CRYPTO_BYTES GENERATOR_CRYPTO_BYTES        //HASH_BYTE_LENGTH

/*size in bytes of the ciphertext*/
#define  OQS_NAMESPACE_CRYPTO_CIPHERTEXTBYTES GENERATOR_CRYPTO_CIPHERTEXTBYTES


/* Generates a keypair - pk is the public key and sk is the secret key. */
int OQS_NAMESPACE_crypto_kem_keypair(uint8_t *pk,
                                     uint8_t *sk );

/* Encrypt - pk is the public key, ct is a key encapsulation message
  (ciphertext), ss is the shared secret.*/
int OQS_NAMESPACE_crypto_kem_enc(uint8_t *ct,
                                 uint8_t *ss,
                                 const uint8_t *pk );


/* Decrypt - ct is a key encapsulation message (ciphertext), sk is the private
   key, ss is the shared secret */

int OQS_NAMESPACE_crypto_kem_dec(uint8_t *ss,
                                 const uint8_t *ct,
                                 const uint8_t *sk );

#endif