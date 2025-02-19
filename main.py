from fastapi import FastAPI
from modules import items, users
from database import engine
import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "FastAPI CRUD with Items and Users"}
