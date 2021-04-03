# SPDX-License-Identifier: MIT

set(_LEDACRYPT_OBJS "")

if(OQS_ENABLE_KEM_ledacrypt_23371)
    add_library(ledacrypt_23371_clean OBJECT kem_ledacrypt_23371.c ledacrypt_23371_clean/aes256.c ledacrypt_23371_clean/bf_decoding.c ledacrypt_23371_clean/dfr_test.c ledacrypt_23371_clean/djbsort.c ledacrypt_23371_clean/gf2x_arith.c ledacrypt_23371_clean/gf2x_arith_mod_xPplusOne.c ledacrypt_23371_clean/H_Q_matrices_generation.c ledacrypt_23371_clean/kem.c ledacrypt_23371_clean/niederreiter_decrypt.c ledacrypt_23371_clean/niederreiter_encrypt.c ledacrypt_23371_clean/niederreiter_keygen.c ledacrypt_23371_clean/rng.c)
    target_include_directories(ledacrypt_23371_clean PRIVATE ${CMAKE_CURRENT_LIST_DIR}/ledacrypt_23371_clean)
    #target_include_directories(ledacrypt_23371_clean PRIVATE ${PROJECT_SOURCE_DIR}/src/common/pqclean_shims)
    set(_CLASSIC_MCELIECE_OBJS ${_CLASSIC_MCELIECE_OBJS} $<TARGET_OBJECTS:ledacrypt_23371_clean>)
endif()

set(LEDACRYPT_OBJS ${_LEDACRYPT_OBJS} PARENT_SCOPE)