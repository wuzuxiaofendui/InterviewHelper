from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    """
    用户信息表

    """
    nid = models.BigAutoField(primary_key=True)

    name = models.CharField(verbose_name="昵称", max_length=32, null=True)

    telephone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="手机")

    creat_time = models.DateField(verbose_name="创建时间", auto_now_add=True)

    email = models.EmailField(null=True,blank=True)

    qq = models.CharField(null=True, unique=True, max_length=30)

    companys = models.ManyToManyField("Company", verbose_name="面试过的公司")


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

    job = models.CharField(max_length=64, null=True, verbose_name="面试职位")

    creat_time = models.DateField(verbose_name="面试日期", auto_now_add=True)

    iview_questions = models.TextField(verbose_name="面试题")

    process = models.TextField(verbose_name="面试流程")

    user = models.ForeignKey(verbose_name="面试人", to='UserInfo', to_field='nid',null=True,blank=True)

    company = models.ForeignKey(verbose_name="面试公司", to='Company', to_field='nid',null=True,blank=True)

    def __str__(self):
        return self.user.username + "--" + self.company.name + "--" + self.job


class Comment(models.Model):
    """
    评论表
    """
    nid = models.BigAutoField(primary_key=True)
    iviewdetail = models.ForeignKey(verbose_name='评论的面试详情', to='IViewDetail', to_field='nid')
    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    parent_id = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid')

    def __str__(self):
        return "%s---%s" % (self.user.username, self.iviewdetail)
