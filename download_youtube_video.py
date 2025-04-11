


# https://www.youtube.com/watch?v=Acbc_f3sfLM&t=5674s


from pytube import YouTube

# URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=Acbc_f3sfLM&t=5674s"

# Create YouTube object
yt = YouTube(video_url)

# Choose the highest resolution stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download(output_path='.', filename='downloaded_video.mp4')

print("Download complete!")
