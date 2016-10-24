from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from .mixins import AuthorMixin, TimeStampMixin, PublishMixin


class Post(AuthorMixin, PublishMixin, TimeStampMixin, models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    objects = models.Manager()

    def get_absolute_url(self):
        cd = timezone.make_naive(self.publish, timezone.get_default_timezone())
        return reverse('blog:post_detail',
                       args=[cd.year,
                             cd.strftime('%m'),
                             cd.strftime('%d'),
                             self.slug])

    def get_archives(self):
        return Post.published.datetimes('publish', 'month')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
