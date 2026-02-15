from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: Optional[str] = None
    name: Optional[str] = None
    password: str
    library_card_number: str = Field(unique=True)
    permissions: str = Field(default="user")
