from tkinter import *

#window
window = Tk()
window.title("My first GUI")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)

#Label

label = Label(text="I am a label",font=("Arial",24))
label['text'] = "new"
label.config(text="label")
label.grid(column=0,row=0)
label.config(padx=50,pady=50)

#button
def button_clicked():
    label["text"] = input.get()



button = Button(text="Button1", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="Button2")
button2.grid(column=3,row=0)


# entry component

input = Entry(width=10)
input.grid(column=4,row=3)














window.mainloop()