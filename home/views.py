from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')




