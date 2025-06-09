from fastapi import FastAPI

from app.backend.db import engine,Base

from app.routers.router import router

app=FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)