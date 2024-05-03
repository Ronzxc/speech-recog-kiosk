import PySimpleGUI as sg
import event_handler as eh

# menu
import menu_item as menu
ricemeals = [menu.chicken, menu.burgersteak]
othermeals = [menu.burger, menu.fries]


# data to be manipulated
cart = {menu.chicken: 1} #format {menu.item1: qty, menu.item2: qty}
temp_item = None
temp_qty = 0


#Layout for order menu
layout_tab1 = [[sg.Text('Content for Tab 1', background_color=('#FF8A08'))],
               [sg.Column([
        [sg.Image(filename=menu.chicken[1], size=(75, 75), pad=10), sg.Image(filename=menu.burgersteak[1], size=(75, 75))]
    ], justification='center', background_color='#FFC100')]]
layout_tab2 = [[sg.Text('Content for Tab 2', background_color=('#FF8A08'))],
               [sg.Column([
        [sg.Image(filename=menu.burger[1], size=(75, 75), pad=10), sg.Image(filename=menu.fries[1], size=(75, 75))]
    ], justification='center', background_color='#FFC100')]]


tab1 = sg.Tab('RICEMEALS', layout_tab1, title_color='red', background_color=('#FF8A08'))
tab2 = sg.Tab('OTHERMEALS', layout_tab2, title_color='green', background_color=('#FF8A08'))



tab_group_layout = [[tab1, tab2]]

tab_group = sg.TabGroup(tab_group_layout, tab_location='left', title_color='white', size=(400, 525), pad= 10, background_color=('#FF6500'))

order_menu_layout = [[sg.Text(text="Pick a Category", 
                    expand_x=True,
                    justification='center',
                    background_color=('#C40C0C'))],
                    [sg.Column([[tab_group]], background_color='#FF6500')]]

#-LISTEN2-
dine_take_layout = [[sg.Text(text="Dine-in or Take-out", 
                    expand_x=True,
                    justification='center',
                    background_color=('#C40C0C'))],
                    [sg.Button('DINE IN',
                    font=('Calibri', 15), 
                    expand_x=True, 
                    button_color=('#C40C0C'),
                    key = ('-THREAD-', 'DINE OR TAKE'),
                    enable_events=True)],
                    [sg.Button('TAKE OUT',
                    font=('Calibri', 15), 
                    expand_x=True, 
                    button_color=('#C40C0C'),
                    key = ('-THREAD-', 'DINE OR TAKE'), 
                    enable_events=True)],
                    [sg.Image(filename='images/bini.png', 
              size=(0,525))],
                    ]


modify_layout = [[sg.Text(text="Modify your order", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]

confirm_layout = [[sg.Text(text="Confirm Delete", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]

check_order_layout = [[sg.Text(text="Check your Order before we proceed", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]

processed_layout = [[sg.Text(text="Your order have been processed", 
                    expand_x=True,
                    justification='center',
                    background_color=('#C40C0C'))],
                    ]


ask_qty_layout = [[sg.Text(text="How many?", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]

cart_layout = [[sg.Text(text="Cart", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]


checkout_layout = [[sg.Text(text="CHECKOUT", 

                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    ]

#Layout for speech 1
speech1_layout = [[]]


home_layout = [
    [sg.Text(text="Hello RotttedBrain!", 
             font=('Calibri', 20), 
             expand_x=True, 
             background_color=('#C40C0C'), 
             colors='#F7EEDD', 
             justification='center', 
             enable_events=True , 
             key='-TEXT-')],
    [sg.Image(filename='images/home.png',
              size=(0,425))],
    [sg.Button('Start Order',
             font=('Calibri', 15), 
             expand_x=True,
             button_color=('#C40C0C'),
             key = ('-THREAD-', 'CHECKOUT'),
             enable_events=True)],
    [sg.Text(text="or Say \"Start Order\" for Speech Option", 
             font=('Calibri', 15), 
             expand_x=True, 
             background_color=('#C40C0C'), 
             justification='center')],
    [sg.Text(text="", font=('Calibri', 15), 
             expand_x=True, 
             background_color=('#FF8A08'),
             justification='center')],
]

main_layout = [
            [sg.Column(home_layout, key= '-LISTEN1-'), 
             sg.Column(dine_take_layout, visible=False, key='-LISTEN2-'),
             sg.Column(order_menu_layout, visible=False, key='-LISTEN3-'),
             sg.Column(ask_qty_layout, visible=False, key='-LISTEN4-'),

             sg.Column(cart_layout, visible=False, key='-LISTEN5-'),

             sg.Column(checkout_layout, visible=False, key='-LISTEN6-'),
             ]]

    
sg.theme_background_color('#FF8A08')
window = sg.Window('Speech \'o Order', main_layout, size=(360, 640))

layout_num = 1
window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))


while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event[0] == '-MODIFY THREAD-':
        if event[1] == 'FINISHED PROMPT':
            window.start_thread(lambda: eh.get_command(window, "CHICKEN", "BURGER", "FRIES", "CHEESE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")
        
        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE"]:
            match event[1]:
                case "CHICKEN":
                    #RONWALDO KINDLY CHANGE UI
                    window['-LISTEN1-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                    temp_item = menu.chicken
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify your Chicken Joy order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), ('-THREAD-', '-THREAD ENDED-'))

                case "BURGER":
                    #RONWALDO KINDLY CHANGE UI
                    window['-LISTEN1-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                    temp_item = menu.burgersteak
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Burger Steak order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), ('-THREAD-', '-THREAD ENDED-'))


                case "FRIES":
                    #RONWALDO KINDLY CHANGE UI
                    window['-LISTEN1-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                    temp_item = menu.fries
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify French Fries order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), ('-THREAD-', '-THREAD ENDED-'))


                case "CHEESE":
                    #RONWALDO KINDLY CHANGE UI
                    window['-LISTEN1-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                    temp_item = menu.burger
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Cheese Burger order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), ('-THREAD-', '-THREAD ENDED-'))
      
                    


    elif event[0] == '-THREAD-':
        if event[1] == 'DONE START':
            window.start_thread(lambda: eh.get_command(window, "START ORDER"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")
    
        elif event[1] == 'START ORDER' or event == 'START ORDER':
            # RONWALDO UPDATE MO UI HERE
            window[f'-LISTEN{layout_num}-'].update(visible=False)
            layout_num = 2
            window[f'-LISTEN{layout_num}-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.WELCOME, 7, 'DINE OR TAKE'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == 'DINE OR TAKE':
            window.start_thread(lambda: eh.get_command(window, "DINE IN", "TAKE OUT"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")

        elif event[1] == 'DINE IN' or event[1] == 'TAKE OUT':
            # RONWALDO UPDATE MO UI HERE
            window[f'-LISTEN{layout_num}-'].update(visible=False)
            layout_num = 3
            window[f'-LISTEN{layout_num}-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_CHOICE + event[1] + "." + eh.CATEGORIES, 11, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "CATEGORY":
            window.start_thread(lambda: eh.get_command(window, "RICE", "OTHERS", "VIEW ORDERS"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")

        elif event[1] == "RICE" or event[1] == "OTHERS":
            if event[1] == "RICE":
                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("change to speech 6 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                window.start_thread(lambda: eh.start_assist(window, eh.RICE_MENU, 5, 'RICE_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "OTHERS":
                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("change to speech 6 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

                window.start_thread(lambda: eh.start_assist(window, eh.OTHER_MENU, 5, 'OTHER_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "RICE_CATEGORY" or event[1] == "OTHER_CATEGORY":
            if event[1] == "RICE_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "CHICKEN", "BURGER"), ('-THREAD-', '-THREAD ENDED-'))
            elif event[1] == "OTHER_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "FRIES", "CHEESE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")


        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE", "CHANGE"]:
            if event[1] == "CHICKEN":
                temp_item = menu.chicken

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("speech 9: chicken") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "BURGER":
                temp_item = menu.burgersteak

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("speech 9: burger steak") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            elif event[1] == "FRIES":
                temp_item = menu.fries

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("speech 9: french fries") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "CHEESE":
                temp_item = menu.burger

                # RONWALDO UPDATE MO UI HERE
                window['-LISTEN1-'].update("speech 9: cheese burger") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.ASK_QTY, 3, 'ASK QTY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "ASK QTY":
            window.start_thread(lambda: eh.get_command(window, *eh.ALLOWED_QTY), ('-THREAD-', '-THREAD ENDED-'))
            window[f'-LISTEN{layout_num}-'].update(visible=False)
            layout_num = 4
            window[f'-LISTEN{layout_num}-'].update(visible=True)


        elif event[1] in eh.ALLOWED_QTY:
            temp_qty = eh.ALLOWED_QTY.index(event[1]) + 1

            # RONWALDO UPDATE MO UI HERE
            # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ITEM, 5, 'CONFIRM ITEM'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "CONFIRM ITEM":
            window.start_thread(lambda: eh.get_command(window, "ADD TO CART", "CANCEL ITEM"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")

        
        elif event[1] in ["ADD TO CART", "CANCEL ITEM", "BACK"]:
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN1-'].update("change to speech 4 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            
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
            window['-LISTEN1-'].update("change to speech 12 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            timeout = len(cart.keys()) + 10
            window.start_thread(lambda: eh.start_assist(window, eh.get_cart_list(cart), timeout, 'ORDER ACTION'), ('-THREAD-', '-THREAD ENDED-'))
            
            window[f'-LISTEN{layout_num}-'].update(visible=False)
            layout_num = 5
            window[f'-LISTEN{layout_num}-'].update(visible=True)
            
            
            

        elif event[1] == "ORDER ACTION":
            window.start_thread(lambda: eh.get_command(window, "MODIFY", "CHECKOUT", "EXIT", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")


        elif event[1] == "MODIFY":
            window['-LISTEN1-'].update("change to speech 12 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
        
            window.start_thread(lambda: eh.modify_order(window, cart), ('-MODIFY THREAD-', '-MODIFY THREAD ENDED-'))


        elif event[1] == "MODIFY OPTION":
            window.start_thread(lambda: eh.get_command(window, "CHANGE", "DELETE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-LISTEN1-'].update("Listening...")

        
        elif event[1] == "CHECKOUT":
            # HELLO GEO
            window.start_thread(lambda: eh.prompt_check_out_menu(cart, window),('-THREAD-', '-THREAD ENDED-'))
            window[f'-LISTEN{layout_num}-'].update(visible=False)
            layout_num = 6
            window[f'-LISTEN{layout_num}-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.get_command(window, "START ORDER"), ('-THREAD-', '-THREAD ENDED-'))
        
        
        elif event[1] == "DONE CHECKOUT":
            window.start_thread(lambda: eh.get_command(window, "CONFIRM ORDER", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "CONFIRM ORDER":
            window.start_thread(lambda: eh.start_assist(window, eh.FINISHED_CHECKOUT, 10, 'EXIT_APP'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "EXIT":
            # RONWALDO UPDATE MO UI HERE
            window['-LISTEN1-'].update("change to speech 20 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.EXIT_APP, 6, 'EXIT APP'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "EXIT APP":
            break


        


    elif event == '-TEXT-':
        eh.kiosk_prompt()
        # switch_window()
        # print("Switched")

window.close()
