# python3 -m venv venv to create a virtual environment
# source venv/bin/activate   -- to activate
# pip install speechrecognition
# pip install pyaudio
# pip install gTTS
# pip install playsound
# pip install PyObjC

import speech_recognition as sr
import time
import os
import playsound
import random
import webbrowser
from time import ctime
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            jo_speak(ask)
        audio = r.listen(source)
        voice_data = " "
        try:
            voice_data = r.recognize_google(audio)
            # print(voice_data)
        except sr.UnknownValueError:
            jo_speak("Sorry, didnt get that")
        except sr.RequestError:
            jo_speak("Sorry, my speech service is down")
        return voice_data
    
def jo_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = "audo-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "What is your name" in voice_data:
        jo_speak("My name is Jo")
    if "what time is it" in voice_data:
        jo_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        jo_speak("Here is what i found for " + search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp"
        webbrowser.get().open(url)
        jo_speak("Here is the location of " + location)
    if "exit" in voice_data:
        exit()


time.sleep(1)
jo_speak("How can i help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
# print(voice_data)
