import speech_recognition as S
import pyttsx3 as tx
from decouple import config
from datetime import datetime as D
from convo import Rand_txt as R
from random import choice as C
import keyboard as Keyb
import os
import subprocess as sb
from onlinethings import findip, SearchonGoogle, Searchwiki, youtubevid

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
        except S.UnknownValueError:
            Speak("Sorry, I did not catch that. Could you please repeat?")
            return None
        except S.RequestError:
            Speak("Sorry, I'm having trouble connecting to the service. Please check your internet connection.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            Speak(f"Sorry, something went wrong. Please try again.")
            return None
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
                Speak("Opening Notepad sir!")
                n_pad = "c:\\windows\\notepad.exe"
                os.startfile(n_pad)
            elif "open vscode" in query or "open vs code" in query:
                Speak("Opening VSCode sir!")
                w_app = "C:\\Users\\Mugeish\\OneDrive\\Desktop\\Visual Studio Code.lnk"
                os.startfile(w_app)
            elif "open a game" in query or "play a game" in query:
                Speak("Opening a game sir!")
                S_app = "C:\\Users\\Public\\Desktop\\Play Ghost of Tsushima.lnk"
                os.startfile(S_app)
            elif "ip address" in query or "my ip" in query:
                ip = findip()
                if ip:
                    Speak(f'Your IP is {ip}, sir')
                else:
                    Speak("Sorry, I couldn't retrieve your IP address.")
            elif "youtube" in query or "play on youtube" in query:
                Speak('What do you want me to play, sir?')
                Vid = RecSpeech()
                if Vid:
                    youtubevid(Vid.lower())
            elif "google" in query or "search on google" in query:
                Speak("What do you want me to search on Google, sir?")
                prt = RecSpeech()
                if prt:
                    SearchonGoogle(prt.lower())
            elif "wikipedia" in query or "search on wikipedia" in query:
                Speak("What do you want me to search on Wikipedia, sir?")
                prt = RecSpeech()
                if prt:
                    R = Searchwiki(prt.lower())
                    if R:
                        Speak(f'According to Wikipedia, {R}')
                    else:
                        Speak("Sorry, I couldn't find any information on Wikipedia.")
            elif "stop listening goose" in query or "stop" in query or "exit" in query:
                Speak("Fine Sir, Bye!")
                break
            else:
                Speak("Sorry, I didn't understand that. Could you please repeat or try a different command?")
