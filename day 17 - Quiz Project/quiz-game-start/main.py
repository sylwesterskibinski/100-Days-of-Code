from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text,answer)
    question_bank.append(question)

while still_has_questions():
    next_question()