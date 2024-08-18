from django.urls import path
from . import views
"""
 path() function is passed four arguments, 
two required: route and view
two optional: kwargs and name
"""
#url configuration,put views.index in URLconf
#To associate URLs with views, Django uses 'URLconfs' to configure

app_name = "polls"
urlpatterns = [
    # # ex: /polls/
    # path("", views.index, name="index"),
    
    # # ex: /polls/5/    question id is 5
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    #第二和第三个模式的路径字符串中匹配的模式名称已从 <question_id> 更改为 <pk>。
    # 使用 DetailView 通用视图
    # 来替换detail() 和 results() 视图 (二者原先的视图除了模板名字一模一样。为了解决冗余，使用通用视图)，它期望从 URL 中捕获的主键值被称为 "pk"。
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]