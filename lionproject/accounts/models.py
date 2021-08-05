from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # 상속받고 확장하고 싶은 column들을 추가하면 된다.
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)