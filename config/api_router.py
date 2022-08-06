from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_portfolio.blog.api.views import CategoryViewSet, PostViewSet
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

# portfolio
router.register("portfolio", PortfolioViewSet, basename="portfolio")
router.register("projects", ProjectViewSet, basename="projects")
router.register("education", EducationViewSet, basename="education")
router.register("competence", CompetenceViewSet, basename="competence")
router.register("information", InformationViewSet, basename="information")
router.register("experience", ExperienceViewSet, basename="experience")
# blog
router.register("blog-post", PostViewSet, basename="blog-post")
router.register("blog-categories", CategoryViewSet, basename="blog-categories")
# users
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
