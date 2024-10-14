from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from router import router
from utils import create_tables


app = FastAPI(
    debug=True,
    title="Tutorial",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
