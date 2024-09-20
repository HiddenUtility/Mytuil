#!/usr/bin/python
# -*- coding: utf-8 -*-
"""default_xml.py

Explain : 設定ファイルがない場合のひな形
          
Create  : 2024-06-13(木): H.U
          
Todo    : 
          
"""



default_xml = """<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 出力先のルートディレクトリ -->
  <DestinationDirectory>../dist</DestinationDirectory>
  <!-- ログの出力先 -->
  <LogOutPath>../dist/log</LogOutPath>
  <!-- 一時置きの出力先 -->
  <TemporaryOutPath>../dist/temporary</TemporaryOutPath>

  <!-- 出力設定 Projectタグは複数可 -->
  <Project>
    <!-- 出力するときの名前 -->
    <PackageName>hoge0</PackageName>
    <!-- 出力対象のディレクトリパス -->
    <RequiredDirecotryPaths>
      <Value>./hoge_dir0</Value>
      <Value>./hoge_dir1</Value>
    </RequiredDirecotryPaths>
    <!-- 出力対象のファイルパス -->
    <RequiredFilePaths>
      <Value>./hoge_file0.py</Value>
      <Value>./hoge_file1.py</Value>
    </RequiredFilePaths>
    <!-- 無視したいディレクトリ名 -->
    <IgnoreDirectoryName>
      <Value>ignored_dirname</Value>
    </IgnoreDirectoryName>
    <!-- 無視したいファイル名 -->
    <IgnoreFileName>
      <Value>ignored_filename</Value>
    </IgnoreFileName>
  </Project>

</root>

"""