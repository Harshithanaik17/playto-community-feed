from django.urls import path
from .views import HealthView
from .views import PostDetailView, LikePostView, LeaderboardView

urlpatterns = [
    path("posts/<int:post_id>/", PostDetailView.as_view()),
    path("posts/<int:post_id>/like/", LikePostView.as_view()),
    path("leaderboard/", LeaderboardView.as_view()),
    path("", HealthView.as_view())
]
