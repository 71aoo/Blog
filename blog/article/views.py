from django.shortcuts import render
from common.models import Navbar, Info, Motto, Friends, Images, Categories
from .models import Articles
from django.shortcuts import get_object_or_404
import random, markdown
# Create your views here.

def articles(request, id):

    # 初始化变量
    pre_flag = 0
    pre_article = 0
    next_article = 0
    context = {}

    navbar =  Navbar.objects.all()
    info = Info.objects.first()
    all_articles = Articles.objects.all().order_by('-id')
    article = get_object_or_404(Articles, id=id)

    # 当前文章访问量
    article.total_views += 1
    article.save(update_fields=['total_views'])

    # 获取当前文章所有评论
    all_comments = article.comments_set.all()

    # 获得上下篇文章
    for i in all_articles:
        if pre_flag == 0 and i.id < id:
            pre_article = get_object_or_404(Articles, id=i.id)
            pre_flag += 1
        if i.id > id:
            next_article = get_object_or_404(Articles, id=i.id)


    # markdown渲染
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    article.content = md.convert(article.content)

    context['Navbar'] = navbar
    context['Info'] = info
    context['article'] = article
    context['tob'] = md.toc
    context['next_article'] = next_article
    context['pre_article'] = pre_article
    context['all_comments'] = all_comments

    return render(request, 'article.html',context)

def category(request,id):

    context = {}
    navbar = Navbar.objects.all()
    info = Info.objects.first()
    categories = Categories.objects.all()
    images = Images.objects.all()
    category = get_object_or_404(Categories,id=id)
    articles = category.articles_set.all().order_by("-created_time")
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]



    context['Navbar'] = navbar
    context['Info'] = info
    context['categories'] = categories
    context['articles'] = articles
    context['category_name'] = category.name

    return render(request, 'category.html', context)


def categories(request):
    context = {}
    navbar = Navbar.objects.all()
    info = Info.objects.first()
    categories = Categories.objects.all()
    images = Images.objects.all()
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]

    context['Navbar'] = navbar
    context['Info'] = info
    context['categories'] = categories

    return render(request, 'classify.html', context)