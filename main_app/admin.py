from django.contrib import admin
from .models import Project, Post, Skill, Photo

# Register your models here.


admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(Photo)
