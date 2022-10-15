from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout)

def true_answer(): #правильно відповіли
    true_answer = QMessageBox()
    true_answer.resize(100, 75)
    true_answer.setText('Вгадав!')
    true_answer.exec_()

def false_answer(): #не правильно відповіли
    false_answer = QMessageBox()
    false_answer.resize(100, 75)
    false_answer.setText('Не правильно!')
    false_answer.exec_()


app = QApplication([])
win = QWidget()
win.setWindowTitle('Вікторина')
win.resize(500, 200)

#створення контенту
lb_qwestions = QLabel('"55" * 2 = ?')
rbtn1 = QRadioButton('110') 
rbtn2 = QRadioButton('"552"')
rbtn3 = QRadioButton('"5555"')
rbtn4 = QRadioButton('Error')

#*розташування ліній і контент в них
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(lb_qwestions, alignment=Qt.AlignCenter)
hline2.addWidget(rbtn1, alignment=Qt.AlignCenter)
hline2.addWidget(rbtn2, alignment=Qt.AlignCenter)
hline3.addWidget(rbtn3, alignment=Qt.AlignCenter)
hline3.addWidget(rbtn4, alignment=Qt.AlignCenter)

#додаєм 3 лінії на 1 лінюю
vline = QVBoxLayout()
vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)

rbtn1.clicked.connect(false_answer)
rbtn2.clicked.connect(false_answer)
rbtn3.clicked.connect(true_answer)
rbtn4.clicked.connect(false_answer)


win.setLayout(vline)

win.show()
app.exec_()
