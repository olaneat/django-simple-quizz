from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Story

class StoryList(ListView):
    model = Story
    context_object_name = 'stories'
    template_name='story/index.html'

def index(request):
    stories = Story.objects.all()
    return render(request, 'story/index.html', {'stories':stories})

def storyDetail(request, id):
    story = get_object_or_404(Story, id=id)
    return render(request, 
            'story/detail.html', 
            {'story':story})


class StoryDetail(DetailView):
    model = Story
    template_name='story/detail.html'