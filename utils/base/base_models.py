"""
Project: django_study
Creator: gaotang
Create time: 2021-03-01 16:09
IDE: PyCharm
Introduction:
"""

from django.db import models


class BaseModel(models.Model):
    # id = models.AutoField(primary_key=True, verbose_name="主键", help_text="主键")
    # auto_now_add 创建时间
    # auto_now 修改时间
    create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        # 当前的base model 只会被继承，数据库迁移时，不会创建该表
        abstract = True
