# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def url(self):
        return '/team/%s' % self.id

class Match(models.Model):
    date = models.DateTimeField()
    home = models.ForeignKey(Team, related_name='home')
    away = models.ForeignKey(Team, related_name='away')
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s - %s" % (self.home.name, self.away.name)
    
    def url(self):
        return '/match/%s' % self.id

class Comment(models.Model):
    user = models.ForeignKey(User)
    match = models.ForeignKey(Match)
    content = models.TextField(max_length=500)
    parent = models.ForeignKey('self', null=True)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    removed = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(blank=True, null=True)
    
    def url(self):
        return '/comment/%s' % self.id
    
    def already_voted(self):
        #return False #for debug only
        return Vote.objects.filter(user=self.user, comment=self)

class Vote(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #avatar = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    
    def url(self):
        return '/user/%s' % self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
