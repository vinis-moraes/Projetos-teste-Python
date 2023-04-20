import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle('05 - Form Layout')

layout = QFormLayout()
layout.addRow("Name", QLineEdit())
layout.addRow("Age", QLineEdit())
layout.addRow("Job", QLineEdit())
layout.addRow("Hobbies", QLineEdit())
layout.addWidget(QPushButton('Submit'))
window.setLayout(layout)

window.show()
sys.exit(app.exec())