from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr
import PySimpleGUI as sg
import utils    
import time

import menu_item as menu
ricemeals = [None, menu.chicken, menu.burgersteak]
othermeals = [None, menu.burger, menu.fries]

ALLOWED_QTY = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]

# prompts
START_PROMPT = "Tap anywhere to start, or Say Start Order for Speech Option"
WELCOME = "Hello, I'm Beanie Aiah. I'm glad to assist you today. Would you like to dine in or take out"
CONFIRM_CHOICE = "You chose "
CATEGORIES = """""To view specific category, say Rice for Rice meals and Others for Other meals.
                    Or if you like to view your orders say view orders"""
RICE_MENU = "You chose rice meals. Say chicken for chicken joy and burger for burger steak"
OTHER_MENU = "You chose other meals. Say cheese for cheese burger and fries for french fries"
ASK_QTY = "How many would you like to order?"
CONFIRM_ITEM = "Say add to cart to confirm item and quantity or cancel item to go back to categories"
CONFIRM_ADD = "Item added to cart"
VIEW_ORDER = """You said view order. Say Modify to modify your order, Checkout to proceed to payment, 
                Exit to cancel transaction or Back to go back to menu"""
EXIT_APP = "You said exit. Hope to see you again soon."

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


def prompt_check_out_menu(cart, window=None):
    orders = ""
    for keys, value in cart.items():
        orders = orders + f" {value} {keys[0]},"
    # print(orders)
    # if(cart.size() == 1)
    if(len(cart.items()) == 1 and list(cart.items())[0][1] == 1):
        utils.kiosk_prompt(f"Your check out item is: {orders}")
    else:
<<<<<<< HEAD
        utils.kiosk_prompt(f"Your check out items are: {orders} Say Confirm to print payment reference or Cancel to go back to menu")
=======
        utils.kiosk_prompt(f"Your check out items are: {orders}")

>>>>>>> gui
    window.write_event_value(('-CHECKOUT THREAD-', 'DONE CHECKOUT'), 'DONE CHECKOUT')
    
