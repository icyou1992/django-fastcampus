from django.urls import path
from supervise import views

urlpatterns = [
    path('orders/<int:shop>', views.orders, name='orders'),
    path('estimated/', views.estimated, name='estimated'),
]
