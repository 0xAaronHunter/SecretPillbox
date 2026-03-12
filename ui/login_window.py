from crypto.authentication_manager import AuthManager


def require_login():
    return AuthManager.require_login()
