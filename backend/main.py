import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

# Must be called BEFORE importing backend.routes
load_dotenv()

from backend.routes import router

app = FastAPI(title="LegalEase API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "LegalEase Backend API Running"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)