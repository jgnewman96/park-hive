"""
Simple HTTP server to interact with python backend
"""
import logging
import os
from typing import Any, Dict, List, Tuple

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend_server.src.directory import Directory, Post
from backend_server.src.markdown_file import MarkdownFile

LOGGER = logging.getLogger(__name__)


app = FastAPI()
directory = Directory.create_directory("writing_content", "img/books")

origins = [
    "https://localhost:8080",
    "http://localhost:8080",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_file")
def get_file(link_path: str) -> Dict[str, Any]:
    post = directory.get_post_by_link_path(link_path)
    file = MarkdownFile(post.file_path)

    return {"metadata": post.metadata, "file": file.render()}


@app.get("/get_posts_by_medium")
def get_posts_by_medium(medium: str) -> List[Post]:
    return directory.get_posts_by_medium(medium)


@app.get("/get_posts_by_subject")
def get_posts_by_subject(subject: str) -> List[Post]:
    return directory.get_posts_by_subject(subject)


@app.get("/get_recent_posts")
def get_recent_posts(number_of_posts: int) -> List[Post]:
    return directory.get_recent_posts(number_of_posts)


@app.get("/get_book_images")
def get_book_images() -> List[Tuple[str, str]]:
    return directory.get_book_images()
