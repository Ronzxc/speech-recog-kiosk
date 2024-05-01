from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr
import PySimpleGUI as sg


# text to speech and speech to text functions
def kiosk_prompt(prompt="hello"):
    tts = gTTS(text=prompt, lang="en")
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return None
