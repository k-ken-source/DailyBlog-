from django.shortcuts import render, get_list_or_404, reverse, get_object_or_404, redirect
from django.db.models import Count,Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from Accounts.models import User
from .models import Post, PostView
from .forms import CommentForm, PostForm 

def Category_Count():
	#categories render the id so use Categories__title 
	catagories = Post.objects.values('Categories__title').annotate(Count('Categories__title'))
	return catagories


def index(request):
	post = Post.objects.filter(featured=True).order_by('-date_added')
	latest=Post.objects.order_by('-date_added')[0:3]
	context={'object':post,'latest':latest}
	return render(request,'posts/index.html',context)

def Search(request):
	q_set1 = Post.objects.all()
	q_set2 = User.objects.all()

	query = request.GET.get('q')
	if query:
		result = q_set1.filter(
			Q(title__icontains = query) |
			Q(Content__icontains = query)
			).distinct()
	else:
		result = ''
	
	context={'result':result}

	return render(request, 'posts/Search.html',context)

class BlogListView(ListView):
	model = Post
	template_name = 'posts/blog.html'
	ordering=['-date_added']

	def get_context_data(self, *args, **kwargs):
		CatCount = Category_Count()
		context = super(BlogListView, self).get_context_data(*args, **kwargs)
		context['latest'] = Post.objects.order_by('-date_added')[0:3]
		context['Category_Count'] = CatCount
		return context


class PostDetailView(DetailView):
	model = Post
	template_name = 'posts/post.html'
	context_object_name = 'obj'
	form = CommentForm

	def get_object(self):
		obj = super().get_object()
		if self.request.user.is_authenticated:
			PostView.objects.get_or_create(user=self.request.user,post=obj)
		return obj

	def get_context_data(self, *args, **kwargs):
		CatCount = Category_Count()
		context = super().get_context_data(*args, **kwargs)
		context['latest'] = Post.objects.order_by('-date_added')[0:3]
		context['Category_Count'] = CatCount
		context['form'] = self.form
		return context

	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			post = self.get_object()
			form.instance.Author = request.user
			form.instance.post = post
			form.save()
			return redirect('post', pk=post.pk)
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	success_url ="/"

	def get_object(self):
		obj = super().get_object()
		if self.request.user.is_authenticated:
			PostView.objects.get_or_create(user=self.request.user,post=obj)
		return obj
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.Author:
			return True
		return False


class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url='/'

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.Author:
			return True
		else:
			return False

class PostCreateView( LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'posts/Create.html'
	form_class = PostForm 

	def form_valid(self, form):
		form.instance.Author = self.request.user
		return super().form_valid(form)
		