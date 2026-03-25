from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from csv_analyser.api.routes import router


OUTPUT_DIR = Path("output")


def _ensure_output_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "images").mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "insights").mkdir(parents=True, exist_ok=True)


@asynccontextmanager
async def lifespan(_: FastAPI):
    _ensure_output_dirs()
    yield


app = FastAPI(
    title="CSV Analyser",
    version="0.1.0",
    description="FastAPI + Plotly general-purpose CSV analytics service.",
    lifespan=lifespan,
)
app.mount("/output", StaticFiles(directory="output"), name="output")
app.include_router(router)
