from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)

class Match(models.Model):
    date = models.DateTimeField()
    home = models.ForeignKey(Team, related_name='home')
    away = models.ForeignKey(Team, related_name='away')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    content = models.TextField(max_length=500)
    parent = models.ForeignKey('self', null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    ip = models.GenericIPAddressField()
    removed = models.BooleanField(default=False)

class Vote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    ip = models.GenericIPAddressField()