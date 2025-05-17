 AudioScribe Pro: AI-Powered Audio Transcription Service

AudioScribe Pro:  is a web application that leverages artificial intelligence to transcribe audio files (MP3, WAV, AAC) and live microphone recordings into text. Built with Flask and the Hugging Face Whisper model, it offers a responsive, user-friendly interface with drag-and-drop file uploads, real-time audio recording, and options to copy or export transcriptions. This project demonstrates expertise in full-stack development, AI integration, and responsive web design.

1.1 Key Features:
Audio Upload: Upload MP3, WAV, or AAC files (up to 2GB) via file selection or drag-and-drop.
Live Recording: Record audio directly in the browser using a microphone.
AI Transcription: Transcribe audio using the `openai/whisper-small` model for high accuracy.
Copy & Export: Copy transcriptions to the clipboard or export as a text file.
Responsive Design: Mobile-friendly UI with a dedicated navigation bar for small screens.
Error Handling: Validates file sizes and handles microphone/audio errors gracefully.

1.2 Technologies Used:
Backend: Flask, Flask-CORS (Python web framework and API handling).
Frontend: HTML, CSS, JavaScript (responsive UI with WebRTC for audio recording).
AI Model: Hugging Face Transformers (`whisper-small` for speech-to-text).
Audio Processing: PyTorch, Torchaudio, Pydub, Soundfile, FFmpeg.
Version Control: Git, GitHub.
Dependencies: Managed via `requirements.txt`.

1.3 Project Structure:
audio_to_text_app/
├── .gitignore                             Excludes venv, pycache, uploads
├── README.md                       Project documentation
├── app.py                                  Flask backend
├── requirements.txt               Python dependencies
├── templates/                          HTML templates
│   └── index.html                     Frontend UI
├── Uploads/                            Temporary audio files
├── screenshot.png                 App screenshot
└── demo.mp4                         Demo video

1.4 Setup Instructions:
1. Clone the Repository:
   git clone https://github.com/Ammar004-SE/audio_to_text_app.git
   cd audio_to_text_app
2. Create a Virtual Environment:  
   python -m venv venv
  \venv\Scripts\activate  # Windows
3. Install Dependencies:
      pip install -r requirements.txt
4. Install FFmpeg:
   Download from [FFmpeg](https://ffmpeg.org/download.html).
   Add to system PATH (e.g., `C:\ffmpeg\bin`).
   Verify: ffmpeg -version.
5. Run the App:
      python app.py
6. Open  [http://127.0.0.1:5000]   in a browser.

1.5 Usage:
Upload Audio: Select an audio file or drag-and-drop into the drop zone, then click "Transcribe Now".
Record Audio: Click "Record Audio", speak, and click "Stop & Process" to transcribe.
Copy/Export: Use "Copy Text" to copy the transcription or "Export" to download as `transcription.txt`.
Mobile View: On screens <640px, use the bottom navigation bar for uploading or recording.

1.6 Requirements:
Software: Python 3.8+, Git, FFmpeg, modern web browser (Chrome recommended).
Hardware: Microphone for recording, ~2GB storage for dependencies.
Python Packages: Flask, Flask-CORS, Transformers, PyTorch, Torchaudio, Pydub, Soundfile (see `requirements.txt`).

 1.7 Development Highlights:
Backend: Flask serves the app and handles audio uploads via a `/transcribe` endpoint, with CORS for cross-origin requests.
Frontend: Responsive HTML/CSS/JavaScript UI with WebRTC for microphone access and drag-and-drop functionality.
AI Integration: Uses `whisper-small` for efficient, accurate transcription.
Error Handling: Validates file sizes (max 2GB) and provides user-friendly error messages for file or microphone issues.
Version Control: Managed with Git, hosted on GitHub for collaboration and deployment.


