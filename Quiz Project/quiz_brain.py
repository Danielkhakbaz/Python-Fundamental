class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.correct_answers = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1

        answer = input(
            f"Q.{self.question_number}: {current_question.question} (True/False): ").lower()

        if answer == current_question.answer.lower():
            self.correct_answers += 1

            return f"""You got it right!\nThe correct answer was: {current_question.answer}\nYour current score is: {self.correct_answers}/{self.question_number}"""
        else:
            return f"""You got it wrong!\nThe correct answer was: {current_question.answer}\nYour current score is: {self.correct_answers}/{self.question_number}"""

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False
