from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Assuming your models are defined using the declarative base method
Base = declarative_base()

def initialize_database():
    # Load environment variables from .env file
    load_dotenv()

    # Get the database URL from the environment variable
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Create a session local class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create all tables stored in this metadata
    Base.metadata.create_all(bind=engine)

    print("Database initialized!")

