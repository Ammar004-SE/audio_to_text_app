from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from pydub import AudioSegment
import os
import soundfile as sf
import tempfile

app = Flask(__name__)
UPLOAD_FOLDER = 'Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the Hugging Face Whisper model with PyTorch framework
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-tiny", framework="pt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        # Check if an audio file is included in the request
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        # Save the audio file temporarily
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(temp_path)
        
        # Convert to WAV if necessary
        wav_path = os.path.join(app.config['UPLOAD_FOLDER'], 'converted.wav')
        try:
            audio = AudioSegment.from_file(temp_path)
            audio.export(wav_path, format='wav')
        except Exception as e:
            os.remove(temp_path)
            return jsonify({'error': f'Failed to convert audio: {str(e)}'}), 400
        
        # Read and transcribe the WAV file
        audio_data, sample_rate = sf.read(wav_path)
        result = transcriber(wav_path)
        
        # Clean up temporary files
        os.remove(temp_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
        
        # Return the transcription
        return jsonify({
            'transcription': result['text']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)