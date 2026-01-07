#
#   Imports
#

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Perso

from adapters.shared.utils.conversion_utils import model_to_orm, orm_to_model
from core.shared.ports.user_db_port import UserDBPort
from adapters.shared.db.orms.user_orm import User as UserORM
from core.shared.models.user import User

#
#   Repositories
#

class UserRepo(UserDBPort):
    """
        Repository for user operations.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def by_id(self, user_id: int) -> User:
        """
            Gets a User by id.

            If there is no user, raises ValueError.
        """
        query = select(UserORM).where(UserORM.id == user_id)
        
        result = await self.session.execute(query)

        user_orm = result.scalar_one_or_none()
        if user_orm is None:
            raise ValueError(f"User with id {user_id} not found")

        return orm_to_model(user_orm, User)

    async def by_email(self, email: str) -> User:
        """
            Gets a User by email.

            If there are multiple raises MultipleResultsFoundError.

            If there is no user, raises ValueError.
        """
        query = select(UserORM).where(UserORM.email == email)

        result = await self.session.execute(query)

        user_orm = result.scalar_one_or_none()
        if user_orm is None:
            raise ValueError(f"User with email {email} not found")

        return orm_to_model(user_orm, User)

    async def create_user(self, user: User) -> None:
        """
            Creates a new User in the db.

            Checks if the email is already in use.
        """
        user_orm = model_to_orm(user, UserORM)

        try:
            await self.by_email(user.email)
        except ValueError:
            self.session.add(user_orm)

            await self.session.commit()

            return

        raise ValueError(f"User with email {user.email} already exists")