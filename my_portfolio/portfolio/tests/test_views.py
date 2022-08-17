import pytest
from django.core.exceptions import MultipleObjectsReturned
from django.test import RequestFactory
from django.urls import reverse

from my_portfolio.portfolio.models import Project
from my_portfolio.portfolio.tests.factories import ProjectFactory
from my_portfolio.portfolio.views import projectDetail, search

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "param",
    [
        ("portfolio:home"),
        ("portfolio:projectsPage"),
    ],
)
def test_views(client, param):
    path = reverse(param)
    resp = client.get(path)
    assert resp.status_code == 200


class TestProjectDetailView:
    def test_detail(self, project: Project, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.project = ProjectFactory()
        try:
            response = projectDetail(request, slug=project.slug)
        except MultipleObjectsReturned:
            return "MultipleObjectsReturned"

        assert response.status_code == 200


class TestProjectSearchView:
    def test_search(self, project: Project, rf: RequestFactory):
        request = rf.post("/fake-url/", kwargs={"search_text": project.slug})
        request.project = ProjectFactory()

        response = search(request)

        assert response.status_code == 200
