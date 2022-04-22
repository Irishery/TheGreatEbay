from flask import make_response, render_template, request
from flask_login import current_user
from app.models import User, Product, db

def set_cookie(name, value):
    response = make_response( render_template('index.html') )
    response.set_cookie(name, value)
    return response

def get_cookie(name):
    return request.cookies.get(name)

def get_cart():
    user = current_user

    cart_products = []

    total = 0
    
    if not user.cart:
        return [], 0
    
    for item in user.cart:
        product_id, count = item.split('_')
        product = Product.query.filter_by(id=product_id).first()
        
        total += product.cost * int(count)

        cart_products.append((product, count))

    return cart_products, total
