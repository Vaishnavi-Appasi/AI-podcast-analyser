import os
import whisper
import torch

FFMPEG_PATH = r"C:\Users\DELL\Downloads\ffmpeg\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin"

os.environ["PATH"] += os.pathsep + FFMPEG_PATH

def transcribe_audio(audio_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("base", device=device)
    result = model.transcribe(audio_path)
    detected_language = result["language"]
    transcription = result["text"]

    print("Transcription:\n", transcription)

    return transcription, detected_language