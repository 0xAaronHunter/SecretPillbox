from crypto.authentication_manager import AuthManager


def require_login():
    """Expose a single login entrypoint for UI"""
    return AuthManager.require_login()
