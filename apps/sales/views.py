from django.shortcuts import render


def sales_view(request):
    return render(request, 'sales.html')
