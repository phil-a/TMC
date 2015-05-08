from django import forms
from models import UserProfile
from django.contrib.admin.widgets import FilteredSelectMultiple

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('display_name','profile_age', 'profile_pic')
		widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'profile_pic_form'}),
            	}