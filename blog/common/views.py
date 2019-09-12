from django.shortcuts import render
from .models import Navbar, Info, Motto, Friends, Images, Categories, Projects
from article.models import Articles
from .get_data_list import get_date_list
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime
import random

# Create your views here.
def index(request):

    context = {}
    images = Images.objects.all()
    navbar =  Navbar.objects.all()
    info = Info.objects.first()
    motto = Motto.objects.all()
    articles = Articles.objects.all()

    # 文章分页
    page_robot = Paginator(articles, 4)
    page_num = request.GET.get('page')
    try:
        articles = page_robot.page(page_num)
    except EmptyPage:
        articles = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        articles = page_robot.page(1)

    # 随机取头部图片
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]

    context['Navbar'] = navbar
    context['Info'] = info
    context['Motto'] = motto
    context['Articles'] = articles
    context['pagerang'] = page_robot

    return render(request, 'index.html',context)


def friends(request):

    context = {}

    images = Images.objects.all()
    friends = Friends.objects.all()
    navbar =  Navbar.objects.all()
    info = Info.objects.first()
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]


    context['Navbar'] = navbar
    context['Info'] = info
    context['Friends'] = friends

    return render(request, 'friends.html',context)

def archive(request):

    # 初始化一些变量
    context = {}
    en_month = {
        '01' : 'Jan',
        '02' : 'Feb.',
        '03' : 'Mar.',
        '04' : 'Apr.',
        '05' : 'May.',
        '06' : 'Jun.',
        '07' : 'Jul.',
        '08' : 'Aug.',
        '09' : 'Sept.',
        '10' : 'Oct.',
        '11' : 'Nov.',
        '12' : 'Dec.'
    }
    articles_order_by_year = {}
    articles_order_by_month = {}
    articles_list = []

    articles_data_list = {}
    images = Images.objects.all()
    navbar =  Navbar.objects.all()
    info = Info.objects.first()
    articles = Articles.objects.all().order_by("-created_time")


    # 随机取一张图片，作为网页顶端图片
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]


    if articles:
        # 最后一篇文章的年份
        year = articles[0].created_time.strftime("%Y")
        # 最后一篇文章的月份
        month = articles[0].created_time.strftime("%m")
        for article in articles:
            # 按 年 月分组文章，生成字典 { year：{month：articles_list}}
            if article.created_time.strftime("%Y") == year:
                if int(month) != 0:
                    if article.created_time.strftime("%m") == month:
                        articles_list.append(article)
                        articles_order_by_month[en_month[month]] = articles_list

                    else:
                        month = article.created_time.strftime("%m")
                        articles_list = [article]
                        articles_order_by_month[en_month[month]] = articles_list

                articles_order_by_year[year] = articles_order_by_month

            else:
                year = article.created_time.strftime("%Y")
                month = article.created_time.strftime("%m")
                articles_order_by_month = {}
                articles_list = [article]
                articles_order_by_month[en_month[month]] = articles_list
                articles_order_by_year[year] = articles_order_by_month

            # 找对应时间文章数,生成字典 { %Y-%m-%d: number}
            if article.created_time.strftime("%Y-%m-%d") in articles_data_list.keys():
                articles_data_list[article.created_time.strftime("%Y-%m-%d")] += 1
            else:
                articles_data_list[article.created_time.strftime("%Y-%m-%d")] = 1

    # 计算出离现在一年之前的所有年月日
    time_now = datetime.datetime.now()
    years_ago = time_now - datetime.timedelta(days = 362)
    data_list = get_date_list(str(years_ago.strftime("%Y-%m-%d")), str(time_now.strftime("%Y-%m-%d")))

    context['Navbar'] = navbar
    context['Info'] = info
    context['time_now'] = time_now.strftime("%Y-%m-%d")
    context['years_ago'] = years_ago.strftime("%Y-%m-%d")
    context['data_list'] = data_list
    context['articles_data_list'] = articles_data_list
    context['articles_order_by_year'] = articles_order_by_year

    return render(request, 'archive.html',context)

def about(request):
    context = {}
    articles_tags = []
    articles_time_num = {}
    categories_and_num = {}
    images = Images.objects.all()
    navbar = Navbar.objects.all()
    info = Info.objects.first()
    categories = Categories.objects.all()
    all_articles =  Articles.objects.all()

    # 随机取图片
    if images:
        num = random.randint(0, len(images) - 1)
        context['header_img'] = images[num]

    if categories:
        for category in categories:
            categories_and_num[category] = len(category.articles_set.all())

    today = datetime.datetime.now()
    if today.month > 1:
        last_month = today.month - 1
        year = today.year
    else:
        last_month = 12
        year = today.year - 1


    articles = Articles.objects.filter(created_time__year=year, created_time__month=last_month).order_by("created_time")
    if articles:
        for article in articles:
            if article.created_time.strftime("%Y-%m-%d") not in articles_time_num:
                articles_time_num[article.created_time.strftime("%Y-%m-%d")] = 1
            else:
                articles_time_num[article.created_time.strftime("%Y-%m-%d")] += 1

    # 获得当前文章下所有tag标签，返回列表
    if  all_articles:
        for article in all_articles:
            for tag in list(article.tags.names()):
                # 去除重复标签
                if tag not in articles_tags:
                    articles_tags.append(tag)

    projects = Projects.objects.all()


    # 基础信息
    context['Navbar'] = navbar
    context['Info'] = info


    # 文章数，分类数， 标签数
    context['articles_num'] = len(all_articles)
    context['articles_categories_num'] = len(Categories.objects.all())
    context['articles_tag_num'] = len(articles_tags)

    # Articles Charts
    context['categories_and_num'] = categories_and_num
    context['articles_time_num'] = articles_time_num
    context["range"] = str(year) + '-' + str(last_month)

    # 所有标签
    context['articles_tags'] = articles_tags

    # 我的项目
    context['projects'] = projects

    return render(request, 'about.html', context)





