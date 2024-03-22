from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
import logging
from .database import SessionLocal, engine
from .db_init import initialize_database
from .schemas import EventBase

initialize_database()
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add events to the database
"""
@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    logger.info(f"Event created with ID: {db_event.id}")
    return db_event"""

@app.get("/events/", response_model=List[EventBase])
def read_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events
