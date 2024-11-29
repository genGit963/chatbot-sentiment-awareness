# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_server():
    return {"message": "There is nothing to worry much !!"}
