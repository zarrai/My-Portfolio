from django.urls import path

from .views import blog, post_category, post_detail

app_name = "blog"

urlpatterns = [
    path("", blog, name="home"),
    path("<slug>/", post_detail, name="post_detail"),
    path("category/<title>", post_category, name="post_category"),
]
