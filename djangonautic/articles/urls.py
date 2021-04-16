from django.conf.urls import url
from . import views
from django.urls import re_path
from django.views.decorators.http import require_GET
from django.urls import include, re_path

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]
