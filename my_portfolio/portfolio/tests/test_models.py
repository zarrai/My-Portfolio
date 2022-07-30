import pytest

from my_portfolio.portfolio.models import Project

pytestmark = pytest.mark.django_db


def test_project_get_absolute_url(project: Project):
    assert project.get_absolute_url() == f"/projects/{project.slug}/"
