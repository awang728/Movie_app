
from django.urls import path, include
from . import views
from .views import cart, add_movie_to_cart


app_name = "movieStore"
urlpatterns = [

    path("movies/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add_to_cart/<int:pk>/', views.add_movie_to_cart, name='add_movie_to_cart'),
    path('cart/', views.Cart, name='cart'),

    path('',views.home,name='home'),
    path('movies', views.IndexView.as_view(), name="movies"),
    path("<int:id>/review/create/", views.create_review, name="create_review"),
    path("<int:id>/review/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    path("<int:id>/review/<int:review_id>/delete/", views.delete_review, name="delete_review"),
]
