class QuizBrain:

    def __init__(self,question_list,score=0):
        self.question_number = 0
        self.question_list = question_list
        self.score = score

    def next_question(self):
        current_question = self.question_number
        user_answer = input(f"Q.{current_question + 1}: {self.question_list[current_question].text} (True/False)?: ")
        correct_answer = self.question_list[current_question].answer
        self.check_answer(user_answer,correct_answer)
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's correct!")
        else:
            print("That's incorrect.")
        print(f"Current score: {self.score}/{self.question_number + 1}")
