from django import forms
from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):
    username = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=20,null=False)
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
 
    # 设置后台管理
    class Meta:
        app_label = 'polls'  
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    # 输出对象时用到的
    def __str__(self):
        return self.username

    
# Create your models here.
#two models:--------------Question（description & time） and Choice（description & votes）
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #pub_date 表示发布日期
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
       


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
