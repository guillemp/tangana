from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

def index(request):
    return render(request, 'index.html', {
    })

@csrf_exempt
@login_required
def comment_vote(request, comment_id):
    return HttpResponse(comment_id)