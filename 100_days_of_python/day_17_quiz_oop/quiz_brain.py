class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def new_question(self):
        text = self.question_list[self.question_number]
        response = input(f"Q{self.question_number+1}: {text.text} (True/False)?\n").lower()
        return response
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self, response):
        answer = self.question_list[self.question_number]
        if response == answer.answer.lower():
            self.question_number +=1
            self.score +=1
            print("You got it right!")
            return True
        else:
            self.question_number +=1
            print("That's wrong.")
            return False 