from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4
    
class QuestionAdmin(admin.ModelAdmin):
   list_display = ['question']
   inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)