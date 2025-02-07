from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Movie, Cart
# Create your views here.
def signup(request):
    if (request.method=='POST'):
        form=UserCreationForm(request.Post)
        if form.is_valid():
            user=form.save()
            login(request,user)
            form.save()
            return redirect('home')
    elif (request.method=='GET'):
        form=UserCreationForm()
        return render(request, 'Mymovies/signup.html', {'form':form})
#Used chatGPT for help on this method
def add_movie_to_cart(request, movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user_name, movie=movie)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')  # Redirect to cart page
    else:
        return redirect('signup')
def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, 'movies/cart.html', {'cart_items': cart_items})
    else:
        return redirect('signup')
