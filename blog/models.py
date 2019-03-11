from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	author_name = models.CharField(max_length=50)
	content = models.TextField()

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	author_nickname = models.CharField(max_length=50)
	author_email = models.CharField(max_length=50)
	content = models.TextField()
