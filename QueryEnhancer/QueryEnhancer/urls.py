from django.contrib import admin
from django.urls import path
from enhancement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('proxy_newsapi/', views.proxy_newsapi, name='proxy_newsapi'),
    path('enhance_query/', views.enhance_query_view, name='enhance_query'),
    path('get_articles/', views.get_articles, name='get_articles'),  # Only if get_articles view is needed
]
