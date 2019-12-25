from django.db import models
from play_django.apps.core.models import TimeStampedModel


class Article(TimeStampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    tags = models.ManyToManyField('articles.Tag', related_name='articles')

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'profiles.Profile', related_name='comments', on_delete=models.CASCADE
    )


class Tag(TimeStampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag
