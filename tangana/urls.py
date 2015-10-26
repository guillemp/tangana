from django.conf.urls import include, url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # main
    url(r'^$', views.index, name='index'),
    
    # auth system
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^login/reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'reset.html', 'post_reset_redirect': '/login/reset/done/'}, name="password_reset"),
    url(r'^login/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'reset_done.html'}),
    url(r'^login/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'reset_confirm.html', 'post_reset_redirect': '/login/reset/complete/'}),
    url(r'^login/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'reset_complete.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    
    #url(r'^user/(?P<username>\w{0,30})/$', 'views.user_view', name='user_view'),
    
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
    url(r'^match/(?P<match_id>[0-9]+)/$', views.match_view, name='match_view'),
    url(r'^match/(?P<match_id>[0-9]+)/votes/$', views.match_votes, name='match_votes'),
    url(r'^match/(?P<match_id>[0-9]+)/yours/$', views.match_yours, name='match_yours'),
]