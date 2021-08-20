import subprocess
import os
import sys
import datetime

#-vf scale=320:-1

input_path = "./inputmovs"
fr = 10
width = 640

if not os.path.isdir(input_path):
  os.makedirs(input_path)
  print("./inputmovsフォルダを作成しました。\nその中に変換したい動画ファイルを保存してください。")
  sys.exit()


now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d-%H-%M")
dir_for_output = "./outputgifs/" + current_time

#outputフォルダを作成
os.makedirs(dir_for_output, exist_ok=True)

files = os.listdir(input_path)
for f in files:
  basename_without_ext = os.path.splitext(os.path.basename(f))[0]
  input_file = input_path + "/" + f
  output_file = dir_for_output + "/" + basename_without_ext + ".gif"
  subprocess.run(["ffmpeg" , "-i" , input_file ,"-vf" ,"scale=" + str(width) + ":-1" , "-r" , str(fr) , output_file , "-y"])
