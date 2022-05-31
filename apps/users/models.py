from django.contrib.auth.models import AbstractUser


# Create your models here.


class UsersModel(AbstractUser):
    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户表'
