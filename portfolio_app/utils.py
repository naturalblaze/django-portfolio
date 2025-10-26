"""Utilities for portfolio_app app"""

from typing import Dict
import toml


def get_project_dependencies(file_path: str = "pyproject.toml") -> Dict[str, str]:
    """
    Extracts the 'dependencies' from the [project] table in a pyproject.toml file.

    Args:
        file_path (str): The path to the pyproject.toml file.

    Returns:
        Dict[str, str]: List of dependencies with their versions and github_url if available.
    """
    try:
        dependencies = {}
        with open(file_path, "r", encoding="utf-8") as f:
            data = toml.load(f)

        for value in data.get("project", {}).get("dependencies", []):
            dependencies[value.split(">=")[0]] = value.split(">=")[1]

        for value in data.get("dependency-groups", {}).get("prod", []):
            dependencies[value.split(">=")[0]] = value.split(">=")[1]

        dependencies["github_url"] = data.get("project", "").get("urls", "").get("Source", "")

        return dependencies

    except Exception:  # pylint: disable=broad-except
        return {}
