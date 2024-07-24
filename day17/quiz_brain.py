from question_model import Question
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list=q_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_answer=input(f"Q{self.question_number+1}. {current_question.text} True/False?")
        self.question_number += 1
        self.correct_answer=current_question.answer
    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
    def check_answer(self):
        return self.question_answer==self.correct_answer


