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
while quizbrain.still_has_questions():
    response = quizbrain.new_question()
    quizbrain.check_answer(response)
print(f"You've completed the quiz! Your final score is {quizbrain.score}/{quizbrain.question_number}")
    
    
