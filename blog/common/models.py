from django.db import models
# Create your models here.


# motto
class Motto(models.Model):
    context = models.TextField(verbose_name="座右铭")

    def __str__(self):
        return self.context

# my information
class Info(models.Model):
    name = models.CharField(max_length=50,verbose_name="ID", blank=False, null=False)
    motto = models.ForeignKey(Motto, null=True, blank=True, on_delete="CASCADE")
    header_img = models.ImageField(verbose_name="头像")
    QQ = models.CharField(max_length=12, verbose_name="QQ", blank=True, null=True)
    email = models.CharField(max_length=100, verbose_name="邮箱", blank=True, null=True)
    github = models.TextField(verbose_name="github", blank=True, null=True)

    def __str__(self):
        return self.name

# friends
class Friends(models.Model):
    name = models.CharField(max_length=20, verbose_name="名字")
    header_img = models.ImageField(verbose_name="头像")
    link = models.TextField(verbose_name="链接")

    def __str__(self):
        return str(self.name)

# navbar
class Navbar(models.Model):
    name = models.CharField(max_length=20,verbose_name="标题")
    font_awesome = models.TextField(verbose_name="Font Awesome")
    path = models.TextField(verbose_name="地址")

    def __str__(self):
        return self.name



# images
class Images(models.Model):
    name = models.CharField(max_length=100, verbose_name="名字", blank=True, null=True)
    img = models.ImageField(verbose_name="顶部图片")

    def __str__(self):
        return self.name

#color
class Colors(models.Model):

    name = models.CharField(max_length=500, verbose_name="颜色", default="button-primary")

    def __str__(self):
        return self.name


# category
class Categories(models.Model):
    name = models.CharField(max_length=10, verbose_name="类名")

    color = models.ForeignKey(Colors, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


