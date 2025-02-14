from django.shortcuts import render, get_object_or_404, redirect
from movieStore.models import Movie, Cart
from .utils import calculate_cart_total

def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('home.index')

def index(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if movie_ids:
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)
    template_data = {
        'title': 'Cart',
        'movies_in_cart': movies_in_cart,
        'cart_total': cart_total,
    }
    return render(request, 'cart/index.html', {'template_data': template_data})

def add_to_cart(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')
# removing all the elements from the cart
def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')

# add multiple items of a movie in the cart
def add_multiple_items_of_movie_to_cart(request, movie_id):
    if request.user.is_authenticated:
        qty = int(request.POST.get('quantity', 1))
        movie = Movie.objects.get(id=movie_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, movie=movie)
        if not created:
            cart_item.quantity += qty
        else:
            cart_item.quantity = qty
        cart_item.save()
        return redirect('cart.index')
    else:
        return redirect('signup')
    
