from django.urls import path
from delivery import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    # path('estimated/', views.estimated, name='estimated'),
]
