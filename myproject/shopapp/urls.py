from django.urls import path
from .views import search_shops

urlpatterns = [
    path('search-shops/', search_shops, name='search_shops'),
]