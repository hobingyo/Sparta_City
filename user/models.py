from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user model
class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일 주소", max_length=100)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.username} / {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):
    # user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, verbose_name="유저", on_delete=models.CASCADE)
    fullname = models.CharField("이름", max_length=20)
    blog_link = models.CharField("개발자 블로그 링크", max_length=100)
    git_link = models.CharField("깃허브 링크", max_length=100)
    picture = models.FileField("프로필 사진", upload_to="../static/profile/")
    team_num = models.IntegerField("팀 번호")
    birthday = models.DateField("생일")

    def __str__(self):
        return f"{self.user.username} 님의 프로필입니다."