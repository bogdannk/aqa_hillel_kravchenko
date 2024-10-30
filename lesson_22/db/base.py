from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus


DATABASE_URL = "postgresql://bogdankravcenko:123postgres@localhost:5432/my_aqa_test_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()