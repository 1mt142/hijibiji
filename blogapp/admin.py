from django.contrib import admin
from .models import *


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'post_body',
        'category',
        'tags_list',
        'created_at',
        'updated_at',
    )
    list_per_page = 25
    date_hierarchy = 'created_at'

    def tags_list(self, instance):
        print("From Admin", instance)
        return [tag.name for tag in instance.tags.all()]


@admin.register(BlogCategory)
class BlogCategory(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
    )
    list_per_page = 25
    date_hierarchy = 'created_at'


@admin.register(BlogTag)
class BlogTag(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
        'updated_at',
    )
    list_per_page = 25
    date_hierarchy = 'created_at'
