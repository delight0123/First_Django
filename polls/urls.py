from django.urls import path
from . import views
"""
 path() function is passed four arguments, 
two required: route and view
two optional: kwargs and name
"""
#url configuration,put views.index in URLconf
urlpatterns = [path("",views.index,name="index"),]