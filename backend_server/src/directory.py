import os
from typing import Dict

from pydantic import BaseModel


class Post(BaseModel):
    file_path: str
    link_path: str


class Directory:
    def __init__(self, posts: Dict[str, Post]):
        self.posts = posts

    def get_filename(self, link_path: str) -> str:
        return self.posts[link_path].file_path

    @staticmethod
    def create_directory(base_dir: str) -> "Directory":

        posts = Directory._parse_files(base_dir)
        return Directory(posts)

    @staticmethod
    def _parse_files(directory: str) -> Dict[str, Post]:
        files = os.listdir(directory)
        posts: Dict[str, Post] = {}
        for file in files:
            full_path = os.path.join(directory, file)
            if os.path.isdir(full_path):
                posts = posts | Directory._parse_files(os.path.join(directory, file))
            else:
                if file.endswith(".md"):
                    link_path = file[:-3]
                    posts[link_path] = Post(link_path=link_path, file_path=full_path)
        return posts
