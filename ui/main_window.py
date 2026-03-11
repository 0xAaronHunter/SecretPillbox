from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QListWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout
)
from PyQt5.QtCore import Qt
from crypto.password_generator import PasswordGenerator


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("APasswordManager")
        self.resize(900,500)

        # Build UI components and layout
        self.setup_ui()
    

    def setup_ui(self):

        central_widget = QWidget()
        main_layout = QHBoxLayout()

        # --- Left side: Vault list ---

        self.vault_list = QListWidget()
        self.vault_list.setMinimumWidth(250)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Saved Entries"))
        left_layout.addWidget(self.vault_list)

        left_panel = QWidget()
        left_panel.setLayout(left_layout)

        # --- Right side: Entry details and actions ---

        self.site_input = QLineEdit()
        self.username_input = QLineEdit()

        # Output field is read-only for auto-generated passwords
        self.password_output = QLineEdit("Click to generate a secure password")
        self.password_output.setReadOnly(True)
        self.password_output.setAlignment(Qt.AlignCenter)

        form_layout = QFormLayout()
        form_layout.addRow("Site:", self.site_input)
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_output)

        # --- Buttons ---

        self.generate_button = QPushButton("Generate Secure Password")
        self.generate_button.clicked.connect(self.generate_password)

        self.copy_button = QPushButton("Copy Password")
        self.copy_button.clicked.connect(self.copy_password)

        self.save_button = QPushButton("Save Entry")
        # Hook to persistence later; currently placeholder
        # self.save_button.clicked.connect(self.save_entry) --- IGNORE ---

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.save_button)

        right_layout = QVBoxLayout()
        right_layout.addLayout(form_layout)
        right_layout.addLayout(button_layout)
        right_layout.addStretch

        right_panel = QWidget()
        right_panel.setLayout(right_layout)

        # --- Main layout ---

        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


    def generate_password(self):
        password = PasswordGenerator.generate()
        self.password_output.setText(password)

    def copy_password(self):
        # Copy generated password to clipboard on demand
        password = self.password_output.text().strip()
        if not password or password == "Click to generate a secure password":
            self.statusBar().showMessage("Generate a password first", 3000)
            return

        QApplication.clipboard().setText(password)
        self.statusBar().showMessage("Password copied to clipboard", 3000)