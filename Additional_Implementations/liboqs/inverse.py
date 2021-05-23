import os
import shutil
import subprocess
from pathlib import Path
from params import params, IMPLEMENTATIONS


#TARGET_FOLDER = "./kem/ledacrypt"
TARGET_FOLDER = "./tables"


for param in params:
    p = param['name'].split('_')[-1]
    cmd = (f"cp ./tables/inverse_perm_tables.h ./tables/inverse_perm_tables_{p}.h")
    subprocess.call(cmd, shell=True)
    cmd = (f"unifdef -m -DP={p} ./tables/inverse_perm_tables_{p}.h")
    print(cmd)
    subprocess.call(cmd, shell=True)
    nmspc = (f"OQS_KEM_{param['name'].upper().replace('-','')}_AVX2")
    cmd = f"sed -i 's/inverse_index_permutation_table/{nmspc}_inverse_index_permutation_table/g' './tables/inverse_perm_tables_{p}.h'"
    print(cmd)
    subprocess.check_call(cmd, shell=True)