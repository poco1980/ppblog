from django.conf.urls import url
from . import views

urlpatterns = [
    #Homepage
    url(r'^$', views.index, name='index'),

    #Topics Page
    url(r'^topics/$', views.topics, name='topics'),

    # Single Topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Titles Page
    url(r'^titles/$', views.titles, name='titles'),

    # Single Title
    url(r'^titles/(?P<title_id>\d+)/$', views.title, name='title'),

    # New Topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # New Title
    url(r'^new_title/$', views.new_title, name='new_title'),

    # New Entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]
