{
  'target_defaults': {
    'defines': [
      'ICE_STATIC_LIBS',
      'ICE_BUILDING_SLICE_COMPILERS'
    ],
    'conditions': [
      ['OS=="win"', {
        'msvs_disabled_warnings': [
          4250,
          4251,
          4275,
          4995
        ],
      }]
    ]
  },

  'targets': [
    {
      'target_name': 'slice2js',
      'type': 'executable',
      'dependencies': ['slice', 'iceutil'],

      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '0',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '1',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
      },
      'sources':  [
        'ice/cpp/src/slice2js/Gen.cpp',
        'ice/cpp/src/slice2js/JsUtil.cpp',
        'ice/cpp/src/slice2js/Main.cpp'
      ],
      'win_delay_load_hook': 'false',
      'include_dirs': [
          'ice/cpp/include',
          'ice/cpp/src/',
          'ice/cpp/src/slice2js'
      ],
      'cflags_cc': [
        '-fexceptions'
      ],
      'cflags_cc!': [
        '-fno-rtti'
      ],
      'conditions': [
        ['OS=="win"', {
          'libraries': [
            '-lrpcrt4.lib', '-ladvapi32.lib', '-lDbgHelp.lib', '-lShlwapi.lib'
          ],
          'libraries!': ['-l"<(node_lib_file)"']
        }],
        ['OS=="linux"', {
          'libraries': [
            '-lrt', '-lcrypto'
          ]
        }]
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "MACOSX_DEPLOYMENT_TARGET": "10.9"
      }
    },

    {
      'target_name': 'slice',
      'type': 'static_library',
      'dependencies': [
        'mcpp/mcpp.gyp:mcpp',
        'iceutil'
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '0',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '1',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
      },
      'sources':  [
        'ice/cpp/src/Slice/Checksum.cpp',
        'ice/cpp/src/Slice/FileTracker.cpp',
        'ice/cpp/src/Slice/Grammar.cpp',
        'ice/cpp/src/Slice/MD5.cpp',
        'ice/cpp/src/Slice/MD5I.cpp',
        'ice/cpp/src/Slice/Parser.cpp',
        'ice/cpp/src/Slice/Preprocessor.cpp',
        'ice/cpp/src/Slice/Scanner.cpp',
        'ice/cpp/src/Slice/SliceUtil.cpp',
        'ice/cpp/src/Slice/StringLiteralUtil.cpp'
      ],
      'win_delay_load_hook': 'false',
      'include_dirs': [
          'ice/cpp/include',
          'ice/cpp/src'
      ],
      'cflags_cc': [
        '-fexceptions'
      ],
      'cflags_cc!': [
        '-fno-rtti'
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "MACOSX_DEPLOYMENT_TARGET": "10.9"
      }
    },

    {
      'target_name': 'iceutil',
      'type': 'static_library',
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '0',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '1',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo': 'true',
                'WarnAsError': 'true'
              },
          },
        },
      },
      'sources':  [
        'ice/cpp/src/IceUtil/ConvertUTF.cpp',
        'ice/cpp/src/IceUtil/ConsoleUtil.cpp',
        'ice/cpp/src/IceUtil/CtrlCHandler.cpp',
        'ice/cpp/src/IceUtil/FileUtil.cpp',
        'ice/cpp/src/IceUtil/InputUtil.cpp',
        'ice/cpp/src/IceUtil/MutexProtocol.cpp',
        'ice/cpp/src/IceUtil/Options.cpp',
        'ice/cpp/src/IceUtil/OutputUtil.cpp',
        'ice/cpp/src/IceUtil/Random.cpp',
        'ice/cpp/src/IceUtil/RecMutex.cpp',
        'ice/cpp/src/IceUtil/Shared.cpp',
        'ice/cpp/src/IceUtil/StringConverter.cpp',
        'ice/cpp/src/IceUtil/StringUtil.cpp',
        'ice/cpp/src/IceUtil/ThreadException.cpp',
        'ice/cpp/src/IceUtil/Time.cpp',
        'ice/cpp/src/IceUtil/Unicode.cpp',
        'ice/cpp/src/IceUtil/UUID.cpp',
        'ice/cpp/src/IceUtil/UtilException.cpp',
      ],
      'win_delay_load_hook': 'false',
      'include_dirs': [
          "ice/cpp/src",
          "ice/cpp/include",
      ],
      'cflags_cc': [
        '-fexceptions',
      ],
      'cflags_cc!': [
        '-fno-rtti'
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "MACOSX_DEPLOYMENT_TARGET": "10.9"
      }
    }
  ]
}
