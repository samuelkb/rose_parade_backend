from django.conf.urls import url
from participants import views

urlpatterns = [
    url(r'^api/participants/join$', views.participant_add, name='join'),
    url(r'^api/participants$', views.participants_list, name='participants'),
    url(r'^api/participants/(?P<pk>[0-9]+)$', views.participant_detail)
]
