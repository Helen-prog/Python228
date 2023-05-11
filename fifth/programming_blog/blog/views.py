from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'


