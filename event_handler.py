from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr
import PySimpleGUI as sg
import utils    
import time

import menu_item as menu

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
# VIEW_ORDER = """You said view order. Say Modify to modify your order, Checkout to proceed to payment, 
#                 Exit to cancel transaction or Back to go back to menu"""
EXIT_APP = "You said exit. Hope to see you again soon."
MODIFY_OPTIONS = "Say change to change quantity or delete to delete item from cart"


def get_cart_list(cart):
    prompt = "You said view order. Your orders are "
    orders = ""
    for k, v in cart.items():
        orders = orders + f"{v} {k[0]}, "
    
    prompt = f"{prompt} {orders}. Say Modify to modify your order, Checkout to proceed to payment, Exit to cancel transaction or Back to go back to menu"
    
    return prompt
    


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

menu_map = {menu.chicken: "chicken", menu.burgersteak: "burger", menu.burger: "cheese", menu.fries: "fries"}


def modify_order(window=None, cart=dict()):
    timeout = len(cart.keys()) + 5
    orders = ""
    prompt = "You said modify order. Select the order you want to modify: Say"

    for k, v in cart.items():
        name = menu_map[k]
        orders = orders + f" {name} for {v} {k[0]}, "
    
    prompt = prompt + orders
    utils.kiosk_prompt(prompt)
    time.sleep(timeout)
    window.write_event_value(('-MODIFY THREAD-', 'FINISHED PROMPT'), 'FINISHED PROMPT')

def get_modify_command(window=None, *args):
    while True:
        command = str(utils.speech_to_text()).upper()
        print(command.upper())
        if command in args:
            window.write_event_value(('-MODIFY THREAD-', command), command)
            break

    


