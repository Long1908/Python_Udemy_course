from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #question_bank.append(Question(question["text"], question["answer"])) -> This also works
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.ask_question()
