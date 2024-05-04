from django.urls import path
from . import views
"""
 path() function is passed four arguments, 
two required: route and view
two optional: kwargs and name
"""
#url configuration,put views.index in URLconf
#To associate URLs with views, Django uses 'URLconfs' to configure

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/    question id is 5
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]