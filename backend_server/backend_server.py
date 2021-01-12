"""
Simple HTTP server to interact with python backend
"""
import logging
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.directory import Directory
from src.markdown_file import MarkdownFile

LOGGER = logging.getLogger(__name__)


app = FastAPI()
directory = Directory.create_directory("writing_content")

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


@app.get("/get_file")
def get_file(link_path: str) -> str:
    filename = directory.get_filename(link_path)
    file = MarkdownFile(filename)

    return file.render()
