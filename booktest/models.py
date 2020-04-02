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


# # 模型多对多示例,多对多的两个类中，任意在一个类中写对应的关系属性即可
# # # 新闻类型类
# # class NewsType(models.Model):
# #     # 类型名
# #     type_name = models.CharField(max_length=20)
# #     # 关系属性，代表信息所属的类型
# #     type_news = models.ManyToManyField('NewsInfo')
# #
# #
# # # 新闻类
# # class NewsInfo(models.Model):
# #     # 新闻标题
# #     title = models.CharField(max_length=20)
# #     # 发布时间
# #     pub_date = models.DateTimeField(auto_now_add=True)
# #     # 信息内容
# #     content = models.TextField()
# #     # # 关系属性，代表信息所属的类型
# #     # news_type = models.ManyToManyField('NewsType')

class AreaInfo(models.Model):
    """地区模型类"""
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)   # 代表这个类与他自身有了这种关联