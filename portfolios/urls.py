"""Defines URL patterns for portfolios."""

from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # List all portfolio item.
    path('portfolios/', views.portfolios, name='portfolios'),
    # Detail page for a single portfolio item.
    path('portfolios/<int:portfolio_id>/', views.portfolio, name='portfolio'),
]
