from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_ALCHEMY_DATABASE_URL = "sqlite:///refbot.db"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, pool_size=20, max_overflow=10)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
