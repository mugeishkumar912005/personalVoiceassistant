import requests as rq
import wikipedia as wiki
import pywhatkit as pwk

def findip():
    try:
        ip = rq.get('https://api.ipify.org?format=json').json()
        return ip['ip']
    except Exception as e:
        print(f"Error finding IP: {e}")
        return None

def Searchwiki(query):
    try:
        print(f"Searching Wikipedia for: {query}")
        s_Res = wiki.summary(query, sentences=2)
        return s_Res
    except Exception as e:
        print(f"Error searching Wikipedia: {e}")
        return None

def SearchonGoogle(query):
    try:
        print(f"Searching Google for: {query}")
        pwk.search(query)
    except Exception as e:
        print(f"Error searching Google: {e}")

def youtubevid(video):
    try:
        print(f"Playing YouTube video for: {video}")
        pwk.playonyt(video)
    except Exception as e:
        print(f"Error playing YouTube video: {e}")