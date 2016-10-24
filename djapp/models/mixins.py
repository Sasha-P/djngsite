from django.db import models
from django.conf import settings
from django.utils import timezone


class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')

    class Meta:
        abstract = True


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class PublishMixin(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    published = PublishedManager()

    class Meta:
        abstract = True
