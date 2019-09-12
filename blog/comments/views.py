from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from article.models import Articles
from .models import Comments
from .forms import CommentsForm

# Create your views here.
def comments(request, id):

    article = get_object_or_404(Articles, id=id)

    if request.method == 'POST':
        # 构造commentform表单
        form = CommentsForm(request.POST)
        # 表单可用
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            comment = Comments(belong_article=article, name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                               url=form.cleaned_data['url'], context=form.cleaned_data['context'])

            # 最终保存到数据库
            comment.save()

            return redirect('article:article', id=id)

    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('article:article', id=id)