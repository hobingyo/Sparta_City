from django.db import models
from user.models import User

from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey("user.User", verbose_name="게시글 작성자", on_delete=models.CASCADE)
    title = models.CharField(("글 제목"), max_length=200)
    body = models.CharField(("글 내용"), max_length=1000)
    # 카테고리는 한개만 선택 가능하게해서 외부키로
    categories = models.ForeignKey('Categories')
    like_users = models.ManyToManyField('Like')
    thumbnail = models.FileField(("썸네일"), )
    post_date = models.DateTimeField(("등록시간"), auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.user.username}의 게시글입니다.'


class Like(models.Model):
    user = models.ForeignKey("user.User", verbose_name="라이크한 유저", on_delete=models.CASCADE)
    articles = models.ManyToManyField('Article')

    def __str__(self):
        return f'{self.user.username}님이 {self.articles.title}를 좋아합니다.'

class Comment(models.Model):
    user = models.ForeignKey('user.User', verbose_nam="댓글 작성자", on_delete=models.CASCADE)
    articles = models.ForeignKey('Article', verbose_name="게시글", on_delete=models.CASCADE)
    comments = models.CharField(('댓글 내용'), max_length=200)

    def __str__(self):
        return f'{self.user.username}님의 댓글입니다.'


class Categories(models.Model):
    categories = models.CharField(("카테고리 이름"), max_length=50, unique=True)
    description = models.CharField(("카테고리 설명"), max_length=200)

    def __str__(self):
        return self.categories




