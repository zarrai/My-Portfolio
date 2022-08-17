from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ["title", "content", "overview"]
    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
