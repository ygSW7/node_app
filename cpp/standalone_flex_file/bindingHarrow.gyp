{
  "targets": [
    {
      "target_name": "standalone_flex_fileHarrow",
      "type": "executable",
      "sources": [ "mainHarrow.cpp"],
      "cflags": ["-Wall", "-std=c++11"],
      "include_dirs" : ['../prime4standalone'],
      "conditions": [ 
        [ 'OS=="mac"', { 
            "xcode_settings": { 
                'OTHER_CPLUSPLUSFLAGS' : ['-std=c++11','-stdlib=libc++'], 
                'OTHER_LDFLAGS': ['-stdlib=libc++'], 
                'MACOSX_DEPLOYMENT_TARGET': '10.7' } 
            }
        ] 
      ] 
    }
  ]
}