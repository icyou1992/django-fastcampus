from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Orders, Order
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

# Create your views here.

@csrf_exempt
def orders(request):
  if request.method == 'GET':
    orders = Orders.objects.all()
    return render(request, 'delivery/orders.html', { 'orders': orders })

  elif request.method == 'POST': 
    order = Orders.objects.get(pk=request.POST['order_id'])
    order.delivered = 1
    order.save()
    return render(request, 'delivery/delivered.html')

  else:
    return HttpResponse(status=404)