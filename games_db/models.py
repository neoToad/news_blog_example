from django.db import models
from itertools import chain
from django.utils import timezone
from django.contrib import admin
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Connection(models.Model):
    """ Game info """
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """ Author info """
    first_name = models.CharField(max_length=50, blank='True', null=True)
    last_name = models.CharField(max_length=50)
    author_description = models.TextField(max_length=300, blank='True', null=True)
    author_pic = models.ImageField(null=True, blank=True)
    author_fb = models.CharField(max_length=100, null=True, blank=True)
    author_tw = models.CharField(max_length=100, null=True, blank=True)
    author_ig = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.first_name:
            return f"{self.first_name}  {self.last_name}"
        else:
            return self.last_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author',)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=350, null=True, blank=True)
    main_image = models.ImageField()
    fb_image = models.ImageField(null=True, blank=True)
    alt_img_tag = models.CharField(max_length=125, null=True, blank=True,)
    image_credit = models.CharField(max_length=125, null=True, blank=True,)
    connections = models.ManyToManyField(Connection, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    description_len = models.PositiveIntegerField(null=True, blank=True)

    side_banner = models.BooleanField(default=True)
    ad_name = models.CharField(max_length=100, null=True, blank=True)

    article_category = models.CharField(max_length=20,
        choices=(
            ('NEWS', 'NEWS'),
            ('DEALS', 'DEALS'),
            ('GUIDES', 'GUIDES'),
            ('REVIEWS', 'REVIEWS'),
        )
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.description_len = len(self.description)
        return super(Article, self).save(*args, **kwargs)


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_contents')
    block_quotes = models.CharField(max_length=200, null=True, blank=True)
    paragraph = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    alt_img_tag = models.CharField(max_length=125, null=True, blank=True,)
    image_credit = models.CharField(max_length=125, null=True, blank=True,)

    def __str__(self):
        return self.paragraph


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class EmailList(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email