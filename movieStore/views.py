from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render
from django.views import generic
from django.contrib import messages
from .models import Movie, Cart, Review


# Create your views here.
def home(request):
    count= User.objects.count()
    return render(request, 'home.html',{'count':count})

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
        return render(request, 'cart.html', {'cart_items': cart_items})
    else:
        return redirect('signup')


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
            messages.error(request, "Your current review is empty!") # Asked ChatGPT to give recommendations on what to improve, it recommended adding messages so I did that for all.
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



