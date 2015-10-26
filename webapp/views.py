# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import *
from .models import *

COMMENTS_PER_PAGE = 10

def index(request):
    matches = Match.objects.all()
    return render(request, 'index.html', {
        'matches': matches,
    })


def match_view(request, match_id, order_by='-id'):
    match = get_object_or_404(Match, pk=match_id)
    comment_form = CommentForm()
    
    #if request.user.is_authenticated():
    if request.method == "POST":
        match_id = request.POST.get('match')
        # check if user logged in
        # check if post id equals get match_id
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.match = match
            comment.ip = get_client_ip(request)
            comment.save()
            return HttpResponseRedirect(match.url())
    
    comment_list = Comment.objects.filter(match=match).order_by(order_by)
    paginator = Paginator(comment_list, COMMENTS_PER_PAGE)
    page = request.GET.get('page')
    
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    
    return render(request, 'match.html', {
        'match': match,
        'comments': comments,
        'comment_form': comment_form,
    })


def match_votes(request, match_id):
    return match_view(request, match_id, order_by='-votes')


def match_yours(request, match_id):
    return match_view(request, match_id, order_by='-votes')


def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    match = get_object_or_404(Match, pk=comment.match.id)
    return render(request, 'match.html', {
        'match': match,
        'comments': [comment],
    })


def chart(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    votes = Vote.objects.filter(comment=comment).order_by('created')
    
    data = []
    series = []
    categories = []
    
    value = 0
    for vote in votes:
        data.append(value)
        value += vote.value
        categories.append(vote.created)
    
    diff = votes[41].created - votes[0].created
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
