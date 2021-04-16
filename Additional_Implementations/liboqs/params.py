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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
     'impl': 'clean',
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
    }
]