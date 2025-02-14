from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Movie, Review, Cart


def home(request):
    count = User.objects.count()
    return render(request, "home.html", {"count": count})


class IndexView(generic.ListView):
    template_name = "movieStore/movies.html"
    context_object_name = "movie_list"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Movie.objects.filter(movie_name__icontains=query)
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = "movieStore/detail.html"



def show(request, id):
    movie = get_object_or_404(Movie, movie_id=id)
    reviews = Review.objects.filter(movie=movie)
    template_data = {}
    template_data['title'] = movie.movie_name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movieStore/show.html',
                  {'template_data': template_data})


@login_required
def create_review(request, id):
    movie = get_object_or_404(Movie, movie_id=id)

    if request.method == "POST":
        comment = request.POST.get("comment", "").strip()

        if not comment:
            messages.error(request, "Your current review is empty!") # Asked ChatGPT to give recommendations on what to improve, it recommended adding messages so I did that for all.
            return redirect("movieStore:show", movie_id=id)

        # Create and save the review
        Review.objects.create(
            comment=comment,
            movie=movie,
            user=request.user
        )
        messages.success(request, "Thanks for leaving a review!")

    return redirect("movieStore:show", id=movie.movie_id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    movie = get_object_or_404(Movie, movie_id=id)

    if request.user != review.user:
        messages.error(request, "Sorry, you cannot edit this review.")
        return redirect("movieStore:show", id=movie.movie_id)

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
        return redirect("movieStore:show", id=movie.movie_id)


@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    movie = get_object_or_404(Movie, movie_id=id)
    if request.method == "POST":  # Only allow deletion via POST request
        review.delete()
        return redirect("movieStore:show", id=movie.movie_id)
        messages.success(request, "Your review was successfully deleted.")
    return redirect("movieStore:show", id=movie.movie_id)



