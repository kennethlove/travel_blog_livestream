from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='detail'),
]
