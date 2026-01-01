#
#   Imports
#

from hashlib import sha256

#
#   Utils
#

def hash_password(password: str) -> str:
    """
        Hashes a password using SHA-256.
    """
    return sha256(password.encode()).hexdigest()

def verify_password(password: str, hash: str) -> bool:
    """
        Verifies a password against a hash using SHA-256.
    """
    return hash_password(password) == hash