from django.conf.urls import include, url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #main
    url(r'^$', views.index, name='index'),
    #comments
    #url(r'^comments/$', views.comment_list, name='comment_list'),
    #url(r'^comments/new/$', views.comment_create, name='comment_create'),
    #url(r'^comments/(?P<comment_id>[0-9]+)/$', views.comment_detail, name='comment_detail'),
    #url(r'^comments/(?P<comment_id>[0-9]+)/edit/$', views.comment_update, name='comment_update'),
    #url(r'^comments/(?P<comment_id>[0-9]+)/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^comments/(?P<comment_id>[0-9]+)/vote/$', views.comment_vote, name='comment_vote'),
    #matches
    #url(r'^matches/$', views.match_list, name='match_list'),
    #url(r'^matches/(?P<match_id>[0-9]+)/$', views.match_detail, name='match_detail'),
]
