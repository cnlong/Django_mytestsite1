from django.db import models

# Create your models here.

class BookInof(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记，删除数据，不代表真正删除，只是修改删除标记
    # 软删除
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄人物模型类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 外键关联图书,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    hbook = models.ForeignKey('BookInof', on_delete=models.CASCADE)
    # 软删除
    isDelete = models.BooleanField(default=False)