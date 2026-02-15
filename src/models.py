from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Checkout(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")
    checked_out_at: datetime = Field(default_factory=datetime.utcnow)
    returned_at: Optional[datetime] = None


class Hold(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")
    placed_at: datetime = Field(default_factory=datetime.utcnow)
