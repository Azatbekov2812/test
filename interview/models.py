from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    ANSWER_TYPE = (
        ('1', 'text'),
        ('2', 'one'),
        ('3', 'some'),
    )
    question_text = models.CharField(max_length=255)
    type = models.CharField(choices=ANSWER_TYPE, max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
