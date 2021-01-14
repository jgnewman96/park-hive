"""
Simple HTTP server to interact with python backend
"""
import logging
from typing import Any, Dict, List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.directory import Directory, Post
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
