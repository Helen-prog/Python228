from django.shortcuts import render
from .models import Profile


def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    prof = Profile.objects.get(id=pk)
    context = {
        'profile': prof,
    }
    return render(request, 'users/profile.html', context)
