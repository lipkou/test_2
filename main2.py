from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Спамер 228')
window.resize(500, 200)

lb_qwestion = QLabel('Скыльки вам раз заспамити вікном?')
button1 = QRadioButton('1 вікно')
button2 = QRadioButton('10 вікон')
button3 = QRadioButton('25 вікон')
button4 = QRadioButton('50 вікон')

button1.setStyleSheet('color: green')
button2.setStyleSheet('color: blue')
button3.setStyleSheet('color: purple')
button4.setStyleSheet('color: red')

v_line = QVBoxLayout()

h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line1.addWidget(lb_qwestion, alignment=Qt.AlignCenter)
h_line2.addWidget(button1, alignment=Qt.AlignCenter)
h_line2.addWidget(button2, alignment=Qt.AlignCenter)
h_line3.addWidget(button3, alignment=Qt.AlignCenter)
h_line3.addWidget(button4, alignment=Qt.AlignCenter)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

def conntent_button():
    spam_win = QMessageBox()
    spam_win.resize(100, 75)
    spam_win.setText('hi')
    spam_win.exec_()




button1.clicked.connect(conntent_button)
button2.clicked.connect(conntent_button)
button3.clicked.connect(conntent_button)
button4.clicked.connect(conntent_button)

window.setLayout(v_line)

window.show()
app.exec_()