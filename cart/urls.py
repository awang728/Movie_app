from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/add/', views.add_to_cart, name='add_to_cart'),
    path('clear/', views.clear, name='clear'),
    path('purchase/', views.purchase, name='cart.purchase'),
    path('orders/', views.orders, name='accounts.orders'),
    path('add_multiple_items_of_movie_to_cart/<int:movie_id>/', views.add_multiple_items_of_movie_to_cart, name='add_multiple_items_of_movie_to_cart'),

]
