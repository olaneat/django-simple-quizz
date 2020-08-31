import os
import time
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
# Create your views here.

def questionIndex(request):
    questions = Question.objects.order_by('-created')[:10]
    context = {'questions': questions}
    return render(request, 'question/forms.html', context )

def questionDetail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {'question': question}
    return render(request, 'question/detail.html', context)


def finalResult(request):
    return render(request, 'question/result.html')