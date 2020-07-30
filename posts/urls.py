from django.contrib import admin
from django.urls import path,include
from posts.views import PostDetailView
from . import views

urlpatterns = [
	path("",views.index,name='index'),
	path("blog/",views.BlogListView.as_view(),name='blog'),
	path("search/",views.Search,name='Search'),
	path('post/<pk>/', PostDetailView.as_view(), name='post'),
#path('post/<int:pk>/', views.post, name='post'),
]
