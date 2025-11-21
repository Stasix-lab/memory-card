#create a memory card application
#brbrbrbbrb
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)

class Question():
    def __init__(self, ques,right_answer,wrong1,wrong2,wrong3):
        self.ques = ques
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
window = QWidget()
window.cur_question = -1
window.resize(800, 500)
window.setWindowTitle("Memory Card")

RadioGroupBox = QGroupBox("Варіанти відповідей")
text = QLabel("Переклади англійською слово автомобіль")
btn = QPushButton("Answer")


btn1 = QRadioButton("Bus")
btn2 = QRadioButton("Car")
btn3 = QRadioButton("Taxi")
btn4 = QRadioButton("Ship")

RadioGroup = QButtonGroup()

RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

ans_line_h = QHBoxLayout()
ans_line_v1 = QVBoxLayout()
ans_line_v2 = QVBoxLayout()



ans_line_v1.addWidget(btn1, alignment=Qt.AlignCenter)
ans_line_v1.addWidget(btn2, alignment=Qt.AlignCenter)

ans_line_v2.addWidget(btn3, alignment=Qt.AlignCenter)
ans_line_v2.addWidget(btn4, alignment=Qt.AlignCenter)

ans_line_h.addLayout(ans_line_v1)
ans_line_h.addLayout(ans_line_v2)

RadioGroupBox.setLayout(ans_line_h)

ans_GroupBox = QGroupBox("Результат тесту")

text1 = QLabel("Відповідь вірна?")
text2 = QLabel("Відповідь буде тут!")

Layout_res = QVBoxLayout()
Layout_res.addWidget(text1)
Layout_res.addWidget(text2, alignment=Qt.AlignCenter)

ans_GroupBox.setLayout(Layout_res)


line_h1 = QHBoxLayout()
line_h1.addWidget(text, alignment=Qt.AlignCenter)

line_h2 = QHBoxLayout()
line_h2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
line_h2.addWidget(ans_GroupBox, alignment=Qt.AlignCenter)
line_h3 = QHBoxLayout()
line_h3.addWidget(btn, alignment=Qt.AlignCenter)



line_v = QVBoxLayout()

line_v.addLayout(line_h1)
line_v.addLayout(line_h2)
line_v.addLayout(line_h3)

ans_GroupBox.hide()



question_list = []
question_list.append( Question("What that pokemon? ", "Pikachu", 'Ponita', "Rock", "Bulbasavr") )
question_list.append( Question("2+2?", "4", '23', "43", "47") )
question_list.append( Question("Скількі днів в тижні ", "7", '2', "365", "500") )
question_list.append( Question("Столиця України?", "Київ", "Львів", "Харків", "Одеса") )
question_list.append( Question("Який тип даних у Python відповідає за цілі числа?", "int", "str", "float", "bool") )
question_list.append( Question("Яка тварина має 9 життів (за легендою)?", "Кіт", "Собака", "Кролик", "Слон") )




def show_result():
    RadioGroupBox.hide()
    ans_GroupBox.show()
    btn.setText("Наступне питання")

def show_question():
    ans_GroupBox.hide()
    RadioGroupBox.show()
    btn.setText("Answer")

    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)


def test():
    if "Answer" == btn.text():
        show_result()
    else:
        show_question()


def ask(q : Question ):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)    

    text.setText(q.ques)
    text2.setText(q.right_answer)
    show_question()

def show_correct(res):
    text1.setText(res)
    show_result()


window.score = 0
window.total = 0
answer = [btn1, btn2, btn3, btn4]
def check_answer():

    if answer[0].isChecked():
        show_correct("Correct!")
        window.score += 1
        print("Score:", window.score, "Total question:", window.total)
        print("Raiting:", window.score / window.total * 100, "%")
    else:

        if answer[1].isChecked() or answer[2].isChecked or answer[3].isChecked(): 
            show_correct("INCORRECT!!!")
            print("Score:", window.score, "Total question:", window.total)
            print("Raiting:", window.score / window.total * 100, "%")

def next_question():
    window.total +=1
    cur_question = randint(0, len(question_list) - 1)




    q = question_list[cur_question]


    ask(q)

def click_ok():
    if btn.text() == "Answer":
        check_answer()
    else:
        next_question()



btn.clicked.connect(click_ok)

next_question()
window.setLayout(line_v)

window.show()

app.exec_()
