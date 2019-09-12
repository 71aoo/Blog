from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    #Meta 里指定一些和表单相关的
    class Meta:
        #表明这个表单对应的数据库模型是 Comments 类
        model = Comments
        fields = ['name','url','email','context']
