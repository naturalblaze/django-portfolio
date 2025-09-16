"""Configuration file for pytest to set up the testing environment."""

from pytest_factoryboy import register
from .factories import (
    PostFactory,
    PortfolioSkillsFactory,
    PortfolioJobsFactory,
    PortfolioEducationFactory,
    PortfolioCertificationsFactory,
)

register(PostFactory)
register(PortfolioSkillsFactory)
register(PortfolioJobsFactory)
register(PortfolioEducationFactory)
register(PortfolioCertificationsFactory)
