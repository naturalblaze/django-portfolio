"""Application URLs for portfolio_app app"""

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("projects/", views.ProjectsView.as_view(), name="projects_all"),
    path("projects/<slug:slug>/", views.ProjectView.as_view(), name="project_single"),
    path("about/", views.AboutView.as_view(), name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
