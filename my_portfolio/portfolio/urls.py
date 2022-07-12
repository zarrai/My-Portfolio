from django.urls import path

from my_portfolio.portfolio.views import (
    Home,
)

app_name = "portfolio"
urlpatterns = [
    path("", view=Home, name="home"),
]
