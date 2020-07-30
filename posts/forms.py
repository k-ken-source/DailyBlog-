from django import forms
from .models import Comments

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


