from datetime import timezone
from django.db import models
from common.models import Categories, Images
from mdeditor.fields import MDTextField
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

# article
class Articles(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题", blank=False, null=False)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    tags = TaggableManager()
    img = models.ForeignKey(Images, on_delete=models.DO_NOTHING)
    intro = models.CharField(max_length=100, verbose_name="文章简介", blank=False, null=False, default=" A")
    content = MDTextField()
    created_time = models.DateTimeField(default = timezone.now(), verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    total_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title