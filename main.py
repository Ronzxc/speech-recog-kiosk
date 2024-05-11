import PySimpleGUI as sg
import event_handler as eh
from PIL import Image, ImageTk
# menu
import menu_item as menu
ricemeals = [menu.chicken, menu.burgersteak]
othermeals = [menu.burger, menu.fries]

# data to be manipulated
cart = {menu.chicken: 1, menu.burgersteak: 3} #format {menu.item1: qty, menu.item2: qty}
temp_item = None
temp_qty = 0


#Layout for order menu


layout_tab1 = [[sg.Text('Content for Tab 1', background_color=('#FF8A08'))],
               [sg.Column([
        [sg.Image(filename=menu.chicken[1], size=(75, 75), pad=10, background_color='#FFC100'), 
         sg.Image(filename=menu.burgersteak[1], size=(75, 75), background_color='#FFC100')]
    ], justification='center', background_color='#FFC100')]]
layout_tab2 = [[sg.Text('Content for Tab 2', background_color=('#FF8A08'))],
               [sg.Column([
        [sg.Image(filename=menu.burger[1], size=(75, 75), pad=10, background_color='#FFC100' ), 
         sg.Image(filename=menu.fries[1], size=(75, 75), background_color='#FFC100')]
    ], justification='center', background_color='#FFC100')]]


tab1 = sg.Tab('🍚', layout_tab1, background_color=('#FF8A08'))
tab2 = sg.Tab('🍔', layout_tab2, background_color=('#FF8A08'))



tab_group_layout = [[tab1, tab2]]

tab_group = sg.TabGroup(tab_group_layout, tab_location='left', title_color='black', size=(400, 525), pad= 10, background_color=('#FF8A08'), tab_background_color='#FF8A08', selected_title_color='#C40C0C', selected_background_color='Yellow', font=100 )

order_menu_layout = [[sg.Text(text="Pick a Category", 
                    expand_x=True,
                    justification='center',
                    background_color=('#C40C0C'))],
                    [sg.Column([[tab_group]], background_color='#FF6500')]]

#-LISTEN2-
dine_take_layout = [[sg.Image(filename='images/bini.png', 
              size=(0,525))]
                    ]


modify_layout = [[sg.Text(text="Modify your order", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                 [sg.Frame('', layout=[
                            [sg.Text('Content inside the frame', justification='center')],
                            [sg.Button('Button inside the frame')]
                    ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
                    ]

confirm_layout = [[sg.Text(text="Confirm Delete", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                  [sg.Frame('', layout=[
                            [sg.Text('Content inside the frame', justification='center')],
                            [sg.Button('Button inside the frame')]
                    ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
                    ]

check_order_layout = [[sg.Text(text="Check your Order before we proceed", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                    [sg.Frame('', layout=[
                            [sg.Text('Content inside the frame', justification='center')],
                            [sg.Button('Button inside the frame')]
                    ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
                    ]

processed_layout = [[sg.Text(text="Your order have been processed", 
                    expand_x=True,
                    justification='center',
                    background_color=('#C40C0C'))],
                    [sg.Frame('', layout=[
                            [sg.Text('Content inside the frame', justification='center')],
                            [sg.Button('Button inside the frame')]
                    ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
                    ]


ask_qty_layout = [[sg.Text(text="How many?", 
                    expand_x=True,
                    justification='center',
                    background_color=('#FF8A08'))],
                  [sg.Frame('', layout=[
                            [sg.Text('Content inside the frame', justification='center')],
                            [sg.Button('Button inside the frame')]
                    ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
                    ]


layout_column = sg.Column([], key='-COLUMN-', expand_x=True)
items_layout = []
for item, qty in cart.items():
    items_layout.append([sg.Image(filename=item[1], size=(75, 75), pad=10),
                         sg.Text(f"{item[0]} x{qty}")])

cart_layout = [
    [sg.Text("Cart", expand_x=True, justification='center', background_color='#FF8A08')],
    [sg.Frame('', layout=[[sg.Column(items_layout, key='-COLUMN-', expand_x=True)]], background_color='#FF6500', expand_x=True, size=(400, 525))]
]
# layout_column.update(items_layout)

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
             enable_events=False)],
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
            [sg.Column(home_layout, key= '-HOME_LAYOUT-'), #CHANGE BACK TO home_layout  
             sg.Column(dine_take_layout, visible=False, key='-DINE_TAKE_LAYOUT-'),
             sg.Column(order_menu_layout, visible=False, key='-ORDER_MENU_LAYOUT-'),
             sg.Column(ask_qty_layout, visible=False, key='-ASK_QTY_LAYOUT-'),
             sg.Column(cart_layout, visible=False, key='-CART_LAYOUT-'), #CHANGE BACK
             sg.Column(check_order_layout, visible=False, key='-CHECK_ORDER_LAYOUT-'),
             sg.Column(processed_layout, visible=False, key='-PROCESSED_LAYOUT-'),
             sg.Column(confirm_layout, visible=False, key='-CONFIRM_LAYOUT-'),
             sg.Column(modify_layout, visible=False, key='-MODIFY_LAYOUT-'),
             ]]

    
sg.theme_background_color('#FF8A08')
window = sg.Window('Speech \'o Order', main_layout, size=(360, 640))

window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))


while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event[0] == '-MODIFY THREAD-':
        if event[1] == 'FINISHED PROMPT':
            window.start_thread(lambda: eh.get_command(window, "CHICKEN", "BURGER", "FRIES", "CHEESE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-HOME_LAYOUT-'].update("Listening...")

        
        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE"]:
            match event[1]:
                case "CHICKEN":
                    #RONWALDO KINDLY CHANGE UI
                    window['-MODIFY_LAYOUT-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
                    temp_item = menu.chicken
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify your Chicken Joy order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
                case "BURGER":
                    #RONWALDO KINDLY CHANGE UI
                    window['-MODIFY_LAYOUT-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
                    temp_item = menu.burgersteak
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Burger Steak order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
                case "FRIES":
                    #RONWALDO KINDLY CHANGE UI
                    window['-MODIFY_LAYOUT-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
                    temp_item = menu.fries
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify French Fries order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'),) 
                case "CHEESE":
                    #RONWALDO KINDLY CHANGE UI
                    window['-MODIFY_LAYOUT-'].update("change to speech 14 gui (see figma for ref)") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
                    temp_item = menu.burger
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Cheese Burger order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
      


    elif event[0] == '-THREAD-':
        if event[1] == 'DONE START':
            window.start_thread(lambda: eh.get_command(window, "START ORDER"), ('-THREAD-', '-THREAD ENDED-'))
    
        elif event[1] == 'START ORDER':
            # RONWALDO UPDATE MO UI HERE
            window.refresh()
            window[f'-HOME_LAYOUT-'].update(visible=False)
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.WELCOME, 7, 'DINE OR TAKE'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == 'DINE OR TAKE':
            window.start_thread(lambda: eh.get_command(window, "DINE IN", "TAKE OUT"), ('-THREAD-', '-THREAD ENDED-'))
            window['-DINE_TAKE_LAYOUT-'].update("Listening...")

        elif event[1] == 'DINE IN' or event[1] == 'TAKE OUT':
            # RONWALDO UPDATE MO UI HERE
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=False)
            window[f'-ORDER_MENU_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_CHOICE + event[1] + "." + eh.CATEGORIES, 11, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "CATEGORY":
            window.start_thread(lambda: eh.get_command(window, "RICE", "OTHERS", "VIEW ORDERS"), ('-THREAD-', '-THREAD ENDED-'))
            window['-ORDER_MENU_LAYOUT-'].update("Listening...")

        elif event[1] == "RICE" or event[1] == "OTHERS":
            if event[1] == "RICE":
                window['RICEMEALS'].select()
                window.start_thread(lambda: eh.start_assist(window, eh.RICE_MENU, 5, 'RICE_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "OTHERS":
                window['OTHERMEALS'].select()
                window.start_thread(lambda: eh.start_assist(window, eh.OTHER_MENU, 5, 'OTHER_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "RICE_CATEGORY" or event[1] == "OTHER_CATEGORY":
            if event[1] == "RICE_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "CHICKEN", "BURGER", "OTHERS"), ('-THREAD-', '-THREAD ENDED-'))
            elif event[1] == "OTHER_CATEGORY":
                window.start_thread(lambda: eh.get_command(window, "FRIES", "CHEESE", "RICE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-ORDER_MENU_LAYOUT-'].update("Listening...")


        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE", "CHANGE"]:
            if event[1] == "CHICKEN":
                temp_item = menu.chicken

                # RONWALDO UPDATE MO UI HERE
                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "BURGER":
                temp_item = menu.burgersteak

                # RONWALDO UPDATE MO UI HERE
                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            elif event[1] == "FRIES":
                temp_item = menu.fries

                # RONWALDO UPDATE MO UI HERE
                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "CHEESE":
                temp_item = menu.burger

                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.ASK_QTY, 3, 'ASK QTY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "ASK QTY":
            window.start_thread(lambda: eh.get_command(window, *eh.ALLOWED_QTY), ('-THREAD-', '-THREAD ENDED-'))
            window[f'-ASK_QTY_LAYOUT-'].update("Listening...")


        elif event[1] in eh.ALLOWED_QTY:
            temp_qty = eh.ALLOWED_QTY.index(event[1]) + 1

            # RONWALDO UPDATE MO UI HERE
            # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            window[f'-ASK_QTY_LAYOUT-'].update("CHANGE QTY NUMBER")
            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ITEM, 5, 'CONFIRM ITEM'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "CONFIRM ITEM":
            window.start_thread(lambda: eh.get_command(window, "ADD TO CART", "CANCEL ITEM"), ('-THREAD-', '-THREAD ENDED-'))
            window['-ASK_QTY_LAYOUT-'].update("Listening...")

        
        elif event[1] in ["ADD TO CART", "CANCEL ITEM", "BACK", "NO"]:
            # RONWALDO UPDATE MO UI HERE
            window['-ASK_QTY_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-CHECK_ORDER_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-MODIFY_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-ORDER_MENU_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            
            if event[1] == "ADD TO CART":
                cart[temp_item] = temp_qty
                print(cart)
                window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ADD + ". " + eh.CATEGORIES, 10, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "CANCEL ITEM" or event[1] == "BACK" or event[1] == "NO":
                window.start_thread(lambda: eh.start_assist(window, eh.CATEGORIES, 7, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            temp_item = None
            temp_qty = 0
            print(f"{temp_item}: {temp_qty}")

        
        elif event[1] == "VIEW ORDERS":
            # RONWALDO UPDATE MO UI HERE
            for item, qty in cart.items():
                items_layout.append([sg.Image(filename=item[1], size=(75, 75), pad=10),
                                     sg.Text(f"{item[0]} x{qty}")])

            # layout_column.update(items_layout)
            window['-ORDER_MENU_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-CART_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            timeout = len(cart.keys()) + 1
            window.start_thread(lambda: eh.start_assist(window, eh.get_cart_list(cart), timeout, 'ORDER ACTION'), ('-THREAD-', '-THREAD ENDED-'))
            
            
            
            

        elif event[1] == "ORDER ACTION":
            window.start_thread(lambda: eh.get_command(window, "MODIFY", "CHECK OUT", "EXIT", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            window['-CART_LAYOUT-'].update("Listening...")


        elif event[1] == "MODIFY":
            window['-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-MODIFY_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
        
            window.start_thread(lambda: eh.modify_order(window, cart), ('-MODIFY THREAD-', '-MODIFY THREAD ENDED-'))


        elif event[1] == "MODIFY OPTION":
            window.start_thread(lambda: eh.get_command(window, "CHANGE", "DELETE"), ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update("Listening...")

        elif event[1] == "DELETE":
            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_DELETE, 10, 'CONFIRM DELETE'), ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update("Listening...")

        elif event[1] == "CONFIRM DELETE":
            window.start_thread(lambda: eh.get_command(window, "YES", "NO"), ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update("Listening...")
        
        elif event[1] == "YES":
            cart.pop(temp_item)
            window.start_thread(lambda: eh.start_assist(window, eh.ITEM_DELETE, 3, 'NO'), ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update("Listening...")

        elif event[1] == "CHECK OUT":
            # HELLO GEO
            window[f'-CART_LAYOUT-'].update(visible=False)
            window[f'-CHECK_ORDER_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.prompt_check_out_menu(cart, window),('-THREAD-', '-THREAD ENDED-'))

        
        
        elif event[1] == "DONE CHECKOUT":
            window[f'-CHECK_ORDER_LAYOUT-'].update("Listening...") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.get_command(window, "CONFIRM ORDER", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "CONFIRM ORDER":
            window[f'-CHECK_ORDER_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.FINISHED_CHECKOUT, 10, 'FINISHED ORDER'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "EXIT":
            # RONWALDO UPDATE MO UI HERE
            window[f'-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.EXIT_APP, 6, 'EXIT APP'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "EXIT APP" or event[1] == "FINISHED ORDER":
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window[f'-HOME_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))
            

        


    elif event == '-TEXT-':
        eh.kiosk_prompt()
        # switch_window()
        # print("Switched")

window.close()
