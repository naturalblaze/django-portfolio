"""Configuration file for pytest to set up the testing environment."""

from pytest_factoryboy import register
from .factories import (
    PostFactory,
    ProjectFactory,
    PortfolioSkillsFactory,
    PortfolioJobsFactory,
    PortfolioEducationFactory,
    PortfolioCertificationsFactory,
)

register(PostFactory)
register(ProjectFactory)
register(PortfolioSkillsFactory)
register(PortfolioJobsFactory)
register(PortfolioEducationFactory)
register(PortfolioCertificationsFactory)
