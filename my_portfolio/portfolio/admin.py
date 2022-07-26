from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Competence, Education, Experience, Project, Message, Information

class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','created_at')
    list_filter = ("created_at",)
    search_fields = ['title', 'description',]
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('description',)


admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Competence)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Message)