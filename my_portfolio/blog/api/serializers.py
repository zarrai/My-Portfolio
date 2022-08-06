from rest_framework import serializers

from my_portfolio.blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
