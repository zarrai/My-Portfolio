from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


def blog(request):
    post_list = Post.objects.all().order_by("-timestamp")
    category_count = get_category_count()
    context = {
        "post_list": post_list,
        "category_count": category_count,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    random_post = Post.objects.all().order_by("?")[:3]
    featured = Post.objects.filter(featured=True).order_by("?")[0:3]
    latest = Post.objects.order_by("-timestamp")[0:3]
    meta = post.as_meta()
    context = {
        "post": post,
        "random_post": random_post,
        "latest": latest,
        "featured": featured,
        "meta": meta,
    }
    return render(request, "blog/post.html", context)


def post_category(request, title):
    categories = Category.objects.all()
    category_count = get_category_count()
    if title:
        category = get_object_or_404(Category, title=title)
        posts = Post.objects.filter(categories=category)
    context = {
        "categories": categories,
        "category": category,
        "posts": posts,
        "category_count": category_count,
    }
    return render(request, "blog/post_category.html", context)
