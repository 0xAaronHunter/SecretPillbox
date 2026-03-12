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
    QFormLayout,
    QCheckBox
)
from PyQt5.QtCore import Qt
from crypto.password_generator import PasswordGenerator


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SecretPillbox – Password Manager")
        self.resize(900, 500)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        vault_panel = self._create_vault_panel()
        editor_panel = self._create_editor_panel()

        main_layout.addWidget(vault_panel)
        main_layout.addWidget(editor_panel)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self._apply_styles()

    def _create_vault_panel(self):
        self.entry_list = QListWidget()
        self.entry_list.setMinimumWidth(250)

        left_layout = QVBoxLayout()
        left_layout.setSpacing(8)
        left_layout.addWidget(QLabel("Saved Entries"))
        left_layout.addWidget(self.entry_list)

        vault_panel = QWidget()
        vault_panel.setLayout(left_layout)
        return vault_panel

    def _create_editor_panel(self):
        self.site_field = QLineEdit()
        self.username_field = QLineEdit()

        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Generate Password")
        self.password_field.setReadOnly(True)
        self.password_field.setAlignment(Qt.AlignCenter)

        form_layout = QFormLayout()
        form_layout.addRow("Site:", self.site_field)
        form_layout.addRow("Username:", self.username_field)
        form_layout.addRow("Password:", self.password_field)

        checkbox_layout = self._create_password_options_panel()

        button_layout = self._create_buttons_panel()

        right_layout = QVBoxLayout()
        right_layout.setSpacing(12)
        right_layout.addLayout(form_layout)
        right_layout.addLayout(checkbox_layout)
        right_layout.addLayout(button_layout)
        right_layout.addStretch()

        editor_panel = QWidget()
        editor_panel.setLayout(right_layout)
        return editor_panel

    def _create_password_options_panel(self):
        checkbox_layout = QVBoxLayout()
        checkbox_layout.addWidget(QLabel("Password Options:"))
        checkbox_layout.setSpacing(4)

        options = [
            ("Include Uppercase Letters", "uppercase_cb"),
            ("Include Lowercase Letters", "lowercase_cb"),
            ("Include Numbers", "digits_cb"),
            ("Include Symbols", "special_cb"),
        ]

        for label, attr in options:
            checkbox = QCheckBox(label)
            checkbox.setChecked(True)
            setattr(self, attr, checkbox)
            checkbox.stateChanged.connect(self.generate_password)
            checkbox_layout.addWidget(checkbox)

        return checkbox_layout

    def _create_buttons_panel(self):
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        self.copy_button = QPushButton("Copy Password")
        self.copy_button.clicked.connect(self.copy_password)

        self.save_button = QPushButton("Save Entry")
        # Hook to persistence later; currently placeholder
        # self.save_button.clicked.connect(self.save_entry)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.save_button)

        return button_layout

    def _apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #A8E6CF;
            }

            QLabel {
                color: #2B2D42;
                font-weight: bold;
            }

            QListWidget {
                background-color: #FFFFFF;
                border: 1px solid #DCE1E6;
                border-radius: 8px;
            }

            QListWidget::item:selected {
                background-color: #CFF5E6;
                color: #2B2D42;
            }

            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #DCE1E6;
                border-radius: 8px;
                padding: 6px;
                font-family: Consolas, Courier, monospace;
            }

            QLineEdit[readOnly="true"] {
                background-color: #F9FBFC;
            }

            QPushButton {
                background-color: #457B9D;
                color: white;
                border-radius: 16px;
                padding: 8px 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #2A9D8F;
            }

            QPushButton:pressed {
                background-color: #1E6F8C;
            }

            QCheckBox {
                color: #2B2D42;
            }
    """)

    def generate_password(self):
        options = {
            "include_uppercase": self.uppercase_cb.isChecked(),
            "include_lowercase": self.lowercase_cb.isChecked(),
            "include_digits": self.digits_cb.isChecked(),
            "include_special": self.special_cb.isChecked(),
        }

        password = PasswordGenerator.generate(**options)
        self.password_field.setText(password)
        self.password_field.setStyleSheet("""
            QLineEdit {
                background-color: #CFF5E6;
                border: 1px solid #DCE1E6;
                padding: 6px;
            }
        """)

    def copy_password(self):
        password = self.password_field.text().strip()

        if not password:
            self.statusBar().showMessage("Generate a password first", 3000)
            return

        QApplication.clipboard().setText(password)
        self.password_field.setStyleSheet("""
            QLineEdit {
                background-color: #d4ffd4;
                border: 1px solid #DCE1E6;
                padding: 4px;
            }
        """)
        self.statusBar().showMessage("Password copied to clipboard", 3000)


