from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Orders, Order
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

# Create your views here.
@csrf_exempt
def shop(request):
  if request.method == 'GET':
    # shop = Shop.objects.all()
    # serializer = ShopSerializer(shop, many=True)
    # return JsonResponse(serializer.data, safe=False)
    shop = Shop.objects.all()
    return render(request, 'order/shops.html', {'shops': shop})

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ShopSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def menu(request, shop):
  if request.method == 'GET':
    menu = Menu.objects.filter(shop=shop)
    # serializer = MenuSerializer(menu, many=True)
    return render(request, 'order/menus.html', {'menus': menu, 'shop': shop})
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = MenuSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def orders(request):
  if request.method == 'POST':
    address = request.POST['address']
    shop = request.POST['shop']
    date = timezone.now()
    foods = request.POST.getlist('food')

    shop = Shop.objects.get(pk=shop)
    shop.orders_set.create(shop=shop, address=address, date=date)

    order = Orders.objects.get(pk=shop.orders_set.latest('date').id)
    for food in foods:
      order.order_set.create(food=food)
    return render(request, 'order/ordered.html')
    
  elif request.method == 'GET':
    orders = Orders.objects.all()
    return render(request, 'order/orders.html', {'orders': orders})