from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.utils.setting import setting

# DATABASE_URL = "sqlite:///./safeher.db"

engine = create_engine(url=setting.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()