from django.db import models

# Create your models here.
class Book(models.Model):
	book_name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/', default='Null')
	
	def __str__(self):
		return self.book_name
		return u'%s %s' % (self.book_name, self.description)

class Picture(models.Model):
	picture = models.ImageField(upload_to='test/', default='Null')
