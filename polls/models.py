import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=220)
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_text')
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
