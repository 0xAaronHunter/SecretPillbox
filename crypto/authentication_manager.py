import sys
import hashlib
from pathlib import Path

from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLineEdit


APP_DIR = Path.home() / ".SecretPillbox"
PASSWORD = APP_DIR / "hashedSecret.txt"

# Gatekeeper
class AuthManager:

    @staticmethod
    def _ask_password(prompt: str) -> str:
        text, ok = QInputDialog.getText(
            None,
            "Password",
            prompt,
            QLineEdit.Password
        )

        if not ok:
            sys.exit(0)

        return text.strip()

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha512(password.encode("utf-8")).hexdigest()

    @classmethod
    def setup_master_password(cls):

        APP_DIR.mkdir(parents=True, exist_ok=True)

        password = cls._ask_password("Set a new password:")

        if not password:
            QMessageBox.warning(None, "Error", " password cannot be empty")
            sys.exit(1)

        hashed_password = cls._hash_password(password)

        PASSWORD.write_text(hashed_password, encoding="utf-8")

        QMessageBox.information(
            None,
            "Setup Complete",
            "Password set. Restart the application."
        )

        sys.exit(0)

    @classmethod
    def require_login(cls):

        APP_DIR.mkdir(parents=True, exist_ok=True)

        if not PASSWORD.exists():
            cls.setup_master_password()

        stored_hash = PASSWORD.read_text(encoding="utf-8").strip()

        while True:

            attempt = cls._ask_password("Enter password:")

            if cls._hash_password(attempt) == stored_hash:
                return True

            QMessageBox.warning(None, "Invalid Password", "Wrong password. Try again.")