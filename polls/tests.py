import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="test1",pub_date=timezone.now())
        Question.objects.create(question_text="test2",pub_date=timezone.now())

    def test_question_str(self):
        test1 = Question.objects.get(question_text="test1")
        test2 = Question.objects.get(question_text="test2")
        self.assertEqual(test1.__str__(), 'test1')
        self.assertEqual(test2.__str__(), 'test2')