from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    characters = {
    "alphabet":['a','b','c','d','e','f','g','h','i','j','k','l''m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L''M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    "numbers" : ['0','1','2','3','4','5','6','7','8','9'],
    "characters": ['!','@',"#","$",'%','^',"&","*"]
    }
    password = ""
    for n in range (1,15):
        type = random.choice(list(characters.keys()))
        category = characters[type]
        choice = random.choice(category)
        password += choice
    password_entry.insert(index=0,string= password)
        

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    with open("day_29_password_manager/passwords.txt",'a') as passwords_file:
        passwords_file.write("\n")
        passwords_file.write(f'Website: {website_entry.get()}, Username/Email: {email_entry.get()}, Password: {password_entry.get()}')
   
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
#image
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="day_29_password_manager/logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0,column=2)

#buttons labels and entries
website_label = Label(text="Website:")
website_label.grid(row=1,column=1)
website_entry = Entry(width=35)
website_entry.grid(row=1,column=2)
password_entry = Entry(width=21)
password_entry.grid(row=4,column=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=2)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column = 1)
password_label = Label(text="Password:")
password_label.grid(row=4,column=1)
generate_button = Button(text="Generate Password",command = generate)
generate_button.grid(row=4,column=4)
add_button = Button(text="Add",command=add, width=36)
add_button.grid(row=5,column=2)





window.mainloop()