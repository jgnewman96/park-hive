import os
from datetime import date
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

import frontmatter
from aenum import MultiValueEnum
from pydantic import BaseModel


class Medium(MultiValueEnum):
    PAPER = ("paper", "papers")
    BOOK = ("book", "books")
    INDUSTRY = "industry"
    RESEARCH = "research"
    TALKS = "talks"
    TEXTBOOKS = "textbooks"
    PERSONAL = "personal"


class Subject(MultiValueEnum):
    DEEPLEARNING = ("deep learning", "deep_learning")
    REINFORCEMENTLEARNING = ("reinforcement learning", "reinforcement_learning")
    MACHINELEARNING = ("machine learning", "machine_learning")
    SOFTWAREENGINEERING = ("software engineering", "software_engineering")
    ACADEMIA = "academia"
    ECONOMICS = "economics"
    STATISTICS = "statistics"
    DESIGN = "design"
    HISTORY = "history"
    NATURE = "nature"
    HEALTH = "health"
    FRISBEE = "frisbee"
    MINDFULNESS = "mindfulness"
    HOUSINGPOLICY = ("housing policy", "housing_policy")
    LEGALPOLICY = ("legal policy", "legal_policy")
    TECHPOLICY = ("tech policy", "tech_policy")
    TRANSPORTATIONPOLICY = ("transportation policy", "transporation_policy")
    AIPOLICY = ("ai policy", "ai_policy")
    POlITICS = "politics"
    RACE = "race"
    FICTION = "fiction"
    SCIENCEFICTION = ("science fiction", "science_fiction")
    NONFICTION = ("non-fiction", "non fiction")
    REFLECTION = ("reflection", "reflections")
    RESOURCE = "resource"


class PostMetaData(BaseModel):
    title: str
    date_published: date
    date_published_str: str
    medium: Medium
    subjects: List[Subject]

    @staticmethod
    def parse_frontmatter(frontmatter: Dict[str, Any]) -> "PostMetaData":

        title = frontmatter["title"]
        date_published = frontmatter["date"]
        date_published_str = date_published.strftime("%B %d %Y")
        medium = frontmatter["categories"][0].lower()
        subjects = [Subject(s.lower()) for s in frontmatter["tags"]]
        return PostMetaData(
            title=title,
            date_published=date_published,
            date_published_str=date_published_str,
            medium=medium,
            subjects=subjects,
        )


class Post(BaseModel):
    file_path: str
    link_path: str
    image_path: Optional[str]
    metadata: PostMetaData


class Directory:
    def __init__(self, posts: Dict[str, Post], current_books):
        self.posts = posts
        self.current_books = current_books

    def get_book_images(
        self,
    ) -> List[Tuple[str, str]]:
        book_images_dict: Dict[str, List[str]] = {"CURRENT": self.current_books}
        for _, post in self.posts.items():
            if post.metadata.medium == Medium.BOOK and post.image_path:
                year = post.metadata.date_published.year
                book_images_dict[year] = book_images_dict.get(year, []) + [
                    post.image_path
                ]
            else:
                continue

        return list(book_images_dict.items())

    def get_post_by_link_path(self, link_path: str) -> Post:
        return self.posts[link_path]

    def get_posts_by_medium(self, medium: str) -> List[Post]:
        return [p for _, p in self.posts.items() if p.metadata.medium.value == medium]

    def get_posts_by_subject(self, subject: str) -> List[Post]:
        return [
            p for _, p in self.posts.items() if Subject(subject) in p.metadata.subjects
        ]

    def get_recent_posts(self, number_of_posts: int) -> List[Post]:
        posts = []
        for i, key in enumerate(self.posts):
            posts.append(self.posts[key])
            if i == number_of_posts:
                break
        return posts

    @staticmethod
    def create_directory(writing_dir: str, book_image_dir: str) -> "Directory":

        posts = Directory._parse_files(writing_dir)
        book_images, current_books = Directory._parse_book_images(book_image_dir)

        # sorting posts by when they were written in descending order
        posts = sorted(posts, key=lambda x: x.metadata.date_published, reverse=True)
        posts_dict = {p.link_path: p for p in posts}

        for post_link, post in posts_dict.items():
            if post.metadata.medium == Medium.BOOK:
                try:
                    post.image_path = book_images[post_link]
                except KeyError:
                    print(f"Could not find Image for {post_link}", flush=True)
                    continue

        return Directory(posts_dict, current_books)

    @staticmethod
    def _parse_book_images(directory: str) -> Tuple[List[str], List[str]]:
        files = os.listdir(directory)
        book_images: Dict[str, str] = {}
        current_books: List[str] = []
        for file in files:
            year_path = os.path.join(directory, file)
            for img in os.listdir(year_path):
                if file == "current":
                    current_books.append(os.path.join(year_path, img))
                else:
                    book_images[img.split(".")[0]] = os.path.join(year_path, img)

        return book_images, current_books

    @staticmethod
    def _parse_files(directory: str) -> List[Post]:
        files = os.listdir(directory)
        posts: List[Post] = []
        for file in files:
            full_path = os.path.join(directory, file)
            if os.path.isdir(full_path):
                posts = posts + Directory._parse_files(os.path.join(directory, file))
            else:
                if file.endswith(".md"):
                    link_path = file[:-3]
                    post = frontmatter.load(full_path)

                    posts.append(
                        Post(
                            link_path=link_path,
                            file_path=full_path,
                            metadata=PostMetaData.parse_frontmatter(post),
                        )
                    )
        return posts
