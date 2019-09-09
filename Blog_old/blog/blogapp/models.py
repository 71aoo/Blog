from django.db import models
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField

# Create your models here.
class Navbar(models.Model):
    title = models.CharField(default='',blank=True,null=True,max_length=20)
    word_img = models.CharField(null=True,help_text="Glyphicons 字体图标",max_length=100)
    url = models.CharField(default='',blank=True,null=True,max_length=20)
    def __str__(self):
        return self.title

class ArticleColumn(models.Model):
     # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(default='',null=False,max_length=100,help_text="文章标题")
    img =models.ImageField(upload_to='images',help_text="文章图片")   
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    tags = TaggableManager(blank=True)
    introduction = models.CharField(null=True,max_length=50,help_text="文章简介")
    content = MDTextField()
    
    create_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

class Recommend(models.Model):
    name = models.CharField(default='',null=False,max_length=100,help_text="（文章标题）与你选择的一样")
    article = models.ForeignKey(
        Article,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='re_article'
        
    )
    def __str__(self):
        return self.name

   
    

class Friends(models.Model):
    name = models.CharField(null=False,max_length=10,help_text="朋友ID")
    head_img = models.ImageField(upload_to='images',help_text="头像")
    Motto = models.CharField(null=False,max_length=30,help_text="座右铭或简介")
    url = models.CharField(null=False,max_length=100,help_text="blog 链接")

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(null=False,max_length=10,help_text="ID")
    head_img = models.ImageField(null=False,upload_to='images',help_text="头像")
    Motto = models.CharField(null=False,max_length=100,help_text="座右铭或简介")
    major = models.CharField(null=False,max_length=50)
    qq = models.CharField(null=True,max_length=500)
    email = models.CharField(null=True,max_length=500)
    github = models.CharField(null=True,max_length=500)
    bili= models.CharField(null=True,max_length=500)


    def __str__(self):
        return self.name

class Header_img(models.Model):
    name = models.CharField(default='',null=False,max_length=10,help_text="组合")
    about_img = models.ImageField(null=False,upload_to='images',help_text="关于我界面")
    friends_img = models.ImageField(null=False,upload_to='images',help_text="友链界面")
    sort_img = models.ImageField(null=False,upload_to='images',help_text="归档界面")
   
    def __str__(self):
        return self.name


