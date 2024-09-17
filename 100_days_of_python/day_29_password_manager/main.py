from tkinter import *
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    all_characters = {
    "alphabet":['a','b','c','d','e','f','g','h','i','j','k','l''m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L''M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    "numbers" : ['0','1','2','3','4','5','6','7','8','9'],
    "characters": ['!','@',"#","$",'%','^',"&","*"]
    }
    password = ""
    for n in range (1,15):
        type = random.choice(list(all_characters.keys()))
        category = all_characters[type]
        character = random.choice(category)
        password += character
    password_entry.insert(index=0,string= password)
# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open ('day_29_password_manager/passwords.json','r') as passwords_file:
            data = json.load(passwords_file)
    except:
        messagebox.showerror(message="No data file found")
        #see if there is a dictionary with the key of the website name
    if website in data:
        email_entry.insert(0,data[website]['email'])
        password_entry.insert(0,data[website]['password'])
    else:
        email_entry.delete(0,END)
        password_entry.delete(0,END)
        messagebox.showerror(message="There is no saved data for this site")
            



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    new_data = {website: {'email': email_entry.get(),'password': password_entry.get()}}
    fields_full= True
    if website_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        fields_full = messagebox.showwarning(message="There are fields empty")
        fields_full = False
    if fields_full == True:
        try:
            with open('day_29_password_manager/passwords.json','r') as passwords_file:
                #reading old data
                data = json.load(passwords_file)
        except:
            #if that fails we want to write the new data in
            with open('day_29_password_manager/passwords.json','w') as passwords_file:
                json.dump(fp=passwords_file,obj=new_data,indent=4)
        else:
            #if it doesn't fail then we want to update the data
            data.update(new_data)
            #and save it into the json file
            with open('day_29_password_manager/passwords.json','w') as passwords_file:
                json.dump(fp=passwords_file,obj=data,indent=4)
        finally:
            #then no matter what we are going to erase the entries
            email_entry.delete(0,END)
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
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
add_button = Button(text="Add",command=add, width=32)
add_button.grid(row=5,column=2)
search_button = Button(text="Search",command=search)
search_button.grid(row=1,column=4)





window.mainloop()