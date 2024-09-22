BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas

current_card = {}
to_learn = {}

############# NEXT CARD ############################

try:
    data = pandas.read_csv("day_31_flashcards/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("day_31_flashcards/flash-card-project-start/data/french_words.csv")
    to_learn = data.to_dict(orient='records')
else:
     to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image = card_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French',fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"],fill = 'black')
    flip_timer = window.after(3000, func=flip_card)

#################### Mark Card as Known or Not Known ######################
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("day_31_flashcards/flash-card-project-start/data/words_to_learn.csv",index=False)
   

############## Make Readout of Words You Missed or Need to Review ########################

##################### flip card ######################

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English",fill = "white")
    canvas.itemconfig(card_background, image = card_back)
    canvas.itemconfig(card_word, text = current_card["English"],fill = "white")

##############User Interface#################
window = Tk()
window.title("Flashcards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,func=flip_card)

#image canvas setup
canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file = 'day_31_flashcards/flash-card-project-start/images/card_front.png')
card_back = PhotoImage(file = "day_31_flashcards/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400,263,image = card_front)
card_title = canvas.create_text(400,150,font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)
wrong_image = PhotoImage(file='day_31_flashcards/flash-card-project-start/images/wrong.png')
wrong_button = Button(image=wrong_image,command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR,highlightthickness=0,borderwidth=0)
right_image = PhotoImage(file='day_31_flashcards/flash-card-project-start/images/right.png')
right_button = Button(image=right_image,command=is_known)
right_button.config(bg= BACKGROUND_COLOR, borderwidth=0,highlightthickness=0)
right_button.grid(row=1,column=0)
wrong_button.grid(row=1,column=1)
#make first french word appear
next_card()


# card_back = PhotoImage('day_31_flashcards/flash-card-project-start/images/card_back.png')
# #              Buttons and button images
# right_button = Button()
# right_button.config(command=known)
# right_button.grid(row=1,column=1)
# wrong_button = Button()
# wrong_button.grid(row=1,column=1)
# #            word text
# f_word_label = Label(text="Word")
# english_word_label = Label(text="English")



window.mainloop()
