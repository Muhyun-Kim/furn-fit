from fastapi import FastAPI
from app.api import user
from app.db.session import engine
from app.db import base
import asyncio

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(base.Base.metadata.create_all)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
