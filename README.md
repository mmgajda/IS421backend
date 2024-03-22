# IS421backend utilizes the following:
- FastAPI
- SQLite DB
- SQLAlchemy
- pydantic
- Alembic

## To run:
- pip install -r requirements.txt
- python3 -m uvicorn main.app:app --host 127.0.0.1 --port 8000
- navigate to 127.0.0.1/8000/events/ for db or 127.0.0.1/8000/docs to see routes, etc.