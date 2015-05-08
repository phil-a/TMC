from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=50,default='')
	profile_age = models.PositiveSmallIntegerField(max,default='0')
	profile_pic = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)

#use user profile model and check db to get profile or if not in db create new
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])	