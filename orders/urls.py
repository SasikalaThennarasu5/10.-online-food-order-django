from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'),
]
