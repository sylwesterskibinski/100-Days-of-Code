class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_number
        input(f"Q.{current_question + 1}: {self.question_list[current_question].text} (True/False)?: ")
    
    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            True
        else:
            False