# mov2gif
* 動画を、gifアニメに変換します。

## 使い方(自分用メモ)
* ffmpegのパスが通っている必要あり
* 適当な場所で実行すれば、inputフォルダが作られます。そこに、動画を保存してください。
* toGif.pyの`fr`と`width`を指定してください。
* 実行すれば、`subprocess.run()`でffmpegを裏で起動し、フォルダ内の動画全てを処理します。
  * `python3`以上じゃないと、subprocessがつかえない。