import os
import shutil
import subprocess
from pathlib import Path
from params import params, IMPLEMENTATIONS


#TARGET_FOLDER = "./kem/ledacrypt"
TARGET_FOLDER = "/home/bob/liboqs/src/kem/ledacrypt"


for param in params:
    for impl in IMPLEMENTATIONS:
        parameterSet = param['name']
        pqcleanDir = f"{TARGET_FOLDER}/{parameterSet}_{impl}"

        # delete old files
        if Path(pqcleanDir).exists():
            shutil.rmtree(pqcleanDir)
        os.makedirs(pqcleanDir)

        nmspc = (f"OQS_KEM_{parameterSet.upper().replace('-','')}"
                f"_{impl.upper()}")
        for src in param['src_folders'][impl]:
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
                    + f" {pqcleanDir}/{f}")
                print(cmd)
                subprocess.call(cmd, shell=True)

        # copy over param specific files
        for f in ['api.h']:
            cmd = "sed -i '" + "".join(["s/"+k+"/"+v+"/g; " for k,v in param['values'].items()]) + "' " + f"'{pqcleanDir}/{f}'"
            subprocess.check_call(cmd, shell=True)

        # copy specific table if this is the optimized implementation
        if impl=='avx2':
            shutil.copyfile(f"./tables/inverse_perm_tables_{parameterSet.split('_')[-1]}.h", f"{pqcleanDir}/inverse_perm_tables.h")

    # copy over oqs header file
    shutil.copyfile(f"base/ledacrypt.c", f"{TARGET_FOLDER}/kem_{parameterSet}.c")
    clean_nmspc = (f"OQS_KEM_{parameterSet.upper().replace('-','')}_CLEAN")
    avx_nmspc = clean_nmspc.replace('_CLEAN', '_AVX2')
    cmd = f"sed -i 's/OQS_NAMESPACE/{clean_nmspc}/g; s/OQS_AVX_NAMESPACE/{avx_nmspc}/g; s/GENERATOR_SCHEME_NAME/{parameterSet}/g; s/GENERATOR_NIST_LEVEL/{param['values']['GENERATOR_NIST_LEVEL']}/g' {TARGET_FOLDER}/kem_{parameterSet}.c"
    subprocess.call(cmd, shell=True)


# copy main header file and cmake
shutil.copyfile(f"base/kem_ledacrypt.h", f"{TARGET_FOLDER}/kem_ledacrypt.h")
shutil.copyfile(f"base/CMakeLists.txt", f"{TARGET_FOLDER}/CMakeLists.txt")

# run astyle to fix formatting due to namespace
# cmd = f"astyle --project {pqcleanDir}/*.[ch]"
# subprocess.call(cmd, shell=True)