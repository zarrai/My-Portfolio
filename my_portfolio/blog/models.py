from django.db import models
from .managers import post_filename
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_category", kwargs={"title": str(self.title)})
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True )
    overview = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    image = models.FileField(upload_to=post_filename)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'