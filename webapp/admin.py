# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Match, Team, Comment

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Comment)