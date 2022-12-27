
from pytube import YouTube
from tqdm import tqdm

# Set the URL of the video you want to download
url = input('Enter the link of the video to download')

# Create a YouTube object
yt = YouTube(url)

# Keep a reference to the YouTube object in a global variable
global youtube_object
youtube_object = yt

# Get the video ID
video_id = yt.video_id

# Select the highest quality video stream
video = yt.streams.get_highest_resolution()

# Download the video
video.download()

# Print a message when the download is complete
def on_complete(stream, file_handle):
  print(f'Finished downloading {stream.title}')

yt.register_on_complete_callback(on_complete)
