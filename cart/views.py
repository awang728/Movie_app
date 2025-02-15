from django.shortcuts import render, get_object_or_404, redirect
from movieStore.models import Movie
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def add(request, id):
    get_object_or_404(Movie, movie_id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('movieStore:home')

def index(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if movie_ids:
        movies_in_cart = Movie.objects.filter(movie_id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)
    template_data = {
        'title': 'Cart',
        'movies_in_cart': movies_in_cart,
        'cart_total': cart_total,
    }
    return render(request, 'cart/index.html', {'template_data': template_data})

def add_to_cart(request, id):
    get_object_or_404(Movie, movie_id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart:index')
# removing all the elements from the cart
def clear(request):
    request.session['cart'] = {}
    return redirect('cart:index')

# add multiple items of a movie in the cart


@login_required
def purchase(request):
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids == []):
        return redirect('cart.index')
    movies_in_cart = Movie.objects.filter(movie_id__in=movie_ids)
    cart_total = calculate_cart_total(cart, movies_in_cart)
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()
    for movie in movies_in_cart:
        item = Item()
        item.movie = movie
        item.price = movie.dollar_price
        item.order = order
        item.quantity = cart[str(movie.movie_id)]
        item.save()
    request.session['cart'] = {}
    template_data = {}
    template_data['title'] = 'Purchase confirmation'
    template_data['order_id'] = order.id
    return render(request, 'cart/purchase.html',
        {'template_data': template_data})
