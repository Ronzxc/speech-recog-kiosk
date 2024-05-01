from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr
import PySimpleGUI as sg
import utils    
import time


# prompts
START_PROMPT = "Tap anywhere to start, or Say Start Order for Speech Option"
WELCOME = "Hello, I'm BINI Aiah. I'm glad to assist you today. Would you like to dine in or take out"


def get_command(window=None, *args):
    while True:
        command = str(utils.speech_to_text()).upper()
        print(command.upper())
        if command in args:
            window.write_event_value(('-THREAD-', command), command)
            break


def start_assist(window=None, prompt="Hello", timeout=1, key=None):
    utils.kiosk_prompt(prompt)
    time.sleep(timeout)
    window.write_event_value(('-THREAD-', key), key)




