from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QListWidget, QApplication, QWidget, QLabel, QPushButton, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout)

app = QApplication([])
win = QWidget()
win.setWindowTitle('Python')
win.resize(500, 200)

qlist = QListWidget()
qlist.addItem('Котик')
btn1 = QPushButton('Додати слово Котик')
btn2 = QPushButton('Видалити весь список')



vline = QVBoxLayout()
hline = QHBoxLayout()

vline.addWidget(qlist)
hline.addWidget(btn1, alignment=Qt.AlignCenter)
hline.addWidget(btn2, alignment=Qt.AlignCenter)

vline.addLayout(hline)

def add_text_in_list():
    qlist.addItem('Котик')
def del_text_in_list():
    qlist.clear()

btn1.clicked.connect(add_text_in_list)
btn2.clicked.connect(del_text_in_list)

win.setLayout(vline)

win.show()
app.exec_()


'''
lb_qwestions = QLabel('Давай я вгадаю на яку ти кнопку натиснеш :)')
button1 = QPushButton('1-ша кнопка')
button2 = QPushButton('2-га кнопка')
button3 = QPushButton('3-тя кнопка')
button4 = QPushButton('4-тa кнопка')

button1.setStyleSheet('color: blue')
button2.setStyleSheet('color: red')
button3.setStyleSheet('color: green')
button4.setStyleSheet('color: purple')


v_line = QVBoxLayout()

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()


h_line1.addWidget(lb_qwestions, alignment=Qt.AlignCenter)
h_line2.addWidget(button1, alignment=Qt.AlignCenter)
h_line2.addWidget(button2, alignment=Qt.AlignCenter)
h_line3.addWidget(button3, alignment=Qt.AlignCenter)
h_line3.addWidget(button4, alignment=Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

def cnt_button1():
    lb_qwestions.setText('Ви натиснули на 1-шу кнопку')
    lb_qwestions.setStyleSheet('color: blue')


def cnt_button2():
    lb_qwestions.setText('Ви натиснули на 2-гу кнопку')
    lb_qwestions.setStyleSheet('color: red')

def cnt_button3():
    lb_qwestions.setText('Ви натиснули на 3-тю кнопку')
    lb_qwestions.setStyleSheet('color: green')

def cnt_button4():
    lb_qwestions.setText('Ви натиснули на 4-ту кнопку')
    lb_qwestions.setStyleSheet('color: purple')

button1.clicked.connect(cnt_button1)
button2.clicked.connect(cnt_button2)
button3.clicked.connect(cnt_button3)
button4.clicked.connect(cnt_button4)


'''