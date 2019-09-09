from django.urls import path
from .import views

app_name = 'article'

urlpatterns = [
    path('article/<int:id>/', views.articles, name='article' ),
    path('category/<int:id>/', views.category, name='category' ),
    path('categories', views.categories, name='categories' ),
]