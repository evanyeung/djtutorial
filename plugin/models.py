from django.db import models
from cms.models import CMSPlugin

class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.IntegerField(default=0)
	address = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class ct(CMSPlugin):
	contact = models.ForeignKey('plugin.Contact', related_name='plugins')

