from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import View, generic
from django.utils import timezone

from polls.form import LoginForm, RegisterForm,QuestionForm, ChoiceForm
from .models import Question,Choice, User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
"""
Create your views here.
The concept of a view in Django is 
              "a collection of web pages with the same functionality and templates."
Each view is responsible for doing one of two things: 
   ①returning an HttpResponse object containing the content for the requested page,
   ②or raising an exception such as Http404.

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
"""

def index(request):
    return render(request, 'polls/index.html')

class IndexView(generic.ListView):
    template_name = "polls/main.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
       # return Question.objects.order_by("-pub_date")[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

#装饰器确保只有已登录的用户才能访问该视图。如果用户未登录，将自动重定向到登录页面。
#@login_required
def main(request):
    all_questions = Question.objects.order_by("pub_date")
    context = {"all_questions": all_questions}
    return render(request, 'polls/main.html', context)
 
 
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'polls/register.html', {'form': form})
 
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '注册成功！')
            return redirect('polls:index')
        return render(request, 'polls/register.html', {'form': form})
 
def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)
 
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'polls/login.html', {'form': form})
 
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '登录成功！')
                return redirect('polls:main')
            else:
                messages.error(request, '用户名或密码错误')
                return render(request, 'polls/login.html', {'form': form})
        return render(request, 'polls/main.html', {'form': form})
 
 
# 注销
def LogoutView(request):
    logout(request)
    return redirect('polls:index')


def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_form = ChoiceForm(request.POST)
        if question_form.is_valid() and choice_form.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            choice = choice_form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('polls:main')
    else:
        question_form = QuestionForm()
        choice_form = ChoiceForm()
    return render(request, 'polls/add_question.html',{'question_form': question_form, 'choice_form': choice_form})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


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
   