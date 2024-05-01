import PySimpleGUI as sg
import event_handler as eh

# menu
import menu_item as menu
ricemeals = [menu.chicken, menu.burgersteak]
othermeals = [menu.burger, menu.fries]


# data to be manipulated
cart = {} #format {menu.item1: qty, menu.item2: qty}
temp_item = None
temp_qty = 0


layout = [
    [sg.Text(text="Hello", font=('Calibri', 20), expand_x=True, background_color=('#008DDA'), colors='#F7EEDD', justification='center', enable_events=True , key='-TEXT-')],
    [sg.Image(filename='images\\home.png', size=(0,425))],
    [sg.Text(text="Tap anywhere to start", font=('Calibri', 15), expand_x=True, background_color=('#008DDA'), justification='center')],
    [sg.Text(text="or Say \"Start Order\" for Speech Option", font=('Calibri', 15), expand_x=True, background_color=('#008DDA'), justification='center')],
    [sg.Text(text="", font=('Calibri', 15), expand_x=True, background_color=('#008DDA'), justification='center', key='-LISTEN-')],
]

    
sg.theme_background_color('#008DDA')
window = sg.Window('Speech \'o Order', layout, size=(360, 640))



def switch_window():
    new_layout = [[sg.Text('New Window')],
                  [sg.Canvas(size=(0, 425), background_color='white', pad=35, expand_x=True, key='-CANVAS-')]]
    sg.theme_background_color('#008DDA')
    new_window = sg.Window('Speech \'o Order', new_layout, size=(360, 640))
    while True:
        event, values = new_window.read()
        if event in (None, 'Exit'):
            break
    new_window.close()


window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event[0] == '-THREAD-':
        if event[1] == 'DONE START':
            window.start_thread(lambda: eh.get_command(window, "START ORDER"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")
    
        elif event[1] == 'START ORDER':
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update("change to speech 1 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED


            window.start_thread(lambda: eh.start_assist(window, eh.WELCOME, 7, 'DINE OR TAKE'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == 'DINE OR TAKE':
            window.start_thread(lambda: eh.get_command(window, "DINE IN", "TAKE OUT"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")

        elif event[1] == 'DINE IN' or event[1] == 'TAKE OUT':
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update("change to speech 4 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_CHOICE + event[1] + "." + eh.CATEGORIES, 11, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "CATEGORY":
            window.start_thread(lambda: eh.get_command(window, "RICE", "OTHERS", "VIEW ORDERS"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")

        elif event[1] == "RICE" or event[1] == "OTHERS":
            if event[1] == "RICE":
                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("change to speech 6 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                window.start_thread(lambda: eh.start_assist(window, eh.RICE_MENU, 5, 'RICE_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "OTHERS":
                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("change to speech 6 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                window.start_thread(lambda: eh.start_assist(window, eh.OTHER_MENU, 5, 'OTHER_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "RICE_CATEGORY" or event[1] == "OTHER_CATEGORY":
            if event[1] == "RICE_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "CHICKEN", "BURGER"), ('-THREAD-', '-THREAD ENDED-'))
            elif event[1] == "OTHER_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "FRIES", "CHEESE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")


        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE"]:
            if event[1] == "CHICKEN":
                temp_item = menu.chicken

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("speech 9: chicken") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "BURGER":
                temp_item = menu.burgersteak

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("speech 9: burger steak") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            elif event[1] == "FRIES":
                temp_item = menu.fries

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("speech 9: french fries") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "CHEESE":
                temp_item = menu.burger

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN-'].update("speech 9: cheese burger") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.ASK_QTY, 3, 'ASK QTY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "ASK QTY":
            window.start_thread(lambda: eh.get_command(window, *eh.ALLOWED_QTY), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")

        elif event[1] in eh.ALLOWED_QTY:
            temp_qty = eh.ALLOWED_QTY.index(event[1]) + 1

            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update(f"speech 11: {event[1]}") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ITEM, 5, 'CONFIRM ITEM'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "CONFIRM ITEM":
            window.start_thread(lambda: eh.get_command(window, "ADD TO CART", "CANCEL ITEM"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")

        
        elif event[1] in ["ADD TO CART", "CANCEL ITEM", "BACK"]:
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update("change to speech 4 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            
            if event[1] == "ADD TO CART":
                cart[temp_item] = temp_qty
                print(cart)
                window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ADD + ". " + eh.CATEGORIES, 10, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "CANCEL ITEM" or event[1] == "BACK":
                window.start_thread(lambda: eh.start_assist(window, eh.CATEGORIES, 7, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            temp_item = None
            temp_qty = 0
            print(f"{temp_item}: {temp_qty}")

        
        elif event[1] == "VIEW ORDERS":
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update("change to speech 12 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.VIEW_ORDER, 10, 'ORDER ACTION'), ('-THREAD-', '-THREAD ENDED-'))
            

        elif event[1] == "ORDER ACTION":
            window.start_thread(lambda: eh.get_command(window, "MODIFY", "CHECKOUT", "EXIT", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN-'].update("Listening...")


        elif event[1] == "MODIFY":
            # HELLO GEO
            pass
            
        
        elif event[1] == "CHECKOUT":
            # HELLO GEO
            pass
        
        
        elif event[1] == "EXIT":
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update("change to speech 20 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.EXIT_APP, 6, 'EXIT APP'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "EXIT APP":
            break


    elif event == '-TEXT-':
        eh.kiosk_prompt()
        # switch_window()
        # print("Switched")

window.close()
