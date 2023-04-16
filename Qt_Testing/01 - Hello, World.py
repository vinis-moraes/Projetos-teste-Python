import sys

from PyQt6.QtWidgets import  (
    QApplication,
    QLabel,
    QWidget,
    QPushButton, 
)

app = QApplication([])

window = QWidget()
window.setWindowTitle('First PyQt Application')
window.setGeometry(600, 600, 240, 240)
helloMsg = QLabel('<h1>Hello, World!</h1>', parent=window)
helloMsg.move(40, 100)
firstBtn = QPushButton('aa')
firstBtn.move(0,0)

window.show()

sys.exit(app.exec())