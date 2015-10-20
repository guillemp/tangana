from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.models import User
from .models import *

def index(request):
    matches = Match.objects.all()
    return render(request, 'index.html', {
        'matches': matches,
    })

def match(request, match_id, order_by='-id'):
    match = get_object_or_404(Match, pk=match_id)
    
    # post
    if request.POST:
        comment = Comment()
        comment.user = request.user
        comment.content = request.POST.get('content')
        comment.match = match
        comment.ip = get_client_ip(request)
        comment.save()
        return HttpResponseRedirect('/match/%s' % match.id)
    
    # comments
    comment_list = Comment.objects.filter(match=match).order_by(order_by)
    paginator = Paginator(comment_list, 10)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    
    # render
    return render(request, 'match.html', {
        'match': match,
        'comments': comments,
    })

def match_votes(request, match_id):
    return match(request, match_id, '-votes')

def match_yours(request, match_id):
    return match(request, match_id, '-votes')

def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    match = get_object_or_404(Match, pk=comment.match.id)
    return render(request, 'match.html', {
        'match': match,
        'comments': [comment],
    })

def chart(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    votes = Vote.objects.filter(comment=comment).order_by('pub_date')
    
    data = []
    series = []
    categories = []
    
    value = 0
    for vote in votes:
        data.append(value)
        value += vote.value
        categories.append(vote.pub_date)
    
    diff = votes[41].pub_date - votes[0].pub_date
    #for day in range(0, diff.seconds):
        #print day
        #print day
        #current_date = (dt_start_date + timedelta(days = day_offset)).strftime("%Y-%m-%d")
        #data.append(date_mentions_dict.get(current_date,0))
        #categories.add(current_date)
    
    serie = {
        'name': 'votes',
        'data': data,
    }
    series.append(serie)
        
    json = {
       'categories': categories,
       'series': series,
    }
    
    return JsonResponse(json)

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
