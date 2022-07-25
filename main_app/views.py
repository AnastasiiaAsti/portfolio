from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from .forms import ContactForm
# from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

import uuid
import boto3
import os
from .models import Project, Post, Skill, Photo
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})


def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def add_photo(request, project_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, project_id=project_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('projects_index', project_id=project_id)
