from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogTag(models.Model):
    name = models.CharField(verbose_name=_('Title'), max_length=100)
    created = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated Date'), auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Blog Tag')
        verbose_name_plural = _('Blog Tags')


class BlogCategory(models.Model):
    name = models.CharField(verbose_name=_('Title'), max_length=100)
    created = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated Date'), auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')


class BlogPost(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    text = models.TextField(verbose_name=_('Description'), max_length=1000, blank=True)
    created = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(verbose_name=_('Updated Date'), auto_now_add=True, blank=True, null=True)
    categories = models.ManyToManyField(BlogCategory)
    tags = models.ManyToManyField(BlogTag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')