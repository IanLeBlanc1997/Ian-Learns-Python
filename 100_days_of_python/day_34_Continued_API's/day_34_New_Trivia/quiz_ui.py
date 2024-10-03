from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
THEME_COLOR = "#375362"
score = 0

#make a question bank
question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]    
    question = Question(text, answer)
    question_bank.append(question)

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        global score
        #make an instance of the quiz brain within the UI
        self.quiz_brain = QuizBrain(question_bank)


        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {score}",fg='white',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas.grid(pady=20)
        self.question_text = self.canvas.create_text(150,125,text="Question",fill=THEME_COLOR, font=("Arial",25,'italic'))
        self.true_button = Button(text='True',command=self.respond_true)
    
        self.true_button.grid(row=2,column=0)
    
        self.false_button = Button(text='False',command=self.respond_false)
        self.false_button.grid(row=2,column=2)
        self.canvas.grid(row=1,column=1)

        #make a new question upon initialization
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.new_question()
            self.canvas.itemconfig(self.question_text,text = question_text)
        else: 
            self.canvas.itemconfig(self.question_text,text = "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def respond_true(self):
        if self.quiz_brain.check_answer("true") == True:
            self.correct()
        else:
            self.incorrect()
        
    def respond_false(self):
        if self.quiz_brain.check_answer("false") == True:
            self.correct()
        else:
            self.incorrect()
        
    def correct(self):
        global score
        self.quiz_brain.question_number += 1
        score +=1
        self.score_label.configure(text=f'Score: {score}')
        self.get_next_question()
    def incorrect(self):
        self.quiz_brain.question_number +=1
        self.get_next_question()
    

quiz_ui = QuizInterface(QuizBrain(question_data[0]['text']))