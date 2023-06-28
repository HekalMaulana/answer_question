from question_model import Question # memanggil class Question di dalam sebuah file question_model.py
from data import question_data # memanggil list question_data di dalam file data.py
from quiz_brain import QuizBrain # memanggil class quiz_brain di dalam file quiz_brain.py

question_bank = []
for question in question_data: # mengulang semua question dan answer yang ada di dalan question data
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # membuat sebuah variable yang berisi class Question dengan parameter question_text dan question_answer
    question_bank.append(new_question) # menambahkan isi dari variabel new_questtion ke sebuah list yang bernama question_bank

quiz = QuizBrain(question_bank) # membuat sebuah varial quiz yang berisi class QuizBrain dengan parameter question_bank

while quiz.still_has_question(): # mengulang apabila quiz.still_has_question == True
    quiz.next_question() # menampilkan method next_question

print("You Complete the quiz")
print(f"Your final score is {quiz.score} from {len(quiz.list)} Question")