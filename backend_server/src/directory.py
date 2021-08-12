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
    LABORPOLICY = ("labor_policy", "labor policy")
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
    has_text: bool = True

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
            has_text=frontmatter.get("has_text", True),
        )


class Post(BaseModel):
    file_path: str
    link_path: str
    image_path: Optional[str]
    metadata: PostMetaData


class Directory:
    def __init__(
        self, posts: Dict[str, Post], book_images_by_year: Dict[str, List[str]]
    ):
        self.posts = posts
        self.book_images_by_year = book_images_by_year

    def get_book_images(
        self,
    ) -> List[Tuple[str, str]]:

        book_images_dict: Dict = {
            "CURRENT": [(img, False) for img in self.book_images_by_year["current"]]
        }
        for _, post in self.posts.items():
            if post.metadata.medium == Medium.BOOK and post.image_path:
                year = post.metadata.date_published.year
                book_images_dict[year] = book_images_dict.get(year, []) + [
                    (post.image_path, post.metadata.has_text)
                ]
            else:
                continue

        return list(book_images_dict.items())

    def get_post_by_link_path(self, link_path: str) -> Post:
        return self.posts[link_path]

    def get_posts_by_medium(self, medium: str) -> List[Post]:
        return [
            p
            for _, p in self.posts.items()
            if p.metadata.medium.value == medium and p.metadata.has_text
        ]

    def get_posts_by_subject(self, subject: str) -> List[Post]:
        return [
            p
            for _, p in self.posts.items()
            if Subject(subject) in p.metadata.subjects and p.metadata.has_text
        ]

    def get_recent_posts(self, number_of_posts: int) -> List[Post]:
        posts = []

        for key in self.posts:
            if self.posts[key].metadata.has_text:
                posts.append(self.posts[key])
            if len(posts) == number_of_posts:
                break
        return posts

    @staticmethod
    def create_directory(writing_dir: str, book_image_dir: str) -> "Directory":

        posts = Directory._parse_files(writing_dir)
        book_images_by_name, book_images_by_year = Directory._parse_book_images(
            book_image_dir
        )

        # sorting posts by when they were written in descending order
        posts = sorted(posts, key=lambda x: x.metadata.date_published, reverse=True)
        posts_dict = {p.link_path: p for p in posts}

        for post_link, post in posts_dict.items():
            if post.metadata.medium == Medium.BOOK:
                try:
                    post.image_path = book_images_by_name[post_link]
                except KeyError:
                    print(f"Could not find Image for {post_link}", flush=True)
                    continue

        return Directory(posts_dict, book_images_by_year)

    @staticmethod
    def _parse_book_images(directory: str) -> Tuple[Dict, Dict]:
        files = os.listdir(directory)
        book_images_by_name: Dict[str, str] = {}
        book_images_by_year: Dict[str, List[Tuple[str, float]]] = {}
        current_books: List[str] = []
        for file in files:
            year_path = os.path.join(directory, file)
            for img in os.listdir(year_path):
                book_images_by_name[img.split(".")[0]] = os.path.join(year_path, img)
                full_file_path = os.path.join(year_path, img)
                book_images_by_year[file] = book_images_by_year.get(file, []) + [
                    full_file_path
                ]
        return book_images_by_name, book_images_by_year

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
