from django.conf.urls import url
from django.urls import path
from .views import (
    blog, post_detail, post_category
)

app_name = 'blog'

urlpatterns = [
    path('', blog, name="home"),
    path('<slug>/', post_detail, name="post_detail"),
    path('category/<title>', post_category, name='post_category')
]