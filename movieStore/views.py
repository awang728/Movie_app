from django.utils import timezone
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Movie

# Create your views here.
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
# Tisha views
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
