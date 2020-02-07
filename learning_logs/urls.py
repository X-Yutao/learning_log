from django.conf.urls import url

from . import views

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),

    #topics
    url(r'^topics/$', views.topics, name='topics'),

    #topic_detail page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]