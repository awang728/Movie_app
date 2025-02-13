from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import  render
from django.views import generic

from .models import Movie, Cart, Review


# Create your views here.
def home(request):
    count= User.objects.count()
    return render(request, 'home.html',{'count':count})

# Create your views here.
class IndexView(generic.ListView):
    template_name = "movieStore/movies.html"
    context_object_name = "movie_list"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(movie_name__icontains=query).order_by('movie_name')
        return Movie.objects.all().order_by('movie_name')

class DetailView(generic.DetailView):
    model = Movie
    template_name = "movieStore/detail.html"
    context_object_name = "review_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_list"] = Review.objects.filter(movie=self.object).order_by('-date')
        return context

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return HttpResponse(request, 'cart.html', {'cart_items': cart_items})
    else:
        return redirect('signup')

def add_movie_to_cart(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        cart_item, created = Cart.objects.get_or_create(userName=request.user, movie_id=movie)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')  # Redirect to cart page
    else:
        return redirect('signup')