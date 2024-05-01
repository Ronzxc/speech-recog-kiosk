import PySimpleGUI as sg
import event_handler as eh

# menu
import menu_item as menu
ricemeals = [None, menu.chicken, menu.burgersteak]
othermeals = [None, menu.burger, menu.fries]


# data to be manipulated
cart = [] #format [[menu_item, qty],[menu_item, qty]] example: [[menu.chicken, 2], [menu.fries, 1]]


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
            window['-LISTEN-'].update("Listening...")
            window.start_thread(lambda: eh.get_command(window, "START ORDER"), ('-THREAD-', '-THREAD ENDED-'))
    
        elif event[1] == 'START ORDER':
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN-'].update(event[1]) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED


            window.start_thread(lambda: eh.start_assist(window, eh.WELCOME, 8, 'DINE OR TAKE'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == 'DINE OR TAKE':
            window['-LISTEN-'].update("Listening...")
            window.start_thread(lambda: eh.get_command(window, "DINE IN", "TAKE OUT"), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == 'DINE IN' or event[1] == 'TAKE OUT':
            window['-LISTEN-'].update(event[1])


    elif event == '-TEXT-':
        eh.kiosk_prompt()
        # switch_window()
        # print("Switched")

window.close()
