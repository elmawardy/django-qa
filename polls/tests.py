import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
from .models import Choice

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="test1",pub_date=timezone.now())
        Question.objects.create(question_text="test2",pub_date=timezone.now())

    def test_question_str(self):
        test1 = Question.objects.get(question_text="test1")
        test2 = Question.objects.get(question_text="test2")
        self.assertEqual(test1.__str__(), 'test1')
        self.assertEqual(test2.__str__(), 'test2')

class ChoiceTest(TestCase):
    def setUp(self):
        test1 = Question.objects.filter(question_text="test1")
        if not test1.exists():
            Question.objects.create(question_text="test1",pub_date=timezone.now())
        test1 = Question.objects.get(question_text="test1")
        Choice.objects.create(question=test1 ,choice_text="choice 1", votes=0)
    
    def test_is_positive(self):
        test1 = Question.objects.get(question_text="test1")
        c1 = Choice.objects.get(question=test1)
        self.assertEqual(c1.is_positive(), True)