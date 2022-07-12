from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_portfolio.users.api.views import UserViewSet
from my_portfolio.portfolio.api.views import PortfolioViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", PortfolioViewSet, basename='portfolio')
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
