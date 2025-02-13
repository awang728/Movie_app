def cart_total_price(cart, movies):
    totalPrice = 0
    for i in movies:
        qty = cart[str(i.id)]
        totalPrice += i.price * int(qty)
    return totalPrice