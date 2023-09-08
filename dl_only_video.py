import shutil
from yt_dlp import YoutubeDL
import os
import datetime
import sys
import csv

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
            ydl_video_opts = {
                'outtmpl' : '%(title)s'+'_.mp4',
                'format' : 'best',
            }

            with YoutubeDL(ydl_video_opts) as ydl:
                res=ydl.extract_info(path, download=True)
            
            print (res['title'])
            shutil.move(res['title'] + "_.mp4", dir_for_output)
        rowcounter = rowcounter + 1
