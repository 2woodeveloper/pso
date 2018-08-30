# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Subject, Comment

def write(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/write.html', {'subjects': subjects})

def main_subject(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/main.html', {'subjects': subjects})

def main_post(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/main_block_content.html', {'posts': posts})

def login(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/login.html', {'subjects': subjects})

def signup(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/signup.html', {'subjects': subjects})

def look(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/look.html', {'subjects': subjects})

def looks(request, post_id):
#    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date') <--- 에러 해결해야함
    posts = Post.objects.filter(id = post_id)
    return render(request, 'fs4pso/look2.html', {'posts' : posts})
#   {'subjects' : subjects} <- 에러 해결해야함

def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    post.num_of_likes += 1
    post.save()
    return HttpResponseRedirect("/look/{}".format(post.id))