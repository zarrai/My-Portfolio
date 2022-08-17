import pytest

from my_portfolio.portfolio.models import Project
from my_portfolio.portfolio.tests.factories import ProjectFactory
from my_portfolio.users.models import User
from my_portfolio.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def project() -> Project:
    return ProjectFactory()
