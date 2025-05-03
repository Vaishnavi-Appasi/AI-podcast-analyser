import yt_dlp

def download_audio(vd_url):
    output_path = "data/output/podcast_audio.%(ext)s"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'ffmpeg_location': r"C:\Users\DELL\Downloads\ffmpeg\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin\ffmpeg.exe",
        'noplaylist': True,
        'continuedl': False,      
        'nopart': True,           
        'retries': 10,            
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vd_url])
        print(f"Audio downloaded and saved to data/output/podcast_audio.mp3")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed: {str(e)}")
