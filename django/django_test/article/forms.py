from django import forms
from models import Article

class ArticleForm(forms.ModelForm):

	class Meta: # define anything that isn't a form field
		model = Article
		fields = ('title', 'body','tags','ecwid', 'pub_date', 'thumbnail','thumbnail2','thumbnail3','clothing_style')

#class CommentForm(forms.ModelForm)

#	class Meta:
#		model = CommentForm
#		fields = ('name', 'body')		