from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_detail', views.blog_detail, name='blog_detail'),
]
