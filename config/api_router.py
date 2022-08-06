from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_portfolio.portfolio.api.views import (
    CompetenceViewSet,
    EducationViewSet,
    ExperienceViewSet,
    InformationViewSet,
    PortfolioViewSet,
    ProjectViewSet,
)
from my_portfolio.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("portfolio", PortfolioViewSet, basename="portfolio")
router.register("projects", ProjectViewSet, basename="projects")
router.register("education", EducationViewSet, basename="education")
router.register("competence", CompetenceViewSet, basename="competence")
router.register("information", InformationViewSet, basename="information")
router.register("experience", ExperienceViewSet, basename="experience")
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
