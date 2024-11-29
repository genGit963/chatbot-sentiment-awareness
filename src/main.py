# bootstraper.py
import uvicorn
from src.app.app import app  # Correct path to import the FastAPI app

def bootstrap():
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

bootstrap()
