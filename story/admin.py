from django.contrib import admin
from .models import Story

# Register your models here.
@admin.register(Story)
class AdminStory(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']
    