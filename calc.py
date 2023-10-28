from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
app = QApplication([])
window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(500,500)
window.move(300,300)

def suma1():
    global f1
    global dia
    f1 = int(text.text())
    text.setText("")
    dia = 1
def vidni1():
    global f1
    global dia
    f1 = int(text.text())
    text.setText("")
    dia = 2
def dilena1():
    global f1
    global dia
    f1 = int(text.text())
    text.setText("")
    dia = 3
def mnod1():
    global f1
    global dia
    f1 = int(text.text())
    text.setText("")
    dia = 4

def one1():
    text.setText(text.text()+"1")
def two1():
    text.setText(text.text()+"2")
def three1():
    text.setText(text.text()+"3")
def four1():
    text.setText(text.text()+"4")
def five1():
    text.setText(text.text()+"5")
def six1():
    text.setText(text.text()+"6")
def seven1():
    text.setText(text.text()+"7")
def eight1():
    text.setText(text.text()+"8")
def ninev1():
    text.setText(text.text()+"9")
def zero1():
    text.setText(text.text()+"0")


def equal1():
    f2 = int(text.text())
    if dia == 1:
        text.setText(str(f1+f2))
    if dia == 2:
        text.setText(str(f1-f2))
    if dia == 3:
        text.setText(str(f1/f2))
    if dia == 4:
        text.setText(str(f1*f2))

text = QLineEdit()
suma = QPushButton()
suma.setText("Сума")

vidni=QPushButton()
vidni.setText("-")

dilena=QPushButton()
dilena.setText("/")

mnod=QPushButton()
mnod.setText("*")

equal = QPushButton()
equal.setText("=")

one = QPushButton()
one.setText("1")
two = QPushButton()
two.setText("2")
three = QPushButton()
three.setText("3")
four = QPushButton()
four.setText("4")
five = QPushButton()
five.setText("5")
six = QPushButton()
six.setText("6")
seven = QPushButton()
seven.setText("7")
eight = QPushButton()
eight.setText("8")
ninev = QPushButton()
ninev.setText("9")
zero = QPushButton()
zero.setText("0")





















vl = QVBoxLayout()
hl1 = QHBoxLayout()
hl2 = QHBoxLayout()
hl3 = QHBoxLayout()
hl4 = QHBoxLayout()
hl5 = QHBoxLayout()
hl6 = QHBoxLayout()
hl7 = QHBoxLayout()

hl1.addWidget(text)

hl2.addWidget(suma)
hl2.addWidget(equal)
hl2.addWidget(vidni)
hl2.addWidget(dilena)
hl2.addWidget(mnod)

hl3.addWidget(one)
hl3.addWidget(two)

hl4.addWidget(three)
hl4.addWidget(four)

hl5.addWidget(five)
hl5.addWidget(six)

hl6.addWidget(seven)
hl6.addWidget(eight)

hl7.addWidget(ninev)
hl7.addWidget(zero)




vl.addLayout(hl1)
vl.addLayout(hl2)
vl.addLayout(hl3)
vl.addLayout(hl4)
vl.addLayout(hl5)
vl.addLayout(hl6)
vl.addLayout(hl7)



suma.clicked.connect(suma1)
vidni.clicked.connect(vidni1)
dilena.clicked.connect(dilena1)
mnod.clicked.connect(mnod1)
one.clicked.connect(one1)
two.clicked.connect(two1)
three.clicked.connect(three1)
four.clicked.connect(four1)
five.clicked.connect(five1)
six.clicked.connect(six1)
seven.clicked.connect(seven1)
eight.clicked.connect(eight1)
ninev.clicked.connect(ninev1)
zero.clicked.connect(zero1)




equal.clicked.connect(equal1)


window.setLayout(vl)
window.show()
app.exec_()