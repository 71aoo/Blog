from django.db import models
from article.models import Articles
from django.utils import timezone
# Create your models here.

class Comments(models.Model):
    belong_article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name="属于那篇文章")
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="名字")
    email = models.EmailField(null=True,blank=True, verbose_name="邮箱")
    url = models.CharField(max_length=500, null=True, blank=True, verbose_name="个人网站")
    context = models.TextField()
    created_time = models.DateTimeField(default = timezone.now(), verbose_name="创建时间")

    def __str__(self):
        return self.name + ":" + self.context[0:5]