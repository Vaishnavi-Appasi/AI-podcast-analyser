import os
import whisper
import torch

# Set FFMPEG path
FFMPEG_PATH = r"C:\Users\DELL\Downloads\ffmpeg\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin"
os.environ["PATH"] += os.pathsep + FFMPEG_PATH

def transcribe_audio(audio_path):
    # Use GPU if available, else use CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    try:
        # Load Whisper model
        model = whisper.load_model("base", device=device)
        
        # Perform transcription
        result = model.transcribe(audio_path)
        
        # Extract the transcription and detected language
        detected_language = result["language"]
        transcription = result["text"]
        
        print(f"Transcription ({detected_language}):\n", transcription)
        
        return transcription, detected_language
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return None, None
