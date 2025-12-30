#
#   Imports
#

from abc import ABC, abstractmethod

# Perso

from core.shared.models.user import User

#
#   Ports
#

class UserDBPort(ABC):
    @abstractmethod
    def by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> None:
        pass
