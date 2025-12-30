#
#   Imports
#



# Perso

from core.shared.ports.user_db_port import UserDBPort

#
#   Services
#

class AuthService:
    """
        Service for authentication and authorization.

        Connects the user to the app using the database data.
    """
    def __init__(self, user_db_port: UserDBPort):
        self._user_db_port = user_db_port

    def register(self, email: str, password: str, pseudo: str) -> User:
        user = self._user_db_port.by_email(email)
        if user:
            raise ValueError("User already exists")
        user = User(email=email, password=password, pseudo=pseudo)
        self._user_db_port.create_user(user)

    def login(self, email: str, pwd: str) -> User: