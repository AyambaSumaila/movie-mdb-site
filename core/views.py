from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView
    )

from core.models import Movie, Person
# Create your views here.

class MovieList(ListView):
    model= Movie
    
   
   

class MovieDetail(DetailView):
    queryset=(
        Movie.objects.all_with_related_persons()
    )
    model= Movie
     
    
class PersonDetail(DetailView):
    queryset=Person.objects.all_with_prefetch_movies()
    