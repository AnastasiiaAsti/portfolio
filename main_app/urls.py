from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name="projects_index"),
    path('posts/', views.posts_index, name="posts_index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
