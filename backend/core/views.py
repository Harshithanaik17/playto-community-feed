from django.db.models import Prefetch
from django.db import transaction, IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment, Like
from .serializers import PostSerializer
from .services.comments import build_comment_tree
from .services.leaderboard import get_leaderboard

class PostDetailView(APIView):
    def get(self, request, post_id):
        post = (
            Post.objects
            .select_related("author")
            .prefetch_related(
                Prefetch(
                    "comments",
                    queryset=Comment.objects.select_related("author").order_by("created_at")
                )
            )
            .get(id=post_id)
        )

        tree = build_comment_tree(list(post.comments.all()))
        serializer = PostSerializer(post, context={"comments": tree})
        return Response(serializer.data)

class LikePostView(APIView):
    def post(self, request, post_id):
        try:
            with transaction.atomic():
                Like.objects.create(
                    user=request.user,
                    post_id=post_id
                )
        except IntegrityError:
            return Response(
                {"detail": "Already liked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"status": "liked"})

class LeaderboardView(APIView):
    def get(self, request):
        return Response(get_leaderboard())
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
