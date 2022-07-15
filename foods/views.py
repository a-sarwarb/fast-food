from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Foods
from django.db.models import Q
import requests
# Create your views here.
class FoodsListView(ListView):
    model = Foods
    template_name = 'foods_list.html'

class FoodsDetailView(DetailView):
    model = Foods
    template_name = 'foods_detail.html'

class BurgerListView(ListView):
    model = Foods
    template_name = 'burger.html'

class CakeListView(ListView):
    model = Foods
    template_name = 'cake.html'

class DrinkListView(ListView):
    model = Foods
    template_name = 'drink.html'

class SearchResultsView(ListView):
    model = Foods
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Foods.objects.filter(
            Q(photo__icontains=query) | Q(name__icontains=query)
        )
        return object_list

