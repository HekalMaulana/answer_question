class QuizBrain:
    def __init__(self, q_list): # sebuah function yang menyimpan data dari qustion_bank
        self.number = 0
        self.list = q_list
        self.score = 0

    def still_has_question(self): # sebuah function yang mereturn nilai True apabila self.number < jumlah list dari self.list
        return self.number < len(self.list)

    def check_answer(self, u_answer, q_answer): # sebuah function yang mencek benar dan salah jawaban dari user dan juga menambahkan score ke user apabila user menjawab question dengan benar
        if u_answer.lower() == q_answer.lower():
            print("You Got Right Answer")
            self.score += 1
        else:
            print("You got Wrong Answer")

        print(f"The right answer is : {q_answer}")
        print(f"Your current score is: {self.score}/{self.number}\n")

    def next_question(self): # sebuah function yang mereturn sebuah output dari function check_answer dan membuat user menginputkan nilau boolean dari sebuah question
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"{self.number}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)



