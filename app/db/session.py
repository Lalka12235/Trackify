from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    url=settings.db_url,
    echo=True
)

Session = sessionmaker(bind=engine)