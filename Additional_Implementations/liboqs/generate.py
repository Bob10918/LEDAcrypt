import os
import shutil
import subprocess
from pathlib import Path


CLEAN_TARGET_FOLDER = "./kem/ledacrypt"
#NINETIES_TARGET_FOLDER = "./kem/ledacrypt"

LEDACRYPT_SOURCE_FOLDERS = [
    'base/Common',
    'base/KEM'
]

LEDACRYPT_FILES = [
    'LICENSE.TXT',
    'META.yml',
    'aes256.c',
    'aes256.h',
    'api.h',
    'bf_decoding.c',
    'bf_decoding.h',
    'dfr_test.c',
    'dfr_test.h',
    'djbsort.c',
    'djbsort.h',
    'gf2x_arith.c',
    'gf2x_arith.h',
    'gf2x_arith_mod_xPplusOne.c',
    'gf2x_arith_mod_xPplusOne.h',
    'gf2x_limbs.h',
    'H_Q_matrices_generation.c',
    'H_Q_matrices_generation.h',
    'Makefile',
    'Makefile.Microsoft_nmake',
    'niederreiter.h',
    'niederreiter_decrypt.c',
    'niederreiter_decrypt.h',
    'niederreiter_encrypt.c',
    'niederreiter_encrypt.h',
    'niederreiter_keygen.c',
    'niederreiter_keygen.h',
    'qc_ldpc_parameters.h',
    'rng.c',
    'rng.h'
]

# LEDACRYPT_CPA_FILES = [
#     'LICENSE',
#     'api.h',
#     'aes256ctr.c',
#     'aes256ctr.h',
#     'cbd.c',
#     'cbd.h',
#     'indcpa.c',
#     'indcpa.h',
#     'kem.c',
#     'ntt.c',
#     'ntt.h',
#     'params.h',
#     'poly.c',
#     'poly.h',
#     'polyvec.c',
#     'polyvec.h',
#     'reduce.c',
#     'reduce.h',
#     'symmetric.h',
#     'verify.c',
#     'verify.h',
# ]


params = [
    {'name': 'ledacrypt23371',
     'impl': 'clean',
     'def': ['CATEGORY=1', 'N0=2', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'target': CLEAN_TARGET_FOLDER,
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '2928',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2952',
         'GENERATOR_NISTKAT_SHA256' : 'c0b5a0c5ea96c69f172e5362bdd95a82e70cdec78c3b501b459d355717a30b86',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_CLAIMED_SECURITY' : 'IND-CCA2'
     }
    }
]

for param in params:
    TARGET_FOLDER = param['target']
    parameterSet = param['name']
    pqcleanDir = f"{TARGET_FOLDER}/{parameterSet}_{param['impl']}"

    # delete old files
    if Path(pqcleanDir).exists():
        shutil.rmtree(pqcleanDir)
    os.makedirs(pqcleanDir)

    nmspc = (f"PQCLEAN_{parameterSet.upper().replace('-','')}"
             f"_{param['impl'].upper()}")
    for src in param['src_folders']:
        for f in os.listdir(src):
            # copy over common source files
            shutil.copyfile(f"{src}/{f}", f"{pqcleanDir}/{f}")

            # namespace source files
            cmd = f"sed -i 's/PQCLEAN_NAMESPACE/{nmspc}/g' '{pqcleanDir}/{f}'"
            print(cmd)
            subprocess.check_call(cmd, shell=True)

            # remove preprocessor conditionals
            cmd = ("unifdef -m " + " ".join(["-D"+d for d in param['def']]) + " "
                + " ".join(['-U'+d for d in param.get('undef', [])])
                #+ f" -f params/params-{param['name']}.h"
                + f" {pqcleanDir}/{f}")
            print(cmd)
            subprocess.call(cmd, shell=True)
        # copy over param specific files

    for f in ['api.h', 'META.yml']:
        cmd = "sed -i '" + "".join(["s/"+k+"/"+v+"/g; " for k,v in param['values'].items()]) + "' " + f"'{pqcleanDir}/{f}'"
        subprocess.check_call(cmd, shell=True)

    # replace lib name
    #cmd = f"sed -i 's/SCHEME_NAME/{parameterSet}/g' {pqcleanDir}/{f}"
    #subprocess.call(cmd, shell=True)

    # run astyle to fix formatting due to namespace
    #cmd = f"astyle --project {pqcleanDir}/*.[ch]"
    #subprocess.call(cmd, shell=True)