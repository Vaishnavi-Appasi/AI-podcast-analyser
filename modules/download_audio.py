import yt_dlp
import os

# Set the output directory path
output_dir = "data/output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def download_audio(video_url):
    output_path = os.path.join(output_dir, "podcast_audio.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'ffmpeg_location': r"C:\Users\DELL\Downloads\ffmpeg\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin\ffmpeg.exe",  # Update to the correct ffmpeg path
        'noplaylist': True,
        'continuedl': False,
        'nopart': True,
        'retries': 10,
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Audio downloaded and saved to {output_dir}/podcast_audio.mp3")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed: {str(e)}")
