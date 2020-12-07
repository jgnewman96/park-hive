"""
Simple HTTP server to interact with python backend
"""
import logging
from typing import List
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI


LOGGER = logging.getLogger(__name__)


app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_notes")
def get_notes() -> List[str]:
    return ["Page 1", "Page 2"]
