from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post', views.post),
    url(r'^', views.index),
]
