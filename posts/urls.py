from django.contrib import admin
from django.urls import path,include
from posts.views import PostDetailView, PostUpdateView, PostDeleteView, PostCreateView
from . import views

urlpatterns = [
	path("",views.index,name='index'),
	path("blog/",views.BlogListView.as_view(),name='blog'),
	path("search/",views.Search,name='Search'),
	path('post/<pk>/', PostDetailView.as_view(), name='post'),
	path('post/<pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/<pk>/delete', PostDeleteView.as_view(), name='post-delete'),
	path('New/', PostCreateView.as_view(), name='post-create'),
#path('post/<int:pk>/', views.post, name='post'),
]
