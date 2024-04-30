from django.contrib import admin

# Register your models here.
from .models import Question

#to tell management that the Question object needs a backend interface
admin.site.register(Question)