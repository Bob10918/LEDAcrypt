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
	kem->ind_cca = true;

	kem->length_public_key = OQS_KEM_GENERATOR_SCHEME_NAME_length_public_key;
	kem->length_secret_key = OQS_KEM_GENERATOR_SCHEME_NAME_length_secret_key;
	kem->length_ciphertext = OQS_KEM_GENERATOR_SCHEME_NAME_length_ciphertext;
	kem->length_shared_secret = OQS_KEM_GENERATOR_SCHEME_NAME_length_shared_secret;

	kem->keypair = OQS_KEM_GENERATOR_SCHEME_NAME_keypair;
	kem->encaps = OQS_KEM_GENERATOR_SCHEME_NAME_encaps;
	kem->decaps = OQS_KEM_GENERATOR_SCHEME_NAME_decaps;

	return kem;
}

#endif