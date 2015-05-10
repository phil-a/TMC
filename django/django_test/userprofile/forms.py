from django import forms
from models import UserProfile
from django.contrib.admin.widgets import FilteredSelectMultiple

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name','last_name','profile_age','postal_code','city','province','country','phone')
