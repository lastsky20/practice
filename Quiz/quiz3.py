class Word:
    def __init__(self, question, showcase1, showcase2, answer):
        self.question = question
        self.showcase1 = showcase1
        self.showcase2 = showcase2
        self.answer = answer

    def show_question(self):
        print("{0} 의 뜻은?".format(self.question))
        print(f"1.{self.showcase1}")
        print(f"2.{self.showcase2}")


    def check_answer(self, answer):
        if answer == self.answer:
            print("정답입니다")
        else:
            print("틀렸습니다")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=>")))
