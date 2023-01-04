import PySimpleGUI as sg
import time


def time_as_int():
    return int(round(time.time() * 1))


# ----------------  Create Form  ----------------

layout = [
            [sg.InputText(key='-IN-', size=(20, 1), background_color='white')],
            [sg.Text('')],
            [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                  justification='center', key='text')],
            [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
             sg.Button('Start', key='-RUN-START-', button_color=('white', '#001480')),
             sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
             sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer',
                   layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0),
                   finalize=True,
                   element_justification='c',
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)
window.maximize()
current_time, paused_time, paused = 0, 0, True
start_time = time_as_int() # start the timer as soon as the program starts

while True:
    event, values = window.read(timeout=10)
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
   
window.close()