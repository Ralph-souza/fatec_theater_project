from django.shortcuts import render


def sales_register(request):
    return render(request, 'sales.html')
