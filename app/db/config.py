import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()


def create_engine():
    if os.getenv("DATABASE_URL"):
        return create_engine(os.getenv("DATABASE_URL"))
    else:
        raise ValueError("DATABASE_URL environment variable is not set")


engine = create_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
