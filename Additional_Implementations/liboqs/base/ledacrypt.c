// SPDX-License-Identifier: MIT

#include <stdlib.h>

#include <oqs/kem_ledacrypt.h>

#ifdef OQS_ENABLE_KEM_GENERATOR_SCHEME_NAME

OQS_KEM *OQS_KEM_GENERATOR_SCHEME_NAME_new() {

	OQS_KEM *kem = malloc(sizeof(OQS_KEM));
	if (kem == NULL) {
		return NULL;
	}
	kem->method_name = OQS_KEM_alg_GENERATOR_SCHEME_NAME;
	kem->alg_version = "https://github.com/Bob10918/LEDAcrypt/commit/b176d7c6821700f5124f591b50ccae9d5f25ee91";

	kem->claimed_nist_level = GENERATOR_NIST_LEVEL;
	kem->ind_cca = GENERATOR_IND_CCA;

	kem->length_public_key = OQS_KEM_GENERATOR_SCHEME_NAME_length_public_key;
	kem->length_secret_key = OQS_KEM_GENERATOR_SCHEME_NAME_length_secret_key;
	kem->length_ciphertext = OQS_KEM_GENERATOR_SCHEME_NAME_length_ciphertext;
	kem->length_shared_secret = OQS_KEM_GENERATOR_SCHEME_NAME_length_shared_secret;

	kem->keypair = OQS_KEM_GENERATOR_SCHEME_NAME_keypair;
	kem->encaps = OQS_KEM_GENERATOR_SCHEME_NAME_encaps;
	kem->decaps = OQS_KEM_GENERATOR_SCHEME_NAME_decaps;

	return kem;
}


extern int OQS_NAMESPACE_crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
extern int OQS_NAMESPACE_crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
extern int OQS_NAMESPACE_crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);

#if defined(OQS_ENABLE_KEM_GENERATOR_SCHEME_NAME_avx2)
extern int OQS_AVX_NAMESPACE_crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
extern int OQS_AVX_NAMESPACE_crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
extern int OQS_AVX_NAMESPACE_crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);
#endif


OQS_API OQS_STATUS OQS_KEM_GENERATOR_SCHEME_NAME_keypair(uint8_t *public_key, uint8_t *secret_key) {
#if defined(OQS_ENABLE_KEM_GENERATOR_SCHEME_NAME_avx2)
#if defined(OQS_DIST_BUILD)
	if (OQS_CPU_has_extension(OQS_CPU_EXT_AVX2)) {
#endif /* OQS_DIST_BUILD */
		return (OQS_STATUS) OQS_AVX_NAMESPACE_crypto_kem_keypair(public_key, secret_key);
#if defined(OQS_DIST_BUILD)
	} else {
		return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_keypair(public_key, secret_key);
	}
#endif /* OQS_DIST_BUILD */
#else
	return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_keypair(public_key, secret_key);
#endif
}

OQS_API OQS_STATUS OQS_KEM_GENERATOR_SCHEME_NAME_encaps(uint8_t *ciphertext, uint8_t *shared_secret, const uint8_t *public_key) {
#if defined(OQS_ENABLE_KEM_GENERATOR_SCHEME_NAME_avx2)
#if defined(OQS_DIST_BUILD)
	if (OQS_CPU_has_extension(OQS_CPU_EXT_AVX2)) {
#endif /* OQS_DIST_BUILD */
		return (OQS_STATUS) OQS_AVX_NAMESPACE_crypto_kem_enc(ciphertext, shared_secret, public_key);
#if defined(OQS_DIST_BUILD)
	} else {
		return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_enc(ciphertext, shared_secret, public_key);
	}
#endif /* OQS_DIST_BUILD */
#else
	return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_enc(ciphertext, shared_secret, public_key);
#endif
}

OQS_API OQS_STATUS OQS_KEM_GENERATOR_SCHEME_NAME_decaps(uint8_t *shared_secret, const unsigned char *ciphertext, const uint8_t *secret_key) {
#if defined(OQS_ENABLE_KEM_GENERATOR_SCHEME_NAME_avx2)
#if defined(OQS_DIST_BUILD)
	if (OQS_CPU_has_extension(OQS_CPU_EXT_AVX2)) {
#endif /* OQS_DIST_BUILD */
		return (OQS_STATUS) OQS_AVX_NAMESPACE_crypto_kem_dec(shared_secret, ciphertext, secret_key);
#if defined(OQS_DIST_BUILD)
	} else {
		return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_dec(shared_secret, ciphertext, secret_key);
	}
#endif /* OQS_DIST_BUILD */
#else
	return (OQS_STATUS) OQS_NAMESPACE_crypto_kem_dec(shared_secret, ciphertext, secret_key);
#endif
}


#endif
