import shutil
import youtube_dl
import os
import datetime
import sys
import csv
import subprocess

if not os.path.isfile("dl_paths.csv"):
    with open('dl_paths.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["動画のURL", "保存したい名前(拡張子無し)"])
    print("csvを作成しました、ダウンロードしたい動画のパスを記入してください")
    sys.exit()


# outputフォルダを作成
now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d-%H-%M")
dir_for_output = "./dl_output/" + current_time
os.makedirs(dir_for_output, exist_ok=True)

# csvを１行ごと処理する。
rowcounter = 0
with open('dl_paths.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if rowcounter == 0:
            pass
        else:
            path = row[0]
            print(path + "の処理を開始します___________")

            #動画のIDをURLから取得
            ## こっちはOK     → https://www.youtube.com/watch?v=WJzSBLCaKc8
            ## 短縮URLは未対応 → https://youtu.be/WJzSBLCaKc8
            douga_name = path.split("=")[-1]

            #youtube_dlは、"動画id+mp4"(ピリオドなし)で動画を保存してしまうことがある。
            #そのときのために、パスの修正を泥臭く行う。
            douga_ok_name = douga_name + "mp4.mp4"
            douga_false_name = douga_name + "mp4"

            ydl = youtube_dl.YoutubeDL(
                {'outtmpl': '%(id)s%(ext)s', 'format': 'best'})

            with ydl:
                result = ydl.extract_info(
                    path,
                    download=True 
                )

            if os.path.isfile(douga_false_name):
                print("ファイル名を訂正します。")
                os.rename(douga_false_name, douga_ok_name)

            os.rename(douga_ok_name, str(row[1]) + ".mp4")
            shutil.move(str(row[1]) + ".mp4", dir_for_output)

            #mp3変換
            subprocess.run(["ffmpeg" , "-i" , dir_for_output + "/" + str(row[1]) + ".mp4" ,"-vn" , dir_for_output + "/" + str(row[1]) + ".mp3"])

        rowcounter = rowcounter + 1
