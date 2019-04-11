#from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'HelloApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# urlpatterns = [
#     path('')
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#]


    #ex: /HelloApp/
    #url(r'^$', views.index, name='index'),
    #ex: /HelloApp/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
    #ex: added the word 'specifics'
    #url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #ex: /HelloApp/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #ex: /HelloApp/5/vote/
    #$url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
