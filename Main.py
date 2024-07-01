import speech_recognition as S
import pyttsx3 as tx
from decouple import config
from datetime import datetime as D
from convo import Rand_txt as R
from random import choice as C
import keyboard as Keyb
import os
import subprocess as sb

engine = tx.init('sapi5')
engine.setProperty('volume', 2.5)
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

User = config('User')
Host = config('Bot')

def RecSpeech():
    recognizer = S.Recognizer()
    with S.Microphone() as source:
        print(f"Listening {User}")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio, language='en-in')
            print(query)
            if not ('stop' in query or 'exit' in query):
                Speak(C(R))
            else:
                hour = D.now().hour
                if 21 <= hour < 6:
                    Speak(f"Good Night {User}, hear you tomorrow")
                else:
                    Speak(f"Have a good day! {User}")
                exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            Speak(f"Sorry, comeback again {User}")
            query = None
        return query

listening = False

def Srt_List():
    global listening
    listening = True
    print("Started Listening!")

def Stp_List():
    global listening
    listening = False
    print("Ok sir, let me wait!")

Keyb.add_hotkey('ctrl+w', Srt_List)
Keyb.add_hotkey('ctrl+s', Stp_List)

def Speak(text):
    engine.say(text)
    engine.runAndWait()
    return text

def initgreet():
    hour = D.now().hour
    if 6 <= hour <= 12:
        Speak(f"Good Morning {User}, how can I help you!")
    elif 12 <= hour <= 16:
        Speak(f"Good Afternoon {User}, how can I help you!")
    else:
        Speak(f"Good Evening {User}, how can I help you!")
    Speak(f'I am {Host}!')

initgreet()

while True:
    if listening:
        query = RecSpeech()
        if query:
            query = query.lower()
            if "how are you" in query:
                Speak(f"I am fine, how about you, sir {User}")
            elif "open command prompt" in query or "open cmd" in query:
                Speak("Opening Command prompt sir!")
                os.system('start cmd')
            elif "open camera" in query:
                Speak("Opening Camera sir!")
                sb.run('start microsoft.windows.camera:', shell=True)
            elif "open notepad" in query or "notepad" in query:
                Speak("Opening NotePad sir!")
                n_pad = "c:\\windows\\notepad.exe"
                os.startfile(n_pad)
            elif "open whatsapp beta" in query or "whatsapp" in query:
                Speak("Opening Whatsapp sir!")
                w_app = "whatsapp:\\chat\\?code=ItJpMyA3l9EJ80vZtW7T4C"
                os.startfile(w_app)
            elif "knox goose" in query:
                Speak("Fine Sir, Bye!")
                break
