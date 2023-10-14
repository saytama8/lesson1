from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle("Генератор")
win.resize(400,200)
win.move(100, 100)

def rand():
    text.setText("Переможець:")
    text2.setText(str(randint(1, 100)))

text = QLabel()
text.setText("Натисни, щоб дізнатися переможця")
text2 = QLabel()
text2.setText("?")

but = QPushButton()
but.setText("Згенерувати")

lineV = QVBoxLayout()
lineV.addWidget(text ,alignment= Qt.AlignCenter) 
lineV.addWidget(text2 ,alignment= Qt.AlignCenter)
lineV.addWidget(but ,alignment= Qt.AlignCenter)
win.setLayout(lineV)

but.clicked.connect(rand)





































































win.show()
app.exec_()