from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

menu = [
    {'title': 'Добавить статью', 'url_name': 'index'},
    {'title': 'Войти', 'url_name': 'index'},
]


class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('cat')


class ShowPost(DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class BlogCategory(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        context['menu'] = menu
        return context

