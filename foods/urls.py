from django.urls import path
from .views import FoodsListView, FoodsDetailView, DrinkListView, CakeListView, BurgerListView, SearchResultsView

urlpatterns = [
    path('list/', FoodsListView.as_view(), name='foods_list'),
    path('burgers/', BurgerListView.as_view(), name='burger'),
    path('cakes/', CakeListView.as_view(), name='cake'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    path('drinks', DrinkListView.as_view(), name='drink'),
    path('detail/<int:pk>/', FoodsDetailView.as_view(), name='foods_detail'),
]