import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


app = QApplication([])
window = QWidget()
window.setWindowTitle('Second application')
window.setGeometry(600, 400, 480, 320)

layout = QHBoxLayout()
layout.addWidget(QPushButton("Teste 1"))
layout.addWidget(QPushButton("Teste 2"))
layout.addWidget(QPushButton("Teste 3"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())