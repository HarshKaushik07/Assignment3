# shopapp/views.py
from django.shortcuts import render
from .models import Shop
from .utils import haversine

def search_shops(request):
    if request.method == 'GET':
        user_lat = float(request.GET.get('latitude'))
        user_lon = float(request.GET.get('longitude'))

        shops = Shop.objects.all()
        shop_distances = []

        for shop in shops:
            distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
            shop_distances.append({'shop': shop, 'distance': distance})

        # Sort the shops by distance
        sorted_shops = sorted(shop_distances, key=lambda x: x['distance'])

        # Debugging: Print sorted shops
        print(sorted_shops)

        return render(request, 'shop_list.html', {'shops': sorted_shops})
