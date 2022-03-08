from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Orders, Order
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

# Create your views here.

@csrf_exempt
def orders(request, shop):
  if request.method == 'GET':
    orders = Orders.objects.filter(shop=shop)
    return render(request, 'supervise/orders.html', { 'orders': orders })
  else:
    return HttpResponse(status=404)

@csrf_exempt
def estimated(request):
  if request.method == 'POST': 
    order = Orders.objects.get(pk=request.POST['order_id'])
    shop = order.shop
    order.estimated_time = int(request.POST['estimated_time'])
    order.save()
    return render(request, 'supervise/estimated.html', { 'shop': shop })
  else:
    return HttpResponse(status=404)