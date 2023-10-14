from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle("Лотерея")
win.resize(400,400)
win.move(100, 100)

def rand():
    num1 = str(randint(0,9))
    num2 = str(randint(0,9))
    text2.setText(num1)
    text3.setText(num2)

    if num1 == num2:
        text1.setText("Ви виграли!")
    else:
        text1.setText("Ви програли!")


text1 = QLabel()
text1.setText("Натисни, щоб взяти участь»")

text2 = QLabel()
text2.setText("?")

text3 = QLabel()
text3.setText("?")

but = QPushButton()
but.setText("Випробувати удачу")

lineV = QVBoxLayout()
lineV.addWidget(text1, alignment=Qt.AlignCenter)
lineV.addWidget(text2, alignment=Qt.AlignCenter)
lineV.addWidget(text3, alignment=Qt.AlignCenter)
lineV.addWidget(but, alignment=Qt.AlignCenter)

win.setLayout(lineV)

but.clicked.connect(rand)


























win.show()
app.exec_()