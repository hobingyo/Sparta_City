from rest_framework import serializers
from article.models import Article, Comment, Like, Categories


class ArticleSerializer(serializers.ModelSerializer):
    articles_user = serializers.SerializerMethodField()

    def get_articles_user(self,obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ["title", "body", "articles_user"]

class CommentSerializer(serializers.ModelSerializer):
    comments_user = serializers.SerializerMethodField()

    def get_comments_user(self,obj):
        return obj.user.username
    class Meta:
        model = Comment
        fields = ["comments", "comments_user"]

class LikeSerializer(serializers.ModelSerializer):
    likes_user = serializers.SerializerMethodField()

    def get_likes_user(self,obj):
        return obj.user.username
    class Meta:
        model = Like
        fields = ["articles", "likes_user"]