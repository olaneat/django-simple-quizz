from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    label = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('-question',)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    is_correct= models.BooleanField(default=False)

    def __str__(self):
        return self.choice
    
    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = "Choice"

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.label
     


