"""Configuration file for pytest to set up the testing environment."""

from pytest_factoryboy import register
from .factories import (
    PortfolioFactory,
    ProjectFactory,
    ResumeSkillsFactory,
    ResumeJobsFactory,
    ResumeEducationFactory,
    ResumeCertificationsFactory,
)

register(PortfolioFactory)
register(ProjectFactory)
register(ResumeSkillsFactory)
register(ResumeJobsFactory)
register(ResumeEducationFactory)
register(ResumeCertificationsFactory)
