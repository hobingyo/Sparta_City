from rest_framework import serializers
from user.models import User, UserProfile
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


class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = UserProfile
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    comment_set = CommentSerializer(many=True)
    article_set = ArticleSerializer(many=True)
    like_set = LikeSerializer(Many=True)
    class Meta:
        # serializer에 사용될 model, field지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용

        fields = ['username', 'userprofile', 'article_set', 'comment_set', 'like_set']
