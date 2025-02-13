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

def show(request, id):
    movie = get_object_or_404(Movie, id=id)
    reviews = Review.objects.filter(movie=movie)
    return render(
        request, "movieStore/show.html", {"title": movie.movie_name, "movie": movie, "reviews": reviews}
    )


@login_required
def create_review(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        comment = request.POST.get("comment", "").strip()

        if not comment:
            messages.error(request, "Your current review is empty!")
            return redirect("detail", pk=id)

        # Create and save the review
        Review.objects.create(
            comment=comment,
            movie=movie,
            user=request.user
        )
        messages.success(request, "Thanks for leaving a review!")

    return redirect("detail", id=id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user != review.user:
        messages.error(request, "Sorry, you cannot edit this review.")
        return redirect("detail", id=id)

    if request.method == "GET":
        return render(request, "movieStore/edit_review.html", {"title": "Edit Review", "review": review})

    if request.method == "POST":
        comment = request.POST.get("comment", "").strip()
        if not comment:
            messages.error(request, "Sorry, your review cannot be empty.")
            return render(request, "movieStore/edit_review.html", {"title": "Edit Review", "review": review})

        review.comment = comment
        review.save()
        messages.success(request, "Your review has been updated!")
        return redirect("detail", id=id)


@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, "Your review was successfully deleted.")
    return redirect("detail", id=id)

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
