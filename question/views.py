import os
import time
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice

# Create your views here.

def questionIndex(request):
    questions = Question.objects.order_by('-created')[:10]
    request.session['questions_ids'] = [question.id for question in questions]
    context = {'questions': questions}
    return render(request, 'question/forms.html', context )



def finalResult(request):
    questions = Question.objects.filter(id__in=request.session['questions_ids']).prefetch_related('choice_set')
    number_of_correct_answers = 0
    
    for question in questions:
        form_choice_name = 'choice_{}'.format(question.id)
        user_answer = request.POST.get(form_choice_name, '')

        if not user_answer:
            continue

        for choice in question.choice_set.all():
            if choice.choice_text == user_answer:
                if choice.is_correct:
                    number_of_correct_answers += 1          
                break
            
    scores = number_of_correct_answers *5
    total_scores = scores * 10
    int_scores = scores / total_scores
    percentage_scores = 100 * (scores / 50)
    if percentage_scores >= 75:
        grade = 'congrats, you passed'
    else:
        grade = 'oh!! no, try again'

    context_data = {
        'number_of_correct_answers': number_of_correct_answers,
        'scores': scores,
        'percentage_scores': percentage_scores,
        'grade': grade
    }

    return render(request, 'question/result.html', context_data)