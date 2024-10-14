from fastapi import FastAPI
from contextlib import asynccontextmanager

# from routers.api import router # add this later
from utils import create_tables


app = FastAPI(
    debug=True,
    title="Tutorial",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


# app.include_router(router)


