from django.db import models
from tinymce import models as tinymce_models

from django.contrib.auth import get_user_model
from django.urls import reverse


User=get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
	title  = models.CharField(verbose_name= 'Category',max_length=200)

	def __str__(self):
		return self.title


class Post(models.Model):
	Author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(verbose_name= 'Title', max_length = 200)
	overview = models.TextField(verbose_name='Overview',max_length=150,default = 'Write an overview to help readers the context of the aticle.')
	Content = tinymce_models.HTMLField()
	date_added = models.DateTimeField(verbose_name = 'Date Added',auto_now_add=True)
	CC = models.IntegerField(verbose_name = 'Comment Count',default=0)
	VC = models.IntegerField(verbose_name='View Count',default = 0)
	thumbnail = models.ImageField()
	Categories = models.ManyToManyField(Category)
	featured = models.BooleanField(default = True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('post',kwargs={'pk': self.pk})

	@property
	def get_comments(self):
		return self.comments.all().order_by('-date_posted')
	

class Comments(models.Model):
	Author = models.ForeignKey(User,on_delete = models.CASCADE)
	post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
	date_posted = models.DateTimeField(verbose_name = 'Comment Date',auto_now_add=True)
	Comment = models.TextField(verbose_name = 'Comment',default = 'Share Your Views')

	def __str__(self):
		return self.Author.username