from django.db import models
from django.shortcuts import reverse

class Story(models.Model):
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250)
	body = models.TextField()
	created= models.DateField(auto_now=True)

	class Meta:
		verbose_name = 'Story'
		verbose_name_plural = 'Stories'
		ordering = ('-created', 'title',)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("story:detail", args=[self.id])
	

