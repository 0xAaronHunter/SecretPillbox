import sys
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.login_window import require_login


def main():
    """Application entry point."""

    print("Starting APasswordManager")

    app = QApplication(sys.argv)

    # Require authentication before opening vault
    authenticated = require_login()

    if not authenticated:
        sys.exit(0)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()