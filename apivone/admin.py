from django.contrib import admin
from .models import BlogTag, BlogCategory, BlogPost


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created',
        'updated',
    )
    list_per_page = 25
    date_hierarchy = 'created'


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created',
        'updated',
    )
    list_per_page = 25
    date_hierarchy = 'created'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'categorie',
        'created',
        'updated',
    )

    def categorie(self, instance):
        return [categorie.name for categorie in instance.categories.all()]

    list_per_page = 25
    date_hierarchy = 'created'
