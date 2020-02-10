from django.conf.urls import url

from . import views

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),

    #topics
    url(r'^topics/$', views.topics, name='topics'),

    #topic_detail page
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    #page to add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #page to add new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #page edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    #search results
    url(r'^search_results/$', views.search_results, name='search_results'),
]