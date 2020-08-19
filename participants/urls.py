from django.conf.urls import url
from participants import views

urlpatterns = [
    url(r'^api/hello/', views.HelloView.as_view(), name='hello'),
]
