import PySimpleGUI as sg


layout = [
    [sg.Text(text="Hello", font=('Calibri', 20), expand_x=True, background_color=('#008DDA'), colors='#F7EEDD', justification='center', enable_events=True , key='-TEXT-')],
    [sg.Canvas(size=(0, 425), background_color='white', pad=35, expand_x=True, key='-CANVAS-')],
    [sg.Text(text="Tap anywhere to start", font=('Calibri', 15), expand_x=True, background_color=('#008DDA'), justification='center')],
    [sg.Text(text="or Say \"Start Order\" for Speech Option", font=('Calibri', 15), expand_x=True, background_color=('#008DDA'), justification='center')]
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

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == '-TEXT-':
        switch_window()
        print("Switched")

window.close()
