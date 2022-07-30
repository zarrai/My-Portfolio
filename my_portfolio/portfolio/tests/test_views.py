import pytest
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest, HttpResponseRedirect
from django.test import RequestFactory
from django.urls import reverse

from my_portfolio.portfolio.models import Project
from django.shortcuts import get_object_or_404
from my_portfolio.portfolio.forms import MessageForm
from my_portfolio.portfolio.tests.factories import ProjectFactory
from my_portfolio.portfolio.views import (
    projectDetail,
    search,
)
from django.core.exceptions import MultipleObjectsReturned

pytestmark = pytest.mark.django_db

@pytest.mark.parametrize('param',
[
    ('portfolio:home'),
    ('portfolio:projectsPage'),
])
def test_views(client,param):
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
        request = rf.post("/fake-url/", kwargs={'search_text':project.slug})
        request.project = ProjectFactory()

        response = search(request)

        assert response.status_code == 200