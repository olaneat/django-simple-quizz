from django.db import models
from question.models import Question
from django.contrib.auth.models import User


# Create your models here.
class Quizz(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	total_scores = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False)
	