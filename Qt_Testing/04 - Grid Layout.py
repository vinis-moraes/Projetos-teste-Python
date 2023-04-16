import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle("04 - Grid Layout")
window.setGeometry(600, 400, 480, 320)

layout = QGridLayout()
layout.addWidget(QPushButton('Button 1'), 0,0)
layout.addWidget(QPushButton('Button 2'), 0, 1)
layout.addWidget(QPushButton('Button 3'), 0, 2)
layout.addWidget(QPushButton('Button 4'), 1, 0)
layout.addWidget(QPushButton('Button 5'), 1, 1)
layout.addWidget(QPushButton('Button 6'), 1, 2)
layout.addWidget(QPushButton('Button 7'), 2, 0, 1, 3)


window.setLayout(layout)

window.show()
sys.exit(app.exec())