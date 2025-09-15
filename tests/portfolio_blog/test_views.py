"""Tests for views.py"""

import pytest
from django.urls import reverse
from django.test import Client
from portfolio_blog.models import PortfolioJobs, PortfolioSkills, PortfolioEducation, PortfolioCertifications


@pytest.mark.django_db
def test_portfolio_view_context():
    PortfolioJobs.objects.create(company="A", role="Dev", description="desc", projects="proj", start_date="2020-01-01")
    PortfolioSkills.objects.create(name="Python", proficiency=10)
    PortfolioEducation.objects.create(institution="Uni", degree="BSc", field_of_study="CS", start_date="2010-01-01")
    PortfolioCertifications.objects.create(name="Cert", issuing_organization="Org", issue_date="2022-01-01")
    client = Client()
    response = client.get(reverse("portfolio"))
    assert response.status_code == 200
    assert "skills" in response.context
    assert "educations" in response.context
    assert "certifications" in response.context


@pytest.mark.django_db
def test_project_view():
    client = Client()
    response = client.get(reverse("projects"))
    assert response.status_code == 200
