from django.db import models
import uuid
from articles.models import Subject
from django.contrib.auth.models import User


class Question(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    quest = models.CharField(max_length=1000)
    opt1 = models.CharField(max_length=1000)
    opt2 = models.CharField(max_length=1000)
    opt3 = models.CharField(max_length=1000)
    opt4 = models.CharField(max_length=1000)
    ans = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quest


class QuestionSet(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    questions = models.ManyToManyField(Question)
    name = models.CharField(max_length=1000, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField(Subject)
    solves = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    questset = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Got {self.score} In {self.questset.name}"
