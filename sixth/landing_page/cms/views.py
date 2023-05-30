from django.shortcuts import render
from .models import CmsSlider


def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(request, 'cms/index.html', {'slider_list': slider_list})
