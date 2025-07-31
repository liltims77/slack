# import yt_dlp

# url = "https://www.youtube.com/watch?v=9P60kdsa8WQ"

# ydl_ops = {}

# with yt_dlp.YoutubeDL(ydl_ops) as ydl:
#     ydl.download([url])

# print("video downloaded")

import yt_dlp

url = "https://www.youtube.com/watch?v=9P60kdsa8WQ"

# Options for yt-dlp
ydl_ops = {
    # You can add various options here, like 'format': 'best', 'outtmpl': 'video.%(ext)s', etc.
}

try:
    with yt_dlp.YoutubeDL(ydl_ops) as ydl:
        ydl.download([url])
    print("Video downloaded successfully")
except Exception as e:
    print(f"An error occurred: {e}")
