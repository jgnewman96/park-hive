import os
from datetime import date
from enum import Enum
from typing import Any, Dict, List

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
    metadata: PostMetaData


class Directory:
    def __init__(self, posts: Dict[str, Post]):
        self.posts = posts

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
    def create_directory(base_dir: str) -> "Directory":

        posts = Directory._parse_files(base_dir)

        # sorting posts by when they were written in descending order
        posts = sorted(posts, key=lambda x: x.metadata.date_published, reverse=True)
        posts_dict = {p.link_path: p for p in posts}

        return Directory(posts_dict)

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
