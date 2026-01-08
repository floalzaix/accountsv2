#
#   Imports
#

import jwt

from datetime import datetime, timezone, timedelta
from typing import Any
from passlib.context import CryptContext

# Perso

from adapters.shared.config.config import get_settings
from core.shared.exceptions.security_error import SecurityError
#
#   Utils
#

settings = get_settings()

password_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    """
        Hashes a password using SHA-256.
    """
    return password_context.hash(password)

def verify_password(password: str, hash: str) -> bool:
    """
        Verifies a password against a hash using SHA-256.
    """
    return password_context.verify(password, hash)

def create_access_token(data: Any) -> str:
    """
        Creates an access token using the secret key and the algorithm.
    """
    return jwt.encode( # type: ignore
        {
            "sub": str(data),
            "exp": datetime.now(timezone.utc) +
            timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGO,
    )

def verify_access_token(token: str) -> Any:
    """
        Verifies an access token using the secret key and the algorithm.
    """
    try:
        payload: dict[str, Any] = jwt.decode( # type: ignore
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGO]
        )

        data: Any = payload.get("sub")

        if not data:
            raise SecurityError(f"Invalid token !")

        return data
    except jwt.ExpiredSignatureError:
        raise SecurityError(f"Token expired !")
    except Exception as e:
        raise SecurityError(f"Invalid token !") from e