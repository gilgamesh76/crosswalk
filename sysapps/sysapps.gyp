{
  'targets': [
    {
      'target_name': 'sysapps',
      'type': 'static_library',
      'dependencies': [
        '../../base/base.gyp:base',
        '../../net/net.gyp:net',
        '../../ui/ui.gyp:ui',
        '../extensions/extensions.gyp:xwalk_extensions',
        'sysapps_resources.gyp:xwalk_sysapps_resources',
      ],
      'variables': {
        'jsapi_component': 'sysapps',
      },
      'includes': [
        '../../build/filename_rules.gypi',
        '../xwalk_jsapi.gypi',
      ],
      'sources': [
        'common/binding_object.h',
        'common/binding_object_store.cc',
        'common/binding_object_store.h',
        'common/common.idl',
        'common/event_target.cc',
        'common/event_target.h',
        'common/sysapps_manager.cc',
        'common/sysapps_manager.h',
        'common/sysapps_manager_android.cc',
        'common/sysapps_manager_linux.cc',
        'common/sysapps_manager_mac.cc',
        'common/sysapps_manager_win.cc',
        'device_capabilities_new/av_codecs_provider.h',
        'device_capabilities_new/av_codecs_provider_android.cc',
        'device_capabilities_new/av_codecs_provider_android.h',
        'device_capabilities_new/cpu_info_provider.cc',
        'device_capabilities_new/cpu_info_provider.h',
        'device_capabilities_new/cpu_info_provider_android.cc',
        'device_capabilities_new/cpu_info_provider_linux.cc',
        'device_capabilities_new/cpu_info_provider_mac.cc',
        'device_capabilities_new/cpu_info_provider_win.cc',
        'device_capabilities_new/device_capabilities.idl',
        'device_capabilities_new/device_capabilities_extension_new.cc',
        'device_capabilities_new/device_capabilities_extension_new.h',
        'device_capabilities_new/device_capabilities_object.cc',
        'device_capabilities_new/device_capabilities_object.h',
        'device_capabilities_new/memory_info_provider.cc',
        'device_capabilities_new/memory_info_provider.h',
        'device_capabilities_new/storage_info_provider.cc',
        'device_capabilities_new/storage_info_provider.h',
        'device_capabilities_new/storage_info_provider_mock.cc',
        'device_capabilities_new/storage_info_provider_mock.h',
        'raw_socket/raw_socket.idl',
        'raw_socket/raw_socket_extension.cc',
        'raw_socket/raw_socket_extension.h',
        'raw_socket/raw_socket_object.cc',
        'raw_socket/raw_socket_object.h',
        'raw_socket/tcp_server_socket.idl',
        'raw_socket/tcp_server_socket_object.cc',
        'raw_socket/tcp_server_socket_object.h',
        'raw_socket/tcp_socket.idl',
        'raw_socket/tcp_socket_object.cc',
        'raw_socket/tcp_socket_object.h',
      ],
      'conditions': [
        ['OS!="android"', {
          'dependencies': [
            '../../content/content.gyp:content_common',
            '../../media/media.gyp:media',
            '../../third_party/ffmpeg/ffmpeg.gyp:ffmpeg',
          ],
          'sources': [
            'device_capabilities_new/av_codecs_provider_ffmpeg.cc',
            'device_capabilities_new/av_codecs_provider_ffmpeg.h',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          # Build units including this module should have this
          # on theirs include path because of the code we generate
          # from the IDL files.
          '<(SHARED_INTERMEDIATE_DIR)',
        ]
      },
    },
  ],
}