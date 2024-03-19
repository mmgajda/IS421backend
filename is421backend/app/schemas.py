from pydantic import BaseModel, Field, constr
from datetime import datetime

class EventBase(BaseModel):
    title: constr(strip_whitespace=True, min_length=3, max_length=100) = Field(..., example="My Event")
    description: constr(strip_whitespace=True, min_length=10, max_length=1000) = Field(..., example="Event Description")
    # constr - used to define constraints for string types
    # Field - can be used to add metadata to the fields
    # Add more fields as needed with appropriate validations

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
