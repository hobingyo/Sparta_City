from django.contrib import admin
from article.models import Article, Comment, Like, Categories

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Categories)