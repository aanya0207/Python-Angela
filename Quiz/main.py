from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for q in question_data:
    new_ques = Question(q["text"],q["answer"])
    question_bank.append(new_ques)

#print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("/n/n You have completed the Quiz !!")