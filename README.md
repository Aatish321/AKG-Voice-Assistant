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
## Sample look
![{FF326C6A-D58A-44B9-B296-9A1983544C43}](https://github.com/user-attachments/assets/c65acf24-b036-49da-8e7e-0de4bbc0a099)

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
1)Uses microphone input to capture user speech

2)Converts it to text using speech_recognition

3)Sends text to Gemini (Google Generative AI) via google.generativeai

4)Receives and speaks the response using pyttsx3

5)Executes relevant actions (e.g., open websites, tell time, play music)


📌 Sample Voice Commands

1)“What is the capital of France?”

2)“Play Tum Hi Ho on YouTube”

3)“Open Gmail”

4)“What’s the time now?”

5)“Tell me a joke”

6)"Goodbye” → ends conversation


🧾 Known Limitations

1)Requires an internet connection for AI and YouTube features

2)Works best in a quiet environment for voice recognition

3)Limited token output (controlled by max_output_tokens)

🙏 Acknowledgements

Google Gemini API
,Python SpeechRecognition Library
,Pyttsx3 for TTS
,Ttkbootstrap
PyWhatKit
