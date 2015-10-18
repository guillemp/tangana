from django.conf.urls import include, url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #main
    url(r'^$', views.index, name='index'),
    #comments
    #url(r'^comments/$', views.comment_list, name='comment_list'),
    #url(r'^comment/new/$', views.comment_create, name='comment_create'),
    url(r'^comment/(?P<comment_id>[0-9]+)/$', views.comment, name='comment'),
    #url(r'^comment/(?P<comment_id>[0-9]+)/edit/$', views.comment_update, name='comment_update'),
    #url(r'^comment/(?P<comment_id>[0-9]+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^comment/(?P<comment_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^comment/(?P<comment_id>[0-9]+)/chart/$', views.chart, name='chart'),
    #matches
    #url(r'^matches/$', views.match_list, name='match_list'),
    url(r'^match/(?P<match_id>[0-9]+)/$', views.match, name='match'),
    url(r'^match/(?P<match_id>[0-9]+)/votes/$', views.match_votes, name='match_votes'),
]