{
  'targets': [
    {
      'target_name': 'dbus',
      'sources': [
        'src/dbus.cc',
        'src/connection.cc',
        'src/signal.cc',
        'src/encoder.cc',
        'src/decoder.cc',
        'src/introspect.cc',
        'src/object_handler.cc'
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'dependencies': [
        'deps/libexpat/libexpat.gyp:expat'
      ],
      'conditions': [
        ['OS=="linux"', {
          'defines': [
            'LIB_EXPAT=expat'
          ],
          'cflags': [
            '-std=gnu++0x',
            '<!@(pkg-config --cflags dbus-1)'
          ],
          'ldflags': [
            '<!@(pkg-config  --libs-only-L --libs-only-other dbus-1)'
          ],
          'libraries': [
            '<!@(pkg-config  --libs-only-l --libs-only-other dbus-1)'
          ]
        }],
        ['OS=="mac"', {
          'include_dirs': [
            "/opt/local/include/dbus-1.0",
            "/opt/local/lib/dbus-1.0/include",
            "/usr/local/opt"
          ],
        }]
      ]
    }
  ]
}
