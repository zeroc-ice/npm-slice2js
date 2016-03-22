{
  'target_defaults': {
    'defines' : [
      'ICE_STATIC_LIBS'
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
      'dependencies' : ['slice', 'iceutil'],

      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
                'RuntimeLibrary': '2',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo' : 'true',
                'WarnAsError' : 'true'
              },
          },
        },
      },
      'sources':  [
        'ice/cpp/src/slice2js/Gen.cpp',
        'ice/cpp/src/slice2js/JsUtil.cpp',
        'ice/cpp/src/slice2js/Main.cpp'
      ],
      'include_dirs' : [
          'ice/cpp/include',
          'ice/cpp/src/',
          'ice/cpp/src/slice2js'
      ],
      'cflags_cc' : [
        '-fexceptions'
      ],
      'cflags_cc!' : [
        '-fno-rtti'
      ],
      'conditions': [
        ['OS=="win"', {
          'libraries': [
            '-lrpcrt4.lib', '-ladvapi32.lib', '-lDbgHelp.lib', '-lShlwapi.lib'
          ]
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
        "MACOSX_DEPLOYMENT_TARGET":"10.9"
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
                'RuntimeLibrary': '2',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo' : 'true',
                'WarnAsError' : 'true'
              }
          }
        }
      },
      'defines': [
        'ICE_BUILDING_SLICE',
      ],
      'sources':  [
        'ice/cpp/src/Slice/CPlusPlusUtil.cpp',
        'ice/cpp/src/Slice/DotNetNames.cpp',
        'ice/cpp/src/Slice/JavaUtil.cpp',
        'ice/cpp/src/Slice/PHPUtil.cpp',
        'ice/cpp/src/Slice/PythonUtil.cpp',
        'ice/cpp/src/Slice/Util.cpp',
        'ice/cpp/src/Slice/Checksum.cpp',
        'ice/cpp/src/Slice/FileTracker.cpp',
        'ice/cpp/src/Slice/MD5.cpp',
        'ice/cpp/src/Slice/Parser.cpp',
        'ice/cpp/src/Slice/RubyUtil.cpp',
        'ice/cpp/src/Slice/CsUtil.cpp',
        'ice/cpp/src/Slice/Grammar.cpp',
        'ice/cpp/src/Slice/MD5I.cpp',
        'ice/cpp/src/Slice/Preprocessor.cpp',
        'ice/cpp/src/Slice/Scanner.cpp'
      ],
      'include_dirs' : [
          'ice/cpp/include',
          'ice/cpp/src'
      ],
      'cflags_cc' : [
        '-fexceptions'
      ],
      'cflags_cc!' : [
        '-fno-rtti'
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "MACOSX_DEPLOYMENT_TARGET":"10.9"
      }
    },

    {
      'target_name': 'iceutil',
      'type': 'static_library',
      'configurations': {
        'Release': {
          'msvs_settings': {

            'VCCLCompilerTool': {
                'RuntimeLibrary': '2',
                'ExceptionHandling': '1',
                'RuntimeTypeInfo' : 'true',
                'WarnAsError' : 'true'
              },
          },
        },
      },
      'defines': [
        'ICE_BUILDING_ICE_UTIL',
      ],
      'sources':  [
        'ice/cpp/src/IceUtil/ArgVector.cpp',
        'ice/cpp/src/IceUtil/Cond.cpp',
        'ice/cpp/src/IceUtil/ConvertUTF.cpp',
        'ice/cpp/src/IceUtil/CountDownLatch.cpp',
        'ice/cpp/src/IceUtil/CtrlCHandler.cpp',
        'ice/cpp/src/IceUtil/Exception.cpp',
        'ice/cpp/src/IceUtil/FileUtil.cpp',
        'ice/cpp/src/IceUtil/InputUtil.cpp',
        'ice/cpp/src/IceUtil/MutexProtocol.cpp',
        'ice/cpp/src/IceUtil/Options.cpp',
        'ice/cpp/src/IceUtil/OutputUtil.cpp',
        'ice/cpp/src/IceUtil/Random.cpp',
        'ice/cpp/src/IceUtil/RecMutex.cpp',
        'ice/cpp/src/IceUtil/SHA1.cpp',
        'ice/cpp/src/IceUtil/Shared.cpp',
        'ice/cpp/src/IceUtil/StringConverter.cpp',
        'ice/cpp/src/IceUtil/StringUtil.cpp',
        'ice/cpp/src/IceUtil/Thread.cpp',
        'ice/cpp/src/IceUtil/ThreadException.cpp',
        'ice/cpp/src/IceUtil/Time.cpp',
        'ice/cpp/src/IceUtil/Timer.cpp',
        'ice/cpp/src/IceUtil/Unicode.cpp',
        'ice/cpp/src/IceUtil/UUID.cpp'
      ],
      'include_dirs' : [
          "ice/cpp/src",
          "ice/cpp/include",
      ],
      'cflags_cc' : [
        '-fexceptions',
      ],
      'cflags_cc!' : [
        '-fno-rtti'
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "MACOSX_DEPLOYMENT_TARGET":"10.9"
      }
    }
  ]
}
