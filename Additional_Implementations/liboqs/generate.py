import os
import shutil
import subprocess
from pathlib import Path


CLEAN_TARGET_FOLDER = "./kem/ledacrypt"

LEDACRYPT_SOURCE_FOLDERS = [
    'base/Common',
    'base/KEM'
]

LEDACRYPT_CPA_SOURCE_FOLDERS = [
    'base/Common',
    'base/KEM-CPA'
]

params = [
    {'name': 'ledacrypt_23371',
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

    nmspc = (f"OQS_KEM_{parameterSet.upper().replace('-','')}"
             f"_{param['impl'].upper()}")
    for src in param['src_folders']:
        for f in os.listdir(src):
            # copy over common source files
            shutil.copyfile(f"{src}/{f}", f"{pqcleanDir}/{f}")

            # namespace source files
            cmd = f"sed -i 's/OQS_NAMESPACE/{nmspc}/g' '{pqcleanDir}/{f}'"
            print(cmd)
            subprocess.check_call(cmd, shell=True)

            # remove preprocessor conditionals
            cmd = ("unifdef -m " 
                + " ".join(["-D"+d for d in param['def']]) + " "
                + " ".join(['-U'+d for d in param.get('undef', [])])
                #+ f" -f params/params-{param['name']}.h"
                + f" {pqcleanDir}/{f}")
            print(cmd)
            subprocess.call(cmd, shell=True)
        # copy over param specific files

    for f in ['api.h']:
        cmd = "sed -i '" + "".join(["s/"+k+"/"+v+"/g; " for k,v in param['values'].items()]) + "' " + f"'{pqcleanDir}/{f}'"
        subprocess.check_call(cmd, shell=True)


    # copy over oqs header file
    shutil.copyfile(f"base/ledacrypt.c", f"{CLEAN_TARGET_FOLDER}/kem_{parameterSet}.c")
    cmd = f"sed -i 's/OQS_NAMESPACE/{nmspc}/g; s/GENERATOR_SCHEME_NAME/{parameterSet}/g; s/GENERATOR_NIST_LEVEL/{param['values']['GENERATOR_NIST_LEVEL']}/g' {CLEAN_TARGET_FOLDER}/kem_{parameterSet}.c"
    subprocess.call(cmd, shell=True)

# copy main header file and cmake
shutil.copyfile(f"base/kem_ledacrypt.h", f"{CLEAN_TARGET_FOLDER}/kem_ledacrypt.h")
shutil.copyfile(f"base/CMakeLists.txt", f"{CLEAN_TARGET_FOLDER}/CMakeLists.txt")

    # run astyle to fix formatting due to namespace
    #cmd = f"astyle --project {pqcleanDir}/*.[ch]"
    #subprocess.call(cmd, shell=True)