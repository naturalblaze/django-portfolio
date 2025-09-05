"""Application URLs for portfolio_blog app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("<slug:slug>/", views.PostView.as_view(), name="post_single"),
]
