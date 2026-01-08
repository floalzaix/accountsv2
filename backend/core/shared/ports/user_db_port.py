#
#   Imports
#

import uuid

from abc import ABC, abstractmethod

# Perso

from core.shared.models.user import User

#
#   Ports
#

class UserDBPort(ABC):
    @abstractmethod
    async def by_id(self, user_id: uuid.UUID) -> User:
        pass

    @abstractmethod
    async def by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> None:
        pass
