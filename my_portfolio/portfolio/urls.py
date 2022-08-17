from django.urls import path

from my_portfolio.portfolio.views import (
    Home,
    handler404,
    projectDetail,
    projectsPage,
    search,
)

app_name = "portfolio"

handler404 = handler404

urlpatterns = [
    path("", view=Home, name="home"),
    path("projects/", projectsPage, name="projectsPage"),
    path("projects/<str:slug>/", projectDetail, name="projectDetail"),
    path("search/", search, name="search"),
]
