from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text,text= quote)
    
    

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/Users/ianleblanc/Desktop/Repositories/Ian-Learns-Python/100_days_of_python/day_33_API's_ISS_Tracker/kanye_quote_generator/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file="day_33_API's_ISS_Tracker/kanye_quote_generator/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()