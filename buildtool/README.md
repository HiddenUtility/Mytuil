# Abstract
pythonのパッケージやファイルを必要なものだけ選択して出力する。
出力先のルートに置く、ディレクトリまたはファイルを直接指定する。
ディレクトリの場合はサブ階層まで探索してコピーする。
__pycache__は無視する。

# 準備
最初に`./buildtool/settings/setting.xml`を設定する。
デフォルトは下記だが、消してもデフォを自動生成する使用。
1. `Project`は`PackageName`タグのみ必須
1. `Project`タグは複数設定可能。

```xml

<?xml version="1.0" encoding="utf-8"?>
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
```

# 実行
後は本体を実行するだけ。

```py
from buildtool import BuildTool
BuildTool().run()

```