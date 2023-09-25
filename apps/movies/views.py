from django.shortcuts import render


def movies_register(request):
    return render(request, 'home.html')
