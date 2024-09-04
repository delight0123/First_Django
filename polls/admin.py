from django.contrib import admin

# Register your models here.
from .models import Question,User

#to tell management that the Question object needs a backend interface
admin.site.register(Question)
admin.site.register(User)
 