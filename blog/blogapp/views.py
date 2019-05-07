from django.shortcuts import render,HttpResponse
from django.template import Context,Template
from .models import Navbar,Article,Recommend,User,Header_img,Friends
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
import markdown
# Create your views here.

# 首页
def index(request):
    user = User.objects.get(id=1)
    navbar = Navbar.objects.all() #顶部导航栏
    article = Article.objects.all().order_by('-create_time') # 文章列表
    recommend = Recommend.objects.all() # 轮播图
    one = Recommend.objects.get(id=1) #轮播图第一个标题
    page_robot = Paginator(article,4)
    page_num = request.GET.get('page')

    try:
        article = page_robot.page(page_num)
    except EmptyPage:
        article = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article = page_robot.page(1)

    context = {
        'navbar': navbar ,
        'article' : article ,
        'recommend' : recommend,
        'pagerange' : page_robot.page_range,
        'one' : one ,
        'user' : user
    }
    return render(request,'index.html',context)

# 关于我
def about(request):
    tag_num = 0
    user = User.objects.get(id=1)
    header_img = Header_img.objects.get(id=1)
    navbar = Navbar.objects.all()
    arti_num = Article.objects.count()
    article = Article.objects.all()
    for art in article:
        tag_num = tag_num + art.tags.count()
    context = {
        'navbar': navbar ,
        'user': user,
        'article': article,
        'arti_num' : arti_num,
        'tag_num':tag_num,
        'header_img' : header_img
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
    header_img = Header_img.objects.get(id=1)
    user = User.objects.get(id=1)
    navbar = Navbar.objects.all()
    dates =  Article.objects.all().order_by('-create_time')   
    context = {}
    context['navbar'] = navbar
    context['dates'] = dates
    context['user'] = user
    context['header_img'] = header_img 
    return render(request,'sort.html',context)

def detail(request, id):
    
    user = User.objects.get(id=1)
    navbar = Navbar.objects.all()
    article = get_object_or_404(Article, id=id) 
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
    return render(request, 'detail.html', context)
























# def first(request):
#     s = 'This is my fist webpage' # 内容
#     return HttpResponse(str(s))  # 返回给浏览器
#
#
#
# def blog(request):
#     person = People(name='playwin',job='coder')
#     html = '''
#     <html>
#     <body>
#     {{person.name}}
#     </body>
#     </html>
#
#     '''
#     t = Template(html)
#     c = Context({'person':person})
#     web = t.render(c)
#     return HttpResponse(web)
#
# def one(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     s = 'a=' + str(a) + '\n' + 'b=' + str(b)
#     return HttpResponse(str(s))
#
#
# from django.shortcuts import render
#
#
# def home(request):
#     return render(request, 'index.html')
