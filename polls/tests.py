from django.test import TestCase

# 按照惯例，Django 应用的测试应该写在应用的 tests.py 文件里。
# 测试系统会自动的在所有文件里寻找并执行以 test 开头的测试函数
import datetime
from django.urls import reverse

from .models import Question
from django.utils import timezone
from django.test import TestCase

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        bug：将来发布的问题应该返回 False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        bug:一天以上发布的问题应该返回 False
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        

    def test_was_published_recently_with_recent_question(self):
        """
        bug: 1天内发布的问题应该返回 True
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


