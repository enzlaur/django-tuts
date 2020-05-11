from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import *
from django.http.response import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    page_render = template.render(context, request)
    return render(request, 'polls/index.html', context)
    # return HttpResponse(page_render)

def detail(request, question_id):
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist") # You can specify a much more specific 404
    #  message through this one
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': q})

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)