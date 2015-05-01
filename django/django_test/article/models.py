from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
 
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	tags = models.TextField(default='')
	ecwid = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name)
	thumbnail2 = models.FileField(upload_to=get_upload_file_name,default=0)
	thumbnail3 = models.FileField(upload_to=get_upload_file_name,default=0)
	PROF = 'PROFESSIONAL'
	STRT = 'STREET'
	PREP = 'PREP'
	CLOTHING_STYLE = ((PROF, 'Professional'),(STRT, 'Street'),(PREP, 'Prep'),)
	clothing_style = models.CharField(max_length=12,
									choices=CLOTHING_STYLE,
 									default=PROF)
	def __unicode__(self):
		return self.title 


#class Comment(models.Model)
#	name = models.CharField(max_length=200)
#	body = models.TextField()
#	pub_date = models.DateTimeField('date published')
#	article = models.ForeignKey(Article)