#
#   Imports
#

# Perso

from pydantic import BaseModel
from core.shared.exceptions.conversion_error import (
    ConversionType,
    ConversionError
)

from adapters.shared.db.base import Base
from typing import Type, TypeVar

#
#   Utils
#

T = TypeVar("T")

def _error_handler(error: Exception, type: ConversionType) -> None:
    """
        Handle an error.
    """
    raise ConversionError(error, type)

def orm_to_model(orm_model: Base, model_type: Type[T]) -> T:
    """
        Convert an ORM to a model.

        Removes private attributes to avoid mismatching attributes.

        For instance, UserORM to User.
    """
    try:
        kwargs = {
            k: v
            for k, v in orm_model.__dict__.items()
            if not k.startswith("_") and
            not k.startswith("created_at") and
            not k.startswith("updated_at")
        }

        return model_type(**kwargs)

    except Exception as e:
        _error_handler(e, ConversionType.ORM_TO_MODEL)
        raise

def model_to_orm(model: object, orm_type: Type[Base]) -> Base:
    """
        Convert a model to an ORM.
    
        Removes private attributes to avoid mismatching attributes.
        
        For instance, User to UserDTO.
    """
    try:
        kwargs = {
            k: v
            for k, v in model.__dict__.items()
            if not k.startswith("_")
        }

        return orm_type(**kwargs)
    except Exception as e:
        _error_handler(e, ConversionType.MODEL_TO_ORM)
        raise

def pydantic_to_model(pydantic_model: BaseModel, model_type: Type[T]) -> T:
    """
        Convert a Pydantic model to a model.
    """
    try:
        kwargs = pydantic_model.model_dump()
        return model_type(**kwargs)
    except Exception as e:
        _error_handler(e, ConversionType.PYDANTIC_TO_MODEL)
        raise

def model_to_pydantic(
    model: object, pydantic_type: Type[BaseModel]
) -> BaseModel:
    """
        Convert a model to a Pydantic model.

        Removes private attributes to avoid mismatching attributes.

        For instance, User to UserDTO.
    """
    try:
        kwargs = {
            k: v
            for k, v in model.__dict__.items()
            if not k.startswith("_")
        }

        return pydantic_type(**kwargs)

    except Exception as e:
        _error_handler(e, ConversionType.MODEL_TO_PYDANTIC)
        raise

def orm_to_pydantic(
    orm_model: Base,
    pydantic_type: Type[BaseModel]
) -> BaseModel:
    """
        Convert an ORM to a Pydantic model.

        Removes private attributes to avoid mismatching attributes.

        For instance, UserORM to UserDTO.
    """
    try:
        return pydantic_type.model_validate(orm_model)
    except Exception as e:
        _error_handler(e, ConversionType.ORM_TO_PYDANTIC)
        raise

def pydantic_to_orm(
    pydantic_model: BaseModel,
    orm_type: Type[Base]
) -> Base:
    """
        Convert a Pydantic model to an ORM.

        Removes private attributes to avoid mismatching attributes.

        For instance, UserDTO to UserORM.
    """
    try:
        kwargs = pydantic_model.model_dump()
        return orm_type(**kwargs)
    except Exception as e:
        _error_handler(e, ConversionType.PYDANTIC_TO_ORM)
        raise