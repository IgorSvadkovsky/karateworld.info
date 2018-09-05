from django.db import models
from django.contrib.auth.models import User, AbstractUser


class KarateworldUser(AbstractUser):

    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)