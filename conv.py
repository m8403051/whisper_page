from flask import Flask, request, render_template_string, send_file
import whisper
import os
import tempfile

app = Flask(__name__)

MODEL = whisper.load_model("base")  # You can change to "small", "medium", etc.

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Whisper SRT Generator</title>
</head>
<body>
    <h2>Upload MP3 or MP4 to Generate SRT</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="audiofile" accept=".mp3,.mp4" required>
        <button type="submit">Generate SRT</button>
    </form>
    {% if srt_url %}
    <p><a href="{{ srt_url }}" download>Download SRT File</a></p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    srt_url = None
    if request.method == 'POST':
        audio = request.files['audiofile']
        if audio:
            with tempfile.TemporaryDirectory() as tmpdir:
                input_path = os.path.join(tmpdir, audio.filename)
                audio.save(input_path)
                
                # Transcribe and save to .srt
                result = MODEL.transcribe(input_path, task="transcribe")
                srt_path = os.path.join("static", f"{os.path.splitext(audio.filename)[0]}.srt")
                os.makedirs("static", exist_ok=True)
                with open(srt_path, "w", encoding="utf-8") as f:
                    for i, segment in enumerate(result["segments"]):
                        start = format_time(segment["start"])
                        end = format_time(segment["end"])
                        f.write(f"{i+1}\n{start} --> {end}\n{segment['text'].strip()}\n\n")
                srt_url = f"/{srt_path}"
    return render_template_string(HTML, srt_url=srt_url)

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
