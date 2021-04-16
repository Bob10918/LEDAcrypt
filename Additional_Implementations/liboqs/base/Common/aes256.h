#ifndef OQS_NAMESPACE_AES256_H
#define OQS_NAMESPACE_AES256_H

#define NROUNDS 14
#define KEYLEN_b 256

#include <stdint.h>

int OQS_NAMESPACE_rijndaelKeySetupEnc(uint32_t *rk, const uint8_t *cipherKey);
void OQS_NAMESPACE_rijndaelEncrypt(const uint32_t *rk, int Nr,
                                                  const uint8_t *pt, uint8_t *ct);

#endif