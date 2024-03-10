from Questions_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    qt = i["text"]
    qa = i["answer"]
    new_question = Question(qt, qa)
    question_bank.append(new_question)
#print(question_bank[0].answer)
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz")
#print(f"Your's total score is {quiz.score}/{quiz.len(question_bank)}")