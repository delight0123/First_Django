from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic

from .models import Question,Choice

"""
Create your views here.
The concept of a view in Django is 
              "a collection of web pages with the same functionality and templates."
Each view is responsible for doing one of two things: 
   ①returning an HttpResponse object containing the content for the requested page,
   ②or raising an exception such as Http404.
"""
#isplays the last 5 poll questions in the database, sorted by publication date
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])  
#     #if you try to make your page look different, use the index.html as template file
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist.")

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
#    # return HttpResponse("You're looking at the detail of question %s." % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 #数据库将投票数加一
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
   