from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#make a question bank
question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]    
    question = Question(text, answer)
    question_bank.append(question)


quizbrain = QuizBrain(question_bank)
while True:
    response = quizbrain.new_question()
    quizbrain.check_answer(response)
    question_number = quizbrain.question_number
    if question_number == len(question_bank):
        print(f"You've completed the quiz! Your final score is {quizbrain.score}/{question_number}")
        break
