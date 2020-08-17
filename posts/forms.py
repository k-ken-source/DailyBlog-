from django import forms
from .models import Comments, Post
from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):
	Comment = forms.CharField(widget = forms.Textarea(attrs ={
		'class':'form-control',
		'placeholder':'Type your comment',
		'id':"usercomment",
		'rows':4
		}))

	class Meta:
		model = Comments
		fields = ['Comment']


class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self,*args):
		return False

class PostForm(forms.ModelForm):
	Content = forms.CharField(widget=TinyMCEWidget(
	 		attrs={'required': False, 'cols': 30, 'rows': 10}
	 	))

	class Meta:
		model = Post
		fields= ['title', 'thumbnail', 'Content','Categories', 'featured']