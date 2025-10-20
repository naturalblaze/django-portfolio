"""Script to populate the database with fake projects."""

from scripts.factory import ProjectFactory


def run(*args) -> None:
    """
    Populates the database with some fake blog projects.
    """
    if args and isinstance(int(args[0]), int) and int(args[0]) > 0:
        projects = int(args[0])
    else:
        projects = 20

    # Create unique projects
    ProjectFactory.create_batch(projects)
    print(f"Database successfully populated with {projects} projects!")
