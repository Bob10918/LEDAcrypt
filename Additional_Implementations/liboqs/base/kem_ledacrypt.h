// SPDX-License-Identifier: MIT

#ifndef OQS_KEM_LEDACRYPT_H
#define OQS_KEM_LEDACRYPT_H

#include <oqs/oqs.h>

#ifdef OQS_ENABLE_KEM_ledacrypt_23371
#define OQS_KEM_ledacrypt_23371_length_public_key 2928
#define OQS_KEM_ledacrypt_23371_length_secret_key 50
#define OQS_KEM_ledacrypt_23371_length_ciphertext 2952
#define OQS_KEM_ledacrypt_23371_length_shared_secret 32
OQS_KEM *OQS_KEM_ledacrypt_23371_new(void);
OQS_API OQS_STATUS OQS_KEM_ledacrypt_23371_keypair(uint8_t *public_key, uint8_t *secret_key);
OQS_API OQS_STATUS OQS_KEM_ledacrypt_23371_encaps(uint8_t *ciphertext, uint8_t *shared_secret, const uint8_t *public_key);
OQS_API OQS_STATUS OQS_KEM_ledacrypt_23371_decaps(uint8_t *shared_secret, const unsigned char *ciphertext, const uint8_t *secret_key);
#endif


#endif // OQS_KEM_LEDACRYPT_H