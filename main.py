from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])
win = QWidget()
win.setWindowTitle('Тест1')
win.resize(300, 130)
win.move(200, 200)


lb_text = QLabel('Дізнайтесь переможця:')
winner = QLabel('???')
btn = QPushButton('Нажми мене')


vline = QVBoxLayout()
vline.addWidget(lb_text, alignment=Qt.AlignCenter)
vline.addWidget(winner, alignment=Qt.AlignCenter)
vline.addWidget(btn, alignment=Qt.AlignCenter)

def rundom_win():
    lb_text.setText('Переможець:')
    winner.setText(str(randint(1, 100)))

btn.clicked.connect(rundom_win)

win.setLayout(vline)


win.show()
app.exec_()