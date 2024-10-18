import speech_recognition as sr
import pyttsx3
import sys
import time, datetime
import webbrowser
import playsound
import os
import random
from gtts import gTTS


recognizer = sr.Recognizer()
#mic_phone =

def alexis_speak(string_text):
    """Convert text to speech."""
    tts = gTTS(text=string_text,lang='en')
    sr = random.randint(1,10000000)
    text_audio ="audio-"+ str(sr)+ ".mp3"
    tts.save(text_audio)
    playsound.playsound(text_audio)
    print(string_text)
    os.remove(text_audio)


def audio_listen(ask=False):
    with  sr.Microphone() as source:
            if ask:
                alexis_speak(ask)
                print(ask)
            voice = recognizer.listen(source)
            query= ''
            try:
                query = recognizer.recognize_google(voice)
                alexis_speak(f"You said: {query}")   
            except sr.RequestError:
                alexis_speak("Sorry, there was an issue with the speech service.")
               
            except sr.UnknownValueError:
                alexis_speak("Sorry, I did not understand that.")
            return query.lower()
            
def audio_response(query):
     """Commands will be Executed, based on user input."""
     if 'google' in query:
        alexis_speak("Opening Google")
        webbrowser.open("https://www.google.com")
     if 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        alexis_speak(f"The current time is {current_time}.")
     if 'search' in query:
        search=audio_listen("What do you want to search?")
        url= 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
     if 'exit' in query or 'bye' in query:
        alexis_speak("Goodbye!")
        sys.exit()

time.sleep(1)
alexis_speak("Your personal voice assistant here, how can I assist you?")
while(1):  
    print("Try saying something...")
    query =audio_listen()
    audio_response(query)


#def record_audio()
#def rspond(voice_data)