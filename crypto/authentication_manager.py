import sys
import hashlib
from pathlib import Path

from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLineEdit


APP_DIR = Path.home() / ".apasswordmanager"
MASTER_FILE = APP_DIR / "master.hash"


class AuthManager:

    @staticmethod
    def _ask_password(prompt: str) -> str:
        text, ok = QInputDialog.getText(
            None,
            "Master Password",
            prompt,
            QLineEdit.Password
        )

        if not ok:
            sys.exit(0)

        return text.strip()

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @classmethod
    def setup_master_password(cls):

        APP_DIR.mkdir(parents=True, exist_ok=True)

        password = cls._ask_password("Set a new master password:")

        if not password:
            QMessageBox.warning(None, "Error", "Master password cannot be empty")
            sys.exit(1)

        hashed = cls._hash_password(password)

        MASTER_FILE.write_text(hashed, encoding="utf-8")

        QMessageBox.information(
            None,
            "Setup Complete",
            "Master password set. Restart the application."
        )

        sys.exit(0)

    @classmethod
    def require_login(cls):

        APP_DIR.mkdir(parents=True, exist_ok=True)

        if not MASTER_FILE.exists():
            cls.setup_master_password()

        stored_hash = MASTER_FILE.read_text(encoding="utf-8").strip()

        while True:

            attempt = cls._ask_password("Enter master password:")

            if cls._hash_password(attempt) == stored_hash:
                return True

            QMessageBox.warning(None, "Invalid Password", "Wrong password. Try again.")