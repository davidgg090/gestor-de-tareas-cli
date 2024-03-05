import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()


if not os.getenv("DATABASE_URL"):
    raise ValueError("DATABASE_URL environment variable is not set")


engine = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()
Session = sessionmaker(bind=engine)
