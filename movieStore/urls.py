from django.urls import path

from . import views

app_name = "movieStore"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('signup/', signup, name='signup'),
    path('add-to-cart/<int:movie_id>/', add_movie_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]
