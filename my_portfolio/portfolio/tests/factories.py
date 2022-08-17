from django.template.defaultfilters import slugify
from factory import Faker, fuzzy
from factory.django import DjangoModelFactory

from my_portfolio.portfolio.models import Project


class ProjectFactory(DjangoModelFactory):
    title = Faker("name")
    slug = slugify("name")
    description = Faker("sentence")
    image = Faker("image_url")
    tags = Faker("name")
    demo = Faker("url")
    github = Faker("url")
    created_at = Faker("user_name")
    show_in_slider = fuzzy.FuzzyChoice(choices=[True, True, True, False])

    class Meta:
        model = Project
        django_get_or_create = ("title",)
