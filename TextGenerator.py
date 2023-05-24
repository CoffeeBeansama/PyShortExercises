import PySimpleGUI as sg
import pathlib

sg.theme("black")
window_size = (800,600)


menu = [ ["File",["Open","Save","Save as","Exit"]],
]

layout = [
    [sg.Menu(menu)],
    [sg.Text("Enter your Text")],
    [sg.Multiline(key= "content",size=[300,20],auto_size_text=False,expand_y=False)],


]

window = sg.Window("Text editor",layout=layout,size=window_size,font="Arial")

while True:

    event, values = window.read()


    if event == sg.WINDOW_CLOSED:
        break

    if event in ["Courier","Verdana","Times"]:

        window["content"].update(font=f"{event}")


    if event == "Save":
        with open('someText(saved).txt', 'w+') as file:
            savedText1 = file.write(values["content"])

    if event == "Save as":
        filepath = sg.popup_get_file("Save as",no_window=True,save_as=True) + ".txt"
        file = pathlib.Path(filepath)
        file.write_text(values["content"])













