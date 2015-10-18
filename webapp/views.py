from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import *

def index(request):
    matches = Match.objects.all()
    return render(request, 'index.html', {
        'matches': matches,
    })

def match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    comments = Comment.objects.filter(match=match).order_by('-id')
    return render(request, 'match.html', {
        'match': match,
        'comments': comments,
    })

def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    match = get_object_or_404(Match, pk=comment.match.id)
    return render(request, 'match.html', {
        'match': match,
        'comments': [comment],
    })

def chart(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    votes = Vote.objects.filter(comment=comment)
    return render(request, 'chart.html', {
        'comment': comment,
        'votes': votes,
    })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
@login_required
def vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user_ip = get_client_ip(request) # future check if ip exists
    vote_exists = False#Vote.objects.filter(user=request.user, comment=comment)
    
    if not vote_exists:
        vote_type = request.POST.get('vote')
        
        vote_value = 0
        if vote_type == 'up':
            vote_value = 1
        elif vote_type == 'down':
            vote_value = -1

        vote = Vote()
        vote.user = request.user
        vote.comment = comment
        vote.value = vote_value
        vote.ip = user_ip
        vote.save()

        comment.votes = comment.votes + vote_value
        comment.save()
        
        # count from votes
        result = comment.votes
    else:
        result = 'Ya has votado'
    
    return HttpResponse(result)
