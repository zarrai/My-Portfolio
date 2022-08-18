from django.db import models
from django.urls import reverse
from meta.models import ModelMeta
from taggit.managers import TaggableManager

from .managers import post_filename


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_category", kwargs={"title": str(self.title)})

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "categories"


class Post(ModelMeta, models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    image = models.FileField(upload_to=post_filename)
    tags = TaggableManager(
        blank=True, help_text="add keyword for the page to improve seo"
    )
    featured = models.BooleanField()

    _metadata = {
        "title": "title",
        "description": "overview",
        "image": "get_meta_image",
        "keywords": "get_list_tags",
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": str(self.slug)})

    def get_meta_image(self):
        return self.image.url

    def get_list_tags(self):
        taglist = []
        for tag in self.tags.all():
            taglist.append(tag.name)
        return taglist

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
