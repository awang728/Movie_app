from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.shortcuts import  render
from django.views import generic

from .models import Movie, Cart
from .utils import cart_total_price



# Create your views here.
def home(request):
    count= User.objects.count()
    return render(request, 'home.html',{'count':count})

class IndexView(generic.ListView):
    template_name = "movieStore/index.html"
    context_object_name = "movie_list"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(movie_name__icontains=query)
        return Movie.objects.all()

class DetailView(generic.DetailView):
    model = Movie
    template_name = "movieStore/detail.html"


def add_movie_to_cart(request, movie_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, movie=movie)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')  
    else:
        return redirect('signup')

def remove(request):
    request.session['cart'] = {}
    return redirect('cart')
def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, 'cart.html', {'cart_items': cart_items})
    else:
        return redirect('signup')
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
    return redirect('cart')
def index(request):
    total_price = 0   
    cart = request.session.get('cart', {})
   
    movies = []            
    movieID = list(cart.keys())

    if (movieID != []):
        movies = Movie.objects.filter(id__in = movieID)
        total_price = cart_total_price(cart, movies)
    template_data = {}
    template_data['movies_in_cart'] = movies

    template_data['title'] = 'Cart'
    template_data['cart_total'] = total_price
    return render(request, 'cart/index.html', {'template_data': template_data})





