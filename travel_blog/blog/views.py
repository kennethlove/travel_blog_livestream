from django.views import generic

from . import models


class PostList(generic.ListView):
    model = models.Post


class PostDetail(generic.DetailView):
    model = models.Post
