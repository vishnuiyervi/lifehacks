from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'hack'
urlpatterns = [
    url(r'^create/hack/$', views.new_hack, name='new_hack'),
    url(r'^create/tip/$', views.new_tip, name='new_tip'),
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<wisdom_id>[0-9]+)', views.display, name='display'),
]
