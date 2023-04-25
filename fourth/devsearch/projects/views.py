from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import search_projects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def projects(request):
    pr, search_query = search_projects(request)
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(pr, results, allow_empty_first_page=False)

    # try:
    #     pr = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     pr = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     pr = paginator.page(page)
    pr = paginator.get_page(page)

    left_index = int(page) - 4

    right_index = int(page) + 5

    custom_range = range(left_index, right_index)

    context = {
        'projects': pr,
        'search_query': search_query,
        'paginator': paginator,
        'custom_range': custom_range
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # new_tags = request.POST.get('tags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            # for tag in new_tags:
            #     tag, created = Tag.objects.get_or_create(name=tag)
            #     print(tag)
            #     project.tags.add(tag.name)
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete.html', context)
