class Question:
    __slots__ = ["question", "answer"]

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
