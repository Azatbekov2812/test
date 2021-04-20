from datetime import datetime
import pytz
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Manager
from django.utils import timezone

User = get_user_model()


# Create your models here.
class CustomQuizManager(models.Manager):
    def active(self):
        return self.filter(end_date__gte=datetime.now(tz=timezone.utc)).filter(
            start_date__lt=datetime.now(tz=timezone.utc))

    def yet_not_active(self):
        return self.filter(start_date=None)
    # def get_queryset(self):
    #     return super().get_queryset().filter(end_date__gte=datetime.today()).filter(start_date__lt=datetime.today())


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    customObject = CustomQuizManager()
    objects = Manager()

    def __str__(self):
        return self.name


class Question(models.Model):
    TYPE_ONE = 'однин вариант'
    TYPE_TEXT = 'техт'
    TYPE_SOME = 'несколько ответов'
    ANSWER_CHOICES = [
        (TYPE_ONE, TYPE_ONE),
        (TYPE_TEXT, TYPE_TEXT),
        (TYPE_SOME, TYPE_SOME),
    ]
    question_text = models.CharField(max_length=255)
    type = models.CharField(choices=ANSWER_CHOICES, max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    options = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.options


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_answer_user = models.PositiveSmallIntegerField()
    text = models.TextField(default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    some_choice = models.ManyToManyField(Choice, related_name='answers_some_choices', null=True)
    one_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answers_one_choice', null=True)
