# Generated by Django 4.0.5 on 2022-06-22 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='글 제목')),
                ('body', models.CharField(max_length=1000, verbose_name='글 내용')),
                ('thumbnail', models.FileField(upload_to='', verbose_name='썸네일')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=50, unique=True, verbose_name='카테고리 이름')),
                ('description', models.CharField(max_length=200, verbose_name='카테고리 설명')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(to='article.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='라이크한 유저')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='댓글 내용')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article', verbose_name='게시글')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='댓글 작성자')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.categories'),
        ),
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(to='article.like'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='게시글 작성자'),
        ),
    ]
