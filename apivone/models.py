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
    created = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, blank=True, null=True) #created at
    updated = models.DateTimeField(verbose_name=_('Updated Date'), auto_now=True, blank=True, null=True)     #updated at
    categories = models.ManyToManyField(BlogCategory)
    tags = models.ManyToManyField(BlogTag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')


class Interests(models.Model):
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=100)
    interests = models.ManyToManyField(Interests)

    def __str__(self):
        return self.name


class PersonAddress(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.person.name + "(" + self.street_address + ")"

