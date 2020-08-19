from django.conf.urls import url
from participants import views

urlpatterns = [
    url(r'^api/participants/join$', views.participant_add, name='join'),
    url(r'^api/participants$', views.participants_list, name='participants')
]
