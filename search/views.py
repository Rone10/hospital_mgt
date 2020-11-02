from django.views.generic import ListView
from .models import City
# Create your views here.

class SearchView(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'search/cities_list.html'