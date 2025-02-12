
from django.urls import path, include
from . import views
from .views import cart, add_movie_to_cart


app_name = "movieStore"
urlpatterns = [

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add-to-cart/<int:movie_id>/', add_movie_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),

    path('',views.home,name='home'),
    path('movies', views.IndexView.as_view(), name="movies"),
]
