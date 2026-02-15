from sqlmodel import Session, SQLModel, create_engine

from src.config import settings

engine = create_engine(settings.database_url)


def create_db_and_tables():
    from src.book import Book  # noqa: F401
    from src.user import User  # noqa: F401
    from src.models import Checkout, Hold  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
