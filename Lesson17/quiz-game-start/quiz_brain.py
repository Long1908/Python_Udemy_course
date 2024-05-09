class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number > len(self.question_list):
            print("You have completed the quiz.")
            print(f"Your final score is: {self.score}/{self.question_number - 1}")
            return False
        return True

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            print("You got it!")
            self.score += 1
        else:
            print(f"That's not correct. The answer is {q_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def ask_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.question} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)





