"""Application URLs for portfolio_blog app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("posts/", views.PostsView.as_view(), name="posts_all"),
    path("posts/<slug:slug>/", views.PostView.as_view(), name="post_single"),
]
