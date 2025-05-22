# AKG-Voice-Assistant

# 🎙️ AKG Voice Assistant

AKG is a voice-activated virtual assistant built with Python, leveraging Google's Gemini API to provide real-time intelligent responses. It can answer questions, open websites, play songs on YouTube, tell the time, and more—all using natural voice commands.

---

## ✨ Features

- 🎤 Voice input via microphone (Speech Recognition)
- 💬 AI-based response generation using **Google Gemini (Generative AI)**
- 🔈 Text-to-speech responses (pyttsx3)
- 🌐 Open popular websites (YouTube, Gmail, ChatGPT, etc.)
- 🎵 Play music on YouTube via voice
- 🕒 Tells you the current time
- 🖥️ Graphical User Interface using `ttkbootstrap`
- 🔁 Runs in continuous loop until manually stopped
- 🧠 Remembers to speak every response via TTS

---

## 🛠️ Technologies Used

| Component | Description |
|----------|-------------|
| Python | Core programming language |
| Google Generative AI | For generating conversational responses |
| Pyttsx3 | For Text-to-Speech (offline) |
| SpeechRecognition | To convert voice to text |
| PyWhatKit | For playing YouTube songs |
| TtkBootstrap | For GUI with modern themes |
| Webbrowser | To open websites |
| Threading | To handle background task without freezing the GUI |

---


🧠 How It Works
Uses microphone input to capture user speech
Converts it to text using speech_recognition
Sends text to Gemini (Google Generative AI) via google.generativeai
Receives and speaks the response using pyttsx3
Executes relevant actions (e.g., open websites, tell time, play music)


📌 Sample Voice Commands
“What is the capital of France?”
“Play Tum Hi Ho on YouTube”
“Open Gmail”
“What’s the time now?”
“Tell me a joke”
"Goodbye” → ends conversation


🧾 Known Limitations
Requires an internet connection for AI and YouTube features
Works best in a quiet environment for voice recognition
Limited token output (controlled by max_output_tokens)

🙏 Acknowledgements
Google Gemini API
Python SpeechRecognition Library
Pyttsx3 for TTS
Ttkbootstrap
PyWhatKit
