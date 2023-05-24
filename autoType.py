import PySimpleGUI as sg
import pyautogui
import time


sg.theme("black")
window_size = (800,500)
text_delay = 0.1
timebeforeTyping = 5

layout = [
    [sg.Text("Enter Text Here")],
    [sg.Multiline(size=(120,20),key="-content-")],
    [sg.Submit("Start",key="-start-",size=(10,4))]
]

window = sg.Window("AutoType",layout=layout,size=window_size)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-start-":

        time.sleep(timebeforeTyping)
        pyautogui.typewrite(values["-content-"],text_delay)


