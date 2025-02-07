from django.urls import path
from .views import signup
from .views import add_movie_to_cart, cart


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('add-to-cart/<int:movie_id>/', add_movie_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),


]
