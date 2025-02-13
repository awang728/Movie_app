
from django.urls import path, include
from . import views
from .views import cart, add_movie_to_cart


app_name = "movieStore"
urlpatterns = [

    path('cart/', views.cart, name='cart'),  
    path('cart/add/<int:movie_id>/', views.add_movie_to_cart, name='add_movie_to_cart'),

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add-to-cart/<int:movie_id>/', add_movie_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('', views.index, name='cart.index'),
    path('remove/', views.remove, name='cart.remove'),
    path('add_multiple_items_of_movie_to_cart/<int:movie_id>/', views.add_multiple_items_of_movie_to_cart, name='add_multiple_items_of_movie_to_cart'),



    path('',views.home,name='home'),
    path('index', views.IndexView.as_view(), name="index"),
]
