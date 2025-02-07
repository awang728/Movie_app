
from django.urls import path, include
from . import views
from .views import signup, cart, add_movie_to_cart

urlpatterns = [

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('signup/', signup, name='signup'),
    path('add-to-cart/<int:movie_id>/', add_movie_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),

    path('',views.home,name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('index', views.IndexView.as_view(), name="index"),
]
