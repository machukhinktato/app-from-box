from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    lateest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lateest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    response = f"You're looking at answer {question_id}"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"You're voting on {question_id}")
