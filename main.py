import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.resize(600,400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.password_output = QLineEdit("Click to generate a secure password")
        self.password_output.setReadOnly(True)
        self.password_output.setAlignment(Qt.AlignCenter)
        self.generate_button = QPushButton("Generate Secure Password")
        self.save_button = QPushButton("Save Secure Password")

        layout.addStretch()
        layout.addWidget(self.password_output)
        layout.addStretch()
        layout.addWidget(self.generate_button)
        layout.addWidget(self.save_button)

        layout.setSpacing(5)
        layout.setContentsMargins(5,5,5,5)

        self.setLayout(layout)


def main():
    print("Starting")

    app = QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
