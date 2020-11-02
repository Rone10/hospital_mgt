from django.views.generic import ListView, TemplateView
from .models import City
from django.db.models import Q
# Create your views here.

class SearchView(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'search/cities_list.html'

    def get_queryset(self):
        name = self.request.GET.get('name')
        region = self.request.GET.get('region')
        results = City.objects.filter(Q(name__icontains=name)| Q(region__icontains=region))
        return results


class SearchFormView(TemplateView):
    template_name = 'search/search_form.html'
