import PySimpleGUI as sg
import event_handler as eh
from PIL import Image, ImageTk
# menu
import menu_item as menu


all_meals = [menu.chicken, menu.burgersteak, menu.burger, menu.fries]

# data to be manipulated
cart = {}
# cart = {menu.chicken: 1, menu.burgersteak: 3} #format {menu.item1: qty, menu.item2: qty}
temp_item = (None, None)
temp_qty = 0


#Layout for order menu


layout_tab1 = [[sg.Text('Rice Meals', background_color=('#E8DFCA'), colors='black', font=('Courier'))],
               [sg.Column([
        [sg.Image(filename=menu.chicken[1], size=(75, 75), pad=10, background_color='#4F6F52'), 
         sg.Image(filename=menu.burgersteak[1], size=(75, 75), background_color='#4F6F52')]
    ], justification='center', background_color='#1A4D2E')]]
layout_tab2 = [[sg.Text('Other Meals', background_color=('#E8DFCA'), colors='black', font=('Courier'))],
               [sg.Column([
        [sg.Image(filename=menu.burger[1], size=(75, 75), pad=10, background_color='#4F6F52' ), 
         sg.Image(filename=menu.fries[1], size=(75, 75), background_color='#4F6F52')]
    ], justification='center', background_color='#1A4D2E')]]


tab1 = sg.Tab('🍚', layout_tab1, background_color=('#E8DFCA'))
tab2 = sg.Tab('🍔', layout_tab2, background_color=('#E8DFCA'))

tab_group_layout = [[tab1, tab2]]

tab_group = sg.TabGroup(tab_group_layout, tab_location='left', title_color='black', size=(400, 525), pad= 10, background_color=('#E8DFCA'), tab_background_color='#E8DFCA', selected_title_color='black', selected_background_color='#4F6F52', font=100 )

order_menu_layout = [[sg.Text(text="Pick a Category", background_color=('#E8DFCA'), colors='black',
                    expand_x=True, justification='center', pad=(0, 0), font=('Courier'))],
                    [sg.Column([[tab_group]], background_color='#E8DFCA', pad=(0, 0))]]


dine_take_layout = [[sg.Image(filename='speech-recog-kiosk\images\\bini.png', 
              size=(0,525), pad=(0, 0), background_color=('#F5EFE6'))]
                    ]

def item_details(item, qty, qty_key, item_key):
    layout = [sg.pin(sg.Col([[sg.Image(filename=item[1], size=(75, 75), pad=10, background_color='#4F6F52',)],
                [sg.Text(item[0], justification='center', background_color=('#E8DFCA'), colors='black',  expand_x=True, pad=(0, 0), font=('Courier', 10))],
                [sg.Text(qty, justification='center', key=(qty_key, item[0]), expand_x=True , pad=(0, 0), colors=('black'), background_color=('#E8DFCA'))]
                ], k=(item_key, item[0]), visible=False, background_color=('#1A4D2E'), pad=(0, 0)))]
    return layout

modify_layout = [[sg.Text(text="Modify your order", expand_x=True, justification='center', background_color=('#E8DFCA'), colors='black', pad=(0, 0), font=('Courier', 10))],
                 [sg.Frame('', layout=[
                    [sg.Column([item_details(item, 1, '-EDIT QTY-', '-MODIFY ITEM-') for item in all_meals], element_justification='center', background_color=('#E8DFCA'),  expand_x=True)]
                    ], background_color=('#E8DFCA'), expand_x=True ,size = (400, 525), pad=(0, 0))]
                    ]

ask_qty_layout = [[sg.Text(text="How many?", expand_x=True, justification='center', background_color=('#E8DFCA'), colors='black', pad=(0, 0), font=('Courier'))],
                  [sg.Frame('', layout=[
                    [sg.Column([item_details(item, 1, '-MODIFY DETAILS-', '-ASK_QTY-') for item in all_meals], element_justification='center', expand_x=True, background_color=('#E8DFCA'))]], 
                            background_color=('#E8DFCA'), expand_x=True ,size = (400, 525), pad=(0, 0))]
                    ]

def item_row(item, qty):    
    row =  [sg.pin(sg.Col([[sg.Image(filename=item[1], size=(75, 75), pad=10, background_color=('#4F6F52')),
                         sg.Text(f"{item[0]} x {qty}", key=(item[0], 'QUANTITY'), background_color=('#E8DFCA'), colors='black', font=('Courier', 10))]], k=('-CART ITEM-', item[0]), visible=False, background_color=('#E8DFCA'), pad=(0, 0)))]
    return row

cart_layout = [
    [sg.Text("Cart", expand_x=True, justification='center', colors=('black'), background_color='#E8DFCA', pad=(0, 0), key='CART_CHECKOUT', font=('Courier'))],
    [sg.Frame('', layout=[[sg.Column([item_row(item, 0) for item in all_meals], key='-ORDER LIST-', expand_x=True, expand_y=True, background_color=('#E8DFCA'), pad=(0, 0))]], 
              background_color='#E8DFCA', expand_x=True, size=(400, 525), pad=(0, 0))]
]

# check_order_layout = [[sg.Text(text="Check your Order before we proceed", 
#                     expand_x=True,
#                     justification='center',
#                     background_color=('#FF8A08'))],
#                     [sg.Frame('', layout=[[sg.Column(, key='-ORDER LIST-', expand_x=True)]
#                     ], background_color=('#FF6500'), expand_x=True ,size = (400, 525))]
#                     ]

home_layout = [
    [sg.Text(text="Hello Customer!", 
             font=('Courier', 20), 
             expand_x=True, 
             background_color=('#E8DFCA'), 
             colors='black', 
             justification='center', 
             enable_events=True, pad=(0, 0),
             key='-TEXT-')],
    [sg.Image(filename='speech-recog-kiosk\images\\newhome.png',
              size=(0,550), pad=(0, 0), background_color=('#F5EFE6'))]
]

main_layout = [
            [sg.Column(home_layout, key= '-HOME_LAYOUT-'), #CHANGE BACK TO home_layout  
             sg.Column(dine_take_layout, visible=False, key='-DINE_TAKE_LAYOUT-'),
             sg.Column(order_menu_layout, visible=False, key='-ORDER_MENU_LAYOUT-'),
             sg.Column(ask_qty_layout, visible=False, key='-ASK_QTY_LAYOUT-'),
             sg.Column(cart_layout, visible=False, key='-CART_LAYOUT-'), #CHANGE BACK
            #  sg.Column(cart_layout, visible=False, key='-CHECK_ORDER_LAYOUT-'),
             sg.Column(modify_layout, visible=False, key='-MODIFY_LAYOUT-'),
             ]]

    
sg.theme_background_color('#F5EFE6')
window = sg.Window('Speech \'o Order', main_layout, size=(360, 640))

window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))
sg.set_options(suppress_raise_key_errors=True, suppress_error_popups=True, suppress_key_guessing=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event[0] == '-MODIFY THREAD-':
        if event[1] == 'FINISHED PROMPT':
            window.start_thread(lambda: eh.get_modify_command(window, "CHICKEN", "BURGER", "FRIES", "CHEESE"), ('-THREAD-', '-THREAD ENDED-'))
                    
        elif event[1] in ["CHICKEN", "BURGER", "FRIES", "CHEESE"]:
            window['-CART_LAYOUT-'].update(visible=False) 

            match event[1]:
                case "CHICKEN":
                    window[('-EDIT QTY-', menu.chicken[0])].update(cart[menu.chicken])
                    window[('-MODIFY ITEM-', menu.chicken[0])].update(visible=True)
                    temp_item = menu.chicken
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify your Chicken Joy order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
                case "BURGER":
                    window[('-EDIT QTY-', menu.burgersteak[0])].update(cart[menu.burgersteak])
                    window[('-MODIFY ITEM-', menu.burgersteak[0])].update(visible=True)
                    temp_item = menu.burgersteak
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Burger Steak order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
                case "FRIES":
                    window[('-EDIT QTY-', menu.fries[0])].update(cart[menu.fries])
                    window[('-MODIFY ITEM-', menu.fries[0])].update(visible=True)
                    temp_item = menu.fries
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify French Fries order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'),) 
                case "CHEESE":
                    window[('-EDIT QTY-', menu.burger[0])].update(cart[menu.burger])
                    window[('-MODIFY ITEM-', menu.burger[0])].update(visible=True)
                    temp_item = menu.burger
                    window.start_thread(lambda: eh.start_assist(window, "You want to modify Cheese Burger order" + eh.MODIFY_OPTIONS, 7, 'MODIFY OPTION'), 
                                        ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update(visible=True)
      


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
            window.start_thread(lambda: eh.get_command(window, "RICE", "KANIN", "OTHERS", "VIEW ORDERS"), ('-THREAD-', '-THREAD ENDED-'))
            window['-ORDER_MENU_LAYOUT-'].update("Listening...")

        elif event[1] in ["RICE", "KANIN", "OTHERS"]:
            if event[1] == "RICE" or event[1] == "KANIN":
                window['🍚'].select()
                window.start_thread(lambda: eh.start_assist(window, eh.RICE_MENU, 5, 'RICE_CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "OTHERS":
                window['🍔'].select()
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
                window[('-ASK_QTY-',temp_item[0])].update(visible=True)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "BURGER":
                temp_item = menu.burgersteak

                # RONWALDO UPDATE MO UI HERE
                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window[('-ASK_QTY-',temp_item[0])].update(visible=True)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            
            elif event[1] == "FRIES":
                temp_item = menu.fries

                # RONWALDO UPDATE MO UI HERE
                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window[('-ASK_QTY-',temp_item[0])].update(visible=True) 
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            elif event[1] == "CHEESE":
                temp_item = menu.burger

                window['-ORDER_MENU_LAYOUT-'].update(visible=False)
                window[('-ASK_QTY-',temp_item[0])].update(visible=True)
                window['-ASK_QTY_LAYOUT-'].update(visible = True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window.start_thread(lambda: eh.start_assist(window, eh.ASK_QTY, 3, 'ASK QTY'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "ASK QTY":
            window.start_thread(lambda: eh.get_command(window, *eh.ALLOWED_QTY, *eh.TAGALOG_QTY), ('-THREAD-', '-THREAD ENDED-'))
            window[f'-ASK_QTY_LAYOUT-'].update("Listening...")


        elif event[1] in eh.ALLOWED_QTY or event[1] in eh.TAGALOG_QTY:
            if event[1] in eh.ALLOWED_QTY:
                temp_qty = eh.ALLOWED_QTY.index(event[1]) + 1
                

            elif event[1] in eh.TAGALOG_QTY:
                temp_qty = eh.TAGALOG_QTY.index(event[1]) + 1

            window[('-MODIFY DETAILS-', temp_item[0])].update(temp_qty)
            window[('-EDIT QTY-', temp_item[0])].update(temp_qty)
            

            window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ITEM, 5, 'CONFIRM ITEM'), ('-THREAD-', '-THREAD ENDED-'))


        elif event[1] == "CONFIRM ITEM":
            window.start_thread(lambda: eh.get_command(window, "ADD TO CART", "CANCEL ITEM"), ('-THREAD-', '-THREAD ENDED-'))
            window['-ASK_QTY_LAYOUT-'].update("Listening...")

        
        elif event[1] in ["ADD TO CART", "CANCEL ITEM", "BACK", "NO"]:
            # RONWALDO UPDATE MO UI HERE
            try:
                # Adding order
                window[('-MODIFY DETAILS-', temp_item[0])].update(1)
                window[('-ASK_QTY-',temp_item[0])].update(visible=False)

                # Modifying  order
                window[('-EDIT QTY-', temp_item[0])].update(1)
                window[('-MODIFY ITEM-', temp_item[0])].update(visible=False)
            
            except:
                print("Cart is empty")
            finally:
                window['-ASK_QTY_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
                window['-MODIFY_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            
            # window['-CHECK_ORDER_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['CART_CHECKOUT'].update("Cart")
            window['-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            window['-ORDER_MENU_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED

            
            if event[1] == "ADD TO CART":
                cart[temp_item] = temp_qty
                window[('-CART ITEM-', temp_item[0])].update(visible=True)
                window[(temp_item[0], 'QUANTITY')].update(f"{temp_item[0]} x {temp_qty}")
                print(cart)
                window.start_thread(lambda: eh.start_assist(window, eh.CONFIRM_ADD + ". " + eh.CATEGORIES, 10, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            elif event[1] == "CANCEL ITEM" or event[1] == "BACK" or event[1] == "NO":
                window.start_thread(lambda: eh.start_assist(window, eh.CATEGORIES, 7, 'CATEGORY'), ('-THREAD-', '-THREAD ENDED-'))
            
            temp_item = (None, None)
            temp_qty = 0
            print(f"{temp_item}: {temp_qty}")

        
        elif event[1] == "VIEW ORDERS":
            # RONWALDO UPDATE MO UI HERE

            window['-ORDER_MENU_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window['-CART_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            timeout = len(cart.keys()) + 1
            window.start_thread(lambda: eh.start_assist(window, eh.get_cart_list(cart), timeout, 'ORDER ACTION'), ('-THREAD-', '-THREAD ENDED-'))
            

        elif event[1] == "ORDER ACTION":
            window.start_thread(lambda: eh.get_command(window, "MODIFY", "CHECK OUT", "EXIT", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            window['-CART_LAYOUT-'].update("Listening...")


        elif event[1] == "MODIFY":
            # window['-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            # window['-MODIFY_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
        
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
            window[('-CART ITEM-', temp_item[0])].update(visible=False)
            window[(temp_item[0], 'QUANTITY')].update(f"{temp_item[0]} x {0}")

            window.start_thread(lambda: eh.start_assist(window, eh.ITEM_DELETE, 3, 'NO'), ('-THREAD-', '-THREAD ENDED-'))
            window['-MODIFY_LAYOUT-'].update("Listening...")

        elif event[1] == "CHECK OUT":
            # HELLO GEO
            # window[f'-CART_LAYOUT-'].update(visible=False)
            # CHECK_ORDER_LAYOUT
            window['CART_CHECKOUT'].update("Check your Order before we proceed")
            # window[f'-CHECK_ORDER_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.prompt_check_out_menu(cart, window),('-THREAD-', '-THREAD ENDED-'))

        
        
        elif event[1] == "DONE CHECKOUT":
            # window[f'-CHECK_ORDER_LAYOUT-'].update("Listening...") # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.get_command(window, "CONFIRM ORDER", "BACK"), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "CONFIRM ORDER":
            window[f'-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            # window[f'-CHECK_ORDER_LAYOUT-'].update(visible=False)
            window['CART_CHECKOUT'].update("Cart")
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.FINISHED_CHECKOUT, 10, 'FINISHED ORDER'), ('-THREAD-', '-THREAD ENDED-'))
            
        elif event[1] == "EXIT":
            # RONWALDO UPDATE MO UI HERE
            window[f'-CART_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.EXIT_APP, 6, 'EXIT APP'), ('-THREAD-', '-THREAD ENDED-'))

        elif event[1] == "EXIT APP" or event[1] == "FINISHED ORDER":
            for item, qty in cart.items():
                window[('-CART ITEM-', item[0])].update(visible=False)
                window[(item[0], 'QUANTITY')].update(f"{temp_item[0]} x {0}")
            cart = {}
            window[f'-DINE_TAKE_LAYOUT-'].update(visible=False) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window[f'-HOME_LAYOUT-'].update(visible=True) # TEMPORARY FOR CHECKING, DELETE WHEN UI UPDATED
            window.start_thread(lambda: eh.start_assist(window, eh.START_PROMPT, 5, 'DONE START'), ('-THREAD-', '-THREAD ENDED-'))
            

        


    elif event == '-TEXT-':
        eh.kiosk_prompt()
        # switch_window()
        # print("Switched")

window.close()
