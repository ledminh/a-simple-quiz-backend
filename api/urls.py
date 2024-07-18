from django.urls import path
from .views import get_questions, update_leaderboard, get_leaderboard

urlpatterns = [
    path('questions/', get_questions),
    path('leaderboard/', get_leaderboard),
    path('update-leaderboard/', update_leaderboard),
]
