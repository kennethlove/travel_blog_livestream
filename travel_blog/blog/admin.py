from django.contrib.gis import admin

from . import models


class ImageInline(admin.StackedInline):
    model = models.Image


class PostAdmin(admin.GeoModelAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)
