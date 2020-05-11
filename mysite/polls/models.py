import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    diff_level = models.CharField(max_length=20)
    def __str__(self):
        full_question = self.question_text + '-' + self.diff_level
        return full_question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth_year = models.IntegerField(default=0)
    def __str__(self):
        person_info = self.first_name + ' ' + self.last_name + ', ' + str(self.birth_year)
        return person_info