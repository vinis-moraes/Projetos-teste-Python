import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Third application")
window.setGeometry(600, 400, 480, 320)

layout = QVBoxLayout()
layout.addWidget(QPushButton("Teste 1"))
layout.addWidget(QPushButton("Teste 2"))
layout.addWidget(QPushButton("Teste 3"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())