from customtkinter import *

app = CTk()

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

app.geometry("350x450")


text = CTkLabel(app,text="Custom Tkinter Text")
text.grid(row=0,column=0)

btn = CTkButton(app,text="Custom Tkinter Button",width=10,height=10,command= lambda : print("Button was pressed"))
btn.grid(row=0,column=1,padx=5,pady=0)

btn = CTkButton(app,text="Custom Tkinter Button",command= lambda : print("Button was pressed"))
btn.grid(row=0,column=2,padx=5,pady=0)

app.mainloop()