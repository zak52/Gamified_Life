from fastapi import FastAPI
from db import db  # Import your database connection

app = FastAPI(
    title="Habit Tracker Backend",
    description="API for the Gamified Habit Tracking App",
    version="0.1.0"
)

@app.get("/")
async def read_root():
    return {"message": "Backend is running!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/test_db")
async def test_db():
    # List collection names as a simple test
    collections = await db.list_collection_names()
    return {"collections": collections}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)