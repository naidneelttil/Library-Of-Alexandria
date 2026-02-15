from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class BookStatus(str, Enum):
    CheckedOut = "CheckedOut"
    Available = "Available"
    OnHold = "OnHold"


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    isbn: str = Field(unique=True)
    copies: int = Field(default=1)
    status: BookStatus = Field(default=BookStatus.Available)
