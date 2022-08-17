import pytest
from django.urls import resolve, reverse

from my_portfolio.portfolio.models import Project

pytestmark = pytest.mark.django_db


def test_project(project: Project):
    assert (
        reverse("index:projectDetail", kwargs={"slug": project.slug})
        == f"/projects/{project.slug}/"
    )
    assert resolve(f"/projects/{project.slug}/").view_name == "index:projectDetail"
