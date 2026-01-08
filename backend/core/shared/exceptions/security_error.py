"""
    Wrapper for security related errors instead of using
    ValueError for instance because it is caught by the route instead
    of the global error handler.
"""

#
#   Exceptions
#

class SecurityError(Exception):
    """
        Exception raised when a security error occurs.
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return f"SecurityError: {self.message}"