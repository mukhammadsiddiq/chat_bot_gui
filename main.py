from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)

        # add chat area widget

        self.text_area = QTextEdit(self)
        self.text_area.setGeometry(10, 10, 480, 340)
        self.text_area.setReadOnly(True)
        # add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        self.button = QPushButton("send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())


