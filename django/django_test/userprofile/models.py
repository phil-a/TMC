from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
# Create your models here.

class UserProfile(models.Model):
	CANADA = 'CA'
	UNITEDSTATES = 'US'
	PURCHASE_COUNTRY = (
		(CANADA, 'Canada'),
		(UNITEDSTATES, 'United States'),
		)


	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=50,default='')
	last_name = models.CharField(max_length=50,default='')
	profile_age = models.CharField(max_length=3,default='')
	postal_code = models.CharField(max_length=8,default='')
	city = models.CharField(max_length=50,default='')
	province = models.CharField(max_length=50,default='')
	country = models.CharField(max_length=2,choices=PURCHASE_COUNTRY,default=CANADA)
	phone = models.CharField(max_length=10,default='')
#use user profile model and check db to get profile or if not in db create new
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])	