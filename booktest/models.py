from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    """自定义一个BookInfo的模型管理器类，继承自模型管理器类"""
    # 1.重写其all方法
    def all(self):
        # 1.调用父类的all方法，获取所有的数据，返回是是一个QuerySet
        books = super().all()
        # 2.对数据进行过滤，加入自己想要的方法
        books = books.filter(isDelete=False)
        # 3.返回查询结果
        return books

    # 2.添加额外的函数方法，操作模型类对象的数据报（增删改查）
    def create_book(self, btitle, bpud_date):
        # 1.创建一个图书对象
        # book = BookInfo()
        # 直接通过BookInfo()创建类的时候，存在一个一一对应的关系，如果模型类的名字变了，管理器也需要改变
        # 所以通过管理器的model方法获取其所对应的模型类的类名，较为方便
        model_class = self.model
        book = model_class()
        book.btitle = btitle
        book.bpub_date =bpud_date
        # 2.数据保存
        book.save()
        # 3.返回对象
        return book

class BookInfo(models.Model):
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
    # # 自定义一个BookInfoManager类的对象
    # object = BookInfoManager()


class HeroInfo(models.Model):
    """英雄人物模型类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 外键关联图书,表与表之间关联的时候,必须要写on_delete参数,否则会报异常
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
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