#
#   Imports
#

from enum import Enum

#
#   Exceptions
#

class ConversionType(Enum):
    """
        Type of conversion error.
    """
    ORM_TO_MODEL = "orm_to_model"
    MODEL_TO_ORM = "model_to_orm"
    PYDANTIC_TO_ORM = "pydantic_to_orm"
    ORM_TO_PYDANTIC = "orm_to_pydantic"
    PYDANTIC_TO_MODEL = "pydantic_to_model"
    MODEL_TO_PYDANTIC = "model_to_pydantic"

class ConversionError(Exception):
    """
        Exception raised when a conversion error occurs.
    """
    def __init__(self, error: Exception, type: ConversionType):
        self._error = error
        self._type = type

    def __str__(self) -> str:
        return f"ConversionError: {self._error} ({self._type})"