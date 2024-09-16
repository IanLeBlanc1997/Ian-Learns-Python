from tkinter import * 
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300,height=100)
window.config(padx=50,pady=50)
answer = Label(text=0)
answer.grid(column=1,row=2)

#calculator
def calculate():
    result = float(input.get()) * 1.6
    answer.config(text=result)
#input and button
input = Entry(width=10)
input.grid(column=1,row=0)
button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=3)

#labels
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=2)
miles = Label(text="Miles")
miles.grid(column=3,row=0)
km = Label(text="Km")
km.grid(column=3,row=2)














window.mainloop()