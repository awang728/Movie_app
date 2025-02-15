
from django.urls import path, include
from . import views


app_name = "movieStore"
urlpatterns = [

    path("movies/<int:id>/", views.show, name="show"),


    path('',views.home,name='home'),
    path('movies', views.IndexView.as_view(), name="movies"),
    path("<int:id>/review/create/", views.create_review, name="create_review"),
    path("<int:id>/review/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    path("<int:id>/review/<int:review_id>/delete/", views.delete_review, name="delete_review"),
]
