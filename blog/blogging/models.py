from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	author = models.CharField(max_length=30)
	title = models.CharField(max_length=100, unique=True)
	content = models.TextField()
	created = models.DateTimeField()
	modified = models.DateTimeField()


	def __unicode__(self):
		return self.title

