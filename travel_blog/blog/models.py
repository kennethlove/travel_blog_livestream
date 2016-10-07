from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    content_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    coords = models.PointField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at', '-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    @property
    def latlng(self):
        return (self.coords[1], self.coords[0])


class Image(models.Model):
    upload = models.ImageField(upload_to='posts/images/')
    description = models.TextField(blank=True, default='')
    post = models.ForeignKey(Post, related_name='images')

    def __str__(self):
        return self.description
