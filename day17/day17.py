from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    questionobj=Question(i['question'],i['correct_answer'])
    question_bank.append(questionobj)
quiz = QuizBrain(question_bank)
score=0
while True:
    if quiz.still_has_question():
        quiz.next_question()
        if quiz.check_answer():
            print("You got it right")
            score+=1
            print(f"The correct answer is {quiz.question_answer}")
            print(f"score is {score}")
        else:
            print(f"You got it wrong")
            break
    else:
        break
print("you have reached end of quiz")
print(f"Your final score is {score}/{quiz.question_number}")