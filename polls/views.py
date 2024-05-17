from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

"""
Create your views here.
The concept of a view in Django is 
              "a collection of web pages with the same functionality and templates."

"""
#isplays the last 5 poll questions in the database, sorted by publication date
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])  
    #if you try to make your page look different, use the index.html as template file
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at the detail of question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)