IMPLEMENTATIONS = ['clean', 'avx2']

LEDACRYPT_SOURCE_FOLDERS = {
    'clean':['base/Reference_Implementation/Common', 'base/Reference_Implementation/KEM'],
    'avx2':['base/Optimized_Implementation/Common', 'base/Optimized_Implementation/KEM']
}

LEDACRYPT_CPA_SOURCE_FOLDERS = {
    'clean':['base/Reference_Implementation/Common', 'base/Reference_Implementation/KEM-CPA'],
    'avx2':['base/Optimized_Implementation/Common', 'base/Optimized_Implementation/KEM-CPA']
}

params = [
    {'name': 'ledacrypt_23371',
     'def': ['CATEGORY=1', 'N0=2', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '2928',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2952',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_16067',
     'def': ['CATEGORY=1', 'N0=3', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '4032',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2040',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_13397',
     'def': ['CATEGORY=1', 'N0=4', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '5040',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '1704',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_28277',
     'def': ['CATEGORY=1', 'N0=2', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '3536',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '3560',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_19709',
     'def': ['CATEGORY=1', 'N0=3', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '4928',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2488',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_16229',
     'def': ['CATEGORY=1', 'N0=4', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '50',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '6096',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2056',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_40787',
     'def': ['CATEGORY=3', 'N0=2', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '5104',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '5136',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_28411',
     'def': ['CATEGORY=3', 'N0=3', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '7104',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '3584',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_22901',
     'def': ['CATEGORY=3', 'N0=4', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '8592',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2896',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_52667',
     'def': ['CATEGORY=3', 'N0=2', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '6584',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '6616',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_36629',
     'def': ['CATEGORY=3', 'N0=3', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '9168',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '4616',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_30803',
     'def': ['CATEGORY=3', 'N0=4', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '66',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '11568',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '3888',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_61717',
     'def': ['CATEGORY=5', 'N0=2', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '7720',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '7760',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_42677',
     'def': ['CATEGORY=5', 'N0=3', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '10672',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '5376',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_35507',
     'def': ['CATEGORY=5', 'N0=4', 'DFR_SL_LEVEL=0'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '13320',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '4480',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_83579',
     'def': ['CATEGORY=5', 'N0=2', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '10448',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '10488',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_58171',
     'def': ['CATEGORY=5', 'N0=3', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '14544',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '7312',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_48371',
     'def': ['CATEGORY=5', 'N0=4', 'DFR_SL_LEVEL=1'],
     'undef': [],
     'src_folders': LEDACRYPT_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '82',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '18144',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '6088',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'true'
     }
    },
    {'name': 'ledacrypt_cpa_10883',
     'def': ['CATEGORY=1', 'N0=2'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '1160',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '1368',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '1392',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_8237',
     'def': ['CATEGORY=1', 'N0=3'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '1920',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '2064',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '1056',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_7187',
     'def': ['CATEGORY=1', 'N0=4'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '24',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '2680',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '2712',
         'GENERATOR_CRYPTO_BYTES' : '32',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '928',
         'GENERATOR_NIST_LEVEL' : '1',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_21011',
     'def': ['CATEGORY=3', 'N0=2'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '1680',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '2632',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2664',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_15373',
     'def': ['CATEGORY=3', 'N0=3'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '2840',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '3856',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '1960',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_13109',
     'def': ['CATEGORY=3', 'N0=4'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '32',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '3968',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '4920',
         'GENERATOR_CRYPTO_BYTES' : '48',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '1672',
         'GENERATOR_NIST_LEVEL' : '3',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_35339',
     'def': ['CATEGORY=5', 'N0=2'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '2232',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '4424',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '4464',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_25603',
     'def': ['CATEGORY=5', 'N0=3'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '3760',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '6416',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '3248',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'false'
     }
    },
    {'name': 'ledacrypt_cpa_21611',
     'def': ['CATEGORY=5', 'N0=4'],
     'undef': [],
     'src_folders': LEDACRYPT_CPA_SOURCE_FOLDERS,
     'values': {
         'GENERATOR_CRYPTO_RANDOMBYTES': '40',
         'GENERATOR_CRYPTO_SECRETKEYBYTES' : '5256',
         'GENERATOR_CRYPTO_PUBLICKEYBYTES' : '8112',
         'GENERATOR_CRYPTO_BYTES' : '64',
         'GENERATOR_CRYPTO_CIPHERTEXTBYTES' : '2744',
         'GENERATOR_NIST_LEVEL' : '5',
         'GENERATOR_IND_CCA' : 'false'
     }
    }
]