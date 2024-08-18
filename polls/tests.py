from django.test import TestCase

# 按照惯例，Django 应用的测试应该写在应用的 tests.py 文件里。
# 测试系统会自动的在所有文件里寻找并执行以 test 开头的测试函数
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        bug：将来发布的问题应该返回 False
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)