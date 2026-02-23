from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       
  path('', views.home, name='home'),
  path ('index/', views.index, name='index'),
  path ('masonry/', views.masonry, name='masonry'),
  path ('grid/', views.grid, name='grid'),
  path ('single_post/', views.single_post, name='single-post'),
  path ('blog/', views.blog, name='blog'),
  path ('about/', views.about, name='about')

]