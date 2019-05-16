from django.shortcuts import render,HttpResponse
from django.template import Context,Template
from .models import Navbar,Article,Recommend,User,Header_img,Friends
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
import markdown
# Create your views here.

# 首页
def index(request):
    tags = []
    user = User.objects.first()
    navbar = Navbar.objects.all() #顶部导航栏
    article = Article.objects.all().order_by('-create_time') # 文章列表
    recommend = Recommend.objects.all() # 轮播图
    one = Recommend.objects.first() #轮播图第一个标题
    page_robot = Paginator(article,4)
    page_num = request.GET.get('page')

    try:
        article = page_robot.page(page_num)
    except EmptyPage:
        article = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article = page_robot.page(1)

    for arti in article:
        for tag in arti.tags.all():
            if tag not in tags:
                tags.append(tag)
    
    context = {
        'navbar': navbar ,
        'article' : article ,
        'recommend' : recommend,
        'pagerange' : page_robot.page_range,
        'one' : one ,
        'user' : user,
        'tags' : tags
    }
    return render(request,'index.html',context)

# 关于我
def about(request):
    tags = []
    tag_num = 0
    user = User.objects.get(id=1)
    header_img = Header_img.objects.get(id=1)
    navbar = Navbar.objects.all()
    arti_num = Article.objects.count()
    article = Article.objects.all()
    
    for art in article:
        tag_num = tag_num + art.tags.count()
        for tag in art.tags.all():
            if tag not in tags:
                tags.append(tag)

    context = {
        'navbar': navbar ,
        'user': user,
        'article': article,
        'arti_num' : arti_num,
        'tag_num':tag_num,
        'header_img' : header_img,
        'tags' : tags
    }
    
    return render(request,'about.html',context)

# 大佬在这
def friends(request):
    header_img = Header_img.objects.get(id=1)
    user = User.objects.get(id=1)
    friend = Friends.objects.all()
    navbar = Navbar.objects.all()
    context = {
        'navbar': navbar ,
        'user' : user,
        'header_img' : header_img,
        'friend' : friend
    }
    return render(request,'friends.html',context)

# 归档
def sort(request):
    tags = []
    header_img = Header_img.objects.get(id=1)
    user = User.objects.get(id=1)
    navbar = Navbar.objects.all()
    dates =  Article.objects.all().order_by('-create_time')

    for arti in dates:
        for tag in arti.tags.all():
            if tag not in tags:
                tags.append(tag)
    
    context = {}
    context['navbar'] = navbar
    context['dates'] = dates
    context['user'] = user
    context['header_img'] = header_img
    context['tags'] = tags 
    return render(request,'sort.html',context)

def detail(request, id):
    pre_flag = 0
    pre = 0
    next = 0
    user = User.objects.get(id=1)
    navbar = Navbar.objects.all()
    all = Article.objects.all().order_by('-id')
    article = get_object_or_404(Article, id=id) 
    for i in all:
        if pre_flag == 0 and i.id < id :
            pre = get_object_or_404(Article, id= i.id)   
            pre_flag += 1
        if i.id > id:
            next = get_object_or_404(Article, id= i.id)   
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ])
    article.content = md.convert(article.content)
    # 需要传递给模板的对象
    context = { 'article': article }
    context['navbar'] = navbar
    context['tob'] = md.toc
    context['user'] = user
    context['pre_art'] = pre
    context['next_art'] = next
    return render(request, 'detail.html', context)
