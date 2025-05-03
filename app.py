from flask import Flask, request, render_template, send_file, redirect, url_for, session
import os
from modules.download_audio import download_audio
from modules.transcribe import transcribe_audio
from modules.summarize import summarize_text

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'

output_dir = r"C:\Users\DELL\OneDrive\Documents\coding\AI podcast analyzer\data\output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def clear_old_results():
    files_to_remove = ["podcast_audio.mp3"]
    for file_name in files_to_remove:
        file_path = os.path.join(output_dir, file_name)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except PermissionError:
                print(f"Skipping {file_path}: Permission denied.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')

        if not youtube_url:
            return render_template('index.html', error="Please enter a valid YouTube URL.")

        print(f"Received YouTube URL: {youtube_url}")

        clear_old_results()

        download_audio(youtube_url)
        audio_path="data/output/podcast_audio.mp3"
        print("Audio downloaded successfully.")

        print(audio_path)
        transcription = transcribe_audio(audio_path)
        print("Transcription completed.")

        summary = summarize_text(transcription)
        print("Summary generated.")

        session['transcription'] = transcription
        session['summary'] = summary
        

        return redirect(url_for('summary'))

    return render_template('index.html')

@app.route('/get_audio')
def get_audio():
    return send_file("data/output/podcast_audio.mp3")


@app.route('/summary')
def summary():
    return render_template('summary.html',
                           audio_url=url_for('get_audio'),
                           transcription=session.get('transcription', ''),
                           summary=session.get('summary', ''))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

