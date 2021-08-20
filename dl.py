import youtube_dl

path = "https://www.youtube.com/watch?v=Zm_tAkWmZPo"


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s','format':'137'})

with ydl:
    result = ydl.extract_info(
        path,
        download=True # We just want to extract the info
    )

