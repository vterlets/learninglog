from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topic_entries/(?P<pk>[0-9]+)/$', views.topic_entries, name='topic_entries'),
    url(r'^topic_new/$', views.topic_new, name="topic_new"),
]

