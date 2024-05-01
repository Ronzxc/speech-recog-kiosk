import tkinter as tk
from gtts import gTTS
import pygame
from io import BytesIO
from tkinter import messagebox
import speech_recognition as sr


def convert_text_to_speech():
    tts = gTTS(text="mama", lang="en")
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()


def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))


class AppLogic:
    def __init__(self, app):
        self.app = app

    def on_button_click(self):
        convert_speech_to_text()
        # convert_text_to_speech()
        # messagebox.showinfo("Message", "Button clicked!")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Order Taking App")
        self.geometry("400x300")
        
        self.app_logic = AppLogic(self)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(self, text="Click Me", command=self.app_logic.on_button_click)
        self.button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
