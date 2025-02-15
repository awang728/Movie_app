def calculate_cart_total(cart, movies_in_cart):
    total = 0
    for movie in movies_in_cart:
        quantity = cart[str(movie.movie_id)]
        total += movie.dollar_price * int(quantity)
    return total