from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    """
    用户信息表

    """
    nid = models.BigAutoField(primary_key=True)

    name = models.CharField(verbose_name="昵称", max_length=32, null=True)

    telephone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="手机")
    creat_time = models.DateField(verbose_name="创建时间", auto_now_add=True)

    email = models.EmailField(null=True)

    qq = models.CharField(null=True, unique=True, max_length=30)


class Company(models.Model):
    """
    公司表

    """
    nid = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=64)

    addr = models.CharField(max_length=64)


class IViewDetail(models.Model):
    """
    面试详情表

    """
    nid = models.BigAutoField(primary_key=True)

    job = models.CharField(max_length=64, null=True,verbose_name="面试职位")

    creat_time = models.DateField(verbose_name="面试日期", auto_now_add=True)

    iview_questions = models.TextField(verbose_name="面试题")

    process = models.TextField(verbose_name="面试流程")


class UserInfo2Company(models.Model):
    """
    多对多
    """
    nid = models.AutoField(primary_key=True)

    userinfo = models.ForeignKey(verbose_name="用户", to="UserInfo", to_field="nid")

    company = models.ForeignKey(verbose_name="公司", to="Company", to_field="nid")
