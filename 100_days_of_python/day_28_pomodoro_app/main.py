
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = ""
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global check
    global reps
    reps = 0
    window.after_cancel(timer)
    check_label.config(text='')
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN *60)
    long_break_sec = int(LONG_BREAK_MIN *60)
    if reps % 2 == 0:
        count_down(work_sec)
        title_label.config(text="Work", fg= RED)
    elif reps % 7 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break",fg=GREEN)
    else:
        count_down(short_break_sec)
        title_label.config(text="Short Break",fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global check
    global reps
    count_minute = math.floor(count/60)
    count_seconds = count%60
    if count_seconds == 0:
        count_seconds = "00"
    if count_seconds !="00":
        if count_seconds < 10:
            count_seconds = (f"0{count_seconds}")
    canvas.itemconfig(timer_text,text = (f"{count_minute}:{count_seconds}"))
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    if count == 0:
        reps +=1
        if reps %2 != 0:
            check += "✓"
            check_update(check)
        start_timer()
    if reps ==8:
        reset_timer()

# ---------------------------- UI SETUP ------------------------------- #

def check_update(check):
    check_label.config(text=check)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg= YELLOW)
canvas = Canvas(width=200,height=223,bg= YELLOW,highlightthickness=0)
tomato = PhotoImage(file = "day_28_pomodoro_app/tomato.png")
canvas.create_image(100,112, image= tomato)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font = (FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#buttons
start = Button(text="Start",command= start_timer)
start.grid(column=0,row=2)
start.config(fg=GREEN,bg=YELLOW,highlightbackground=YELLOW)
reset = Button(text="Reset",command=reset_timer)
reset.grid(column=3,row=2)
reset.config(fg=GREEN,bg=YELLOW,highlightbackground=YELLOW)
#labels
check_label = Label(text=f"{check}")
check_label.grid(column=1,row=3)
check_label.config(fg=GREEN,bg=YELLOW)
title_label = Label(text="Timer")
title_label.grid(column=1,row=0)
title_label.config(fg=GREEN,bg=YELLOW,font= (FONT_NAME, 25))






window.mainloop()