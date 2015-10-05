from django.db import models
from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length=100)

class Match(models.Model):
    pass

class Comment(models.Model):
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    content = models.TextField(max_length=500)
    parent = models.ForeignKey('self', null=True)
    pub_date = models.DateTimeField(default=timezone.utcnow)
    votes = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)

class Vote(models.Model):
    comment = models.ForeignKey(Comment)
    pub_date = models.DateTimeField(default=timezone.utcnow)
    ip = models.IPAddressField()