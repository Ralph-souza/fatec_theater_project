from django.shortcuts import render, redirect

from apps.movies.models import MoviesModel, RoomsModel

from apps.sales.models import MovieSalesModel, SeatSalesModel
from apps.sales.forms import MovieSalesForm, SeatSalesForm

def movie_sales_view(request):
    context = {}

    if request.POST:
        movie_sales_form = MovieSalesForm(request.POST)
        if movie_sales_form.is_valid():
            room_id = movie_sales_form.cleaned_data["sold_room"]
            movie_title = movie_sales_form.cleaned_data["sold_movie"]

            room_instance = RoomsModel.objects.get(id=room_id)
            movie_instance = MoviesModel.objects.get(title=movie_title)

            MovieSalesModel.objects.create(sold_room=room_instance, sold_movie=movie_instance)

            return redirect('seats')
        
    else:
        movie_sales_form = MovieSalesForm()
    
    context["movie_sales_form"] = movie_sales_form
    return render(request, 'sales.html', context)


def seat_sales_view(request):
    context = {}

    if request.POST:
        sales_form = SeatSalesForm(request.POST)
        if sales_form.is_valid():
            sales_form.save()

            return redirect('ticket')
        
    else:
        sales_form = SeatSalesForm()
    
    context["seat_sales_form"] = sales_form
    return render(request, 'seats.html', context)
