from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project, Post, Skill
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})


def contact(request):
    return render(request, 'contact.html')


def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})
