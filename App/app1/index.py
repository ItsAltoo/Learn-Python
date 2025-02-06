from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle("Aplikasi PyQt6")
window.setGeometry(100, 100, 400, 300)

label = QLabel("Halo, Malik!", window)
label.move(150, 130)

window.show()
app.exec()
