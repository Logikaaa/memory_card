from PyQt5.QtWidgets import QWidget, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QVBoxLayout, QLabel

win_width = 600
win_height = 500

window = QWidget()
window.resize(win_width, win_height)
window.setWindowTitle('Memory Card')
window.move(300, 300)



RadioGroupBox = QGroupBox('Варіанти відповідей')

RadioGroup = QButtonGroup()

r1 = QRadioButton('1')
r2 = QRadioButton('2')
r3 = QRadioButton('3')
r4 = QRadioButton('4')

RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

l1 = QHBoxLayout()
l2 = QVBoxLayout()
l3 = QVBoxLayout()

l2.addWidget(r1)
l2.addWidget(r2)
l3.addWidget(r3)
l3.addWidget(r4)

l1.addLayout(l2)
l1.addLayout(l3)

RadioGroupBox.setLayout(l1)

main_line = QVBoxLayout()

question = QLabel('Питання')

main_line.addWidget(question)
main_line.addWidget(RadioGroupBox)

window.setLayout(main_line)
window.show()


