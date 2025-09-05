"""Script to populate the database with fake blog posts."""

from scripts.factory import PostFactory


def run() -> None:
    """
    Populates the database with some fake blog posts.
    """
    # Create 10 unique blog posts
    PostFactory.create_batch(100)
    print("Database successfully populated with 100 blog posts!")
