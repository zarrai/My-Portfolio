from django.db import models
from django.urls import reverse
from meta.models import ModelMeta
from taggit.managers import TaggableManager


class Information(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    cv = models.FileField(upload_to="cv", blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    upwork = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class Competence(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.FileField(upload_to="competence/", blank=False, null=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    the_year = models.DateTimeField(auto_now=False, null=False)

    def __str__(self):
        return self.title

    def year(self):
        return self.the_year.strftime("%Y")


class Experience(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    the_year = models.DateTimeField(auto_now=False, null=False)

    def __str__(self):
        return self.title

    def year(self):
        return self.the_year.strftime("%Y")


class Project(ModelMeta, models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="projects/", blank=False, null=False)
    tags = TaggableManager(
        blank=True, help_text="add keyword for the page to improve seo"
    )
    demo = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    show_in_slider = models.BooleanField(default=False)

    _metadata = {
        "title": "title",
        "description": "description",
        "image": "get_meta_image",
        "keywords": "get_list_tags",
    }

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index:projectDetail", kwargs={"slug": str(self.slug)})

    def get_meta_image(self):
        return self.image.url

    def get_list_tags(self):
        taglist = []
        for tag in self.tags.all():
            taglist.append(tag.name)
        return taglist


class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
