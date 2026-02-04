from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "content", "author", "children"]

    def get_children(self, obj):
        return CommentSerializer(
            getattr(obj, "children_list", []),
            many=True
        ).data

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "content", "author", "comments"]

    def get_comments(self, obj):
        return CommentSerializer(
            self.context["comments"],
            many=True
        ).data
