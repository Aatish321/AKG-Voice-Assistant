from google import genai

import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
import datetime
import webbrowser
import pywhatkit
from apikey import api_data

# Configure Gemini API
GENAI_API_KEY = api_data
genai.configure(api_key=GENAI_API_KEY)

# Text-to-Speech Engine
engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        conversation_area.insert(END, "Listening...\n\n")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            query = recognizer.recognize_google(audio, language='en-in').lower()
            conversation_area.insert(END, f"You: {query}\n")
            return query
        except sr.UnknownValueError:
            conversation_area.insert(END, "AKG: Sorry, I didn't catch that. Please repeat.\n")
            speak("Sorry, I didn't catch that. Please repeat.")
            return "none"
        except sr.RequestError:
            conversation_area.insert(END, "AKG: Network error. Please check your connection.\n")
            speak("Network error. Please check your connection.")
            return "none"
        except Exception as e:
            conversation_area.insert(END, f"AKG: Error: {e}\n")
            speak("Sorry, I encountered an error.")
            return "none"

def generate_response(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query, generation_config=genai.GenerationConfig(
            max_output_tokens=75,
            temperature=0.1,
        ))
        return response.text
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

stop_conversation = False

def handle_conversation():
    global stop_conversation
    while not stop_conversation:
        query = listen_to_command()
        if query == "none":
            continue

        if "bye" in query or "goodbye" in query:
            conversation_area.insert(END, "AKG: Goodbye! Have a great day!\n")
            speak("Goodbye! Have a great day!")
            break

        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "chatgpt": "https://chat.openai.com",
            "gmail": "https://mail.google.com",
            "hotstar": "https://www.hotstar.com",
            "google": "https://www.google.com",
            "instagram": "https://www.instagram.com"
        }

        # ✅ New logic to handle "play X on youtube"
        if "play" in query and "youtube" in query:
            song = query.replace("play", "").replace("on youtube", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            return

        # Open general sites
        for site in sites:
            if f"open {site}" in query:
                speak(f"Opening {site} sir...")
                webbrowser.open(sites[site])
                return

        # Tell the time
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strfTime}")
            conversation_area.insert(END, f"AKG: The time is {strfTime}\n")
            return

        # General AI response
        response = generate_response(query)
        conversation_area.insert(END, f"AKG: {response}\n")
        speak(response)

def start_conversation():
    global stop_conversation
    stop_conversation = False
    conversation_thread = threading.Thread(target=handle_conversation)
    conversation_thread.daemon = True
    conversation_thread.start()
    conversation_area.insert(END, "Hi, I am AKG. How can I help you?\n\n")
    conversation_area.see(END)
    speak("Hi, I am AKG. How can I help you")

def end_conversation():
    global stop_conversation
    stop_conversation = True
    conversation_area.insert(END, "AKG: Conversation ended manually. Goodbye!\n")
    speak("Conversation ended manually. Goodbye!")
    root.quit()

# GUI Setup with ttkbootstrap
root = ttk.Window(themename="darkly")
root.title("A-K-G Assistant")
root.geometry("600x500")

conversation_area = ScrolledText(root, wrap="word", width=70, height=20, font=("Consolas", 12))
conversation_area.pack(padx=10, pady=10)

start_button = ttk.Button(root, text="Start Conversation", bootstyle="success", command=start_conversation)
start_button.pack(pady=5)

end_button = ttk.Button(root, text="End Conversation", bootstyle="danger", command=end_conversation)
end_button.pack(pady=5)

root.mainloop()
