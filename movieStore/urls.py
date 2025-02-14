from django.urls import path
from . import views

app_name = 'movieStore'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add_to_cart/<int:movie_id>/', views.add_movie_to_cart, name='add_movie_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/', views.remove, name='cart.remove'),
    path('add_multiple_items_of_movie_to_cart/<int:movie_id>/', views.add_multiple_items_of_movie_to_cart, name='add_multiple_items_of_movie_to_cart'),
]
