from .models import Project
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_projects(request, projects, results):
    page = request.GET.get('page', 1)
    # results = 3
    paginator = Paginator(projects, results, allow_empty_first_page=True)  #, allow_empty_first_page=False

    # try:
    #     pr = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     pr = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     pr = paginator.page(page)
    projects = paginator.get_page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, projects


def search_projects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(
        description__icontains=search_query)
                                           | Q(
        owner__name__icontains=search_query) |
                                           Q(tags__name__icontains=search_query))  # | Q(tags__in=tags)
    return projects, search_query
