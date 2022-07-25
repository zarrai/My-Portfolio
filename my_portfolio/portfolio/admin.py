from django.contrib import admin
from .models import Competence, Education, Experience, Project, Message, Information

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_at')
    list_filter = ("created_at",)
    search_fields = ['title', 'description',]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Competence)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Message)