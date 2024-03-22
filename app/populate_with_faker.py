from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import os
from dotenv import load_dotenv
from app.models import Event, Base  # Assuming Event is in models.py

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(os.getcwd())

print(DATABASE_URL)

fake = Faker()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_fake_data(model, num_entries=100):
    session = Session()
    for _ in range(num_entries):
        if model == Event:
            entry = Event(
                title=fake.sentence(nb_words=6),
                description=fake.text(max_nb_chars=200),
                date=fake.future_date(end_date="+30d")
            )
            session.add(entry)
    session.commit()
    session.close()
    print(f"Inserted {num_entries} entries into {model.__tablename__}.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Ensure tables exist
    create_fake_data(Event, 100)  # Populate the 'events' table with 100 fake entries
