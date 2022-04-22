from crypt import methods
from sqlalchemy import desc, text, update, and_

from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import Product, User, db
from app import route_utils

product_api = Blueprint('product_api', __name__)


@product_api.route('/api/product/', methods=['GET'])
def get_product():
    data = request.args.to_dict()
    id = data['id']
    return jsonify(Product.query.filter_by(id=id).first())


@product_api.route('/api/products/', methods=['GET'])
def get_products():
    return jsonify(Product.query.all())


@product_api.route('/api/cookie/', methods=['POST'])
def set_new_cookie():
    data = request.args.to_dict()
    name = data['name']
    value = data['value']

    route_utils.set_cookie(name, value)
    return {'cookie set': f'{name}: {value}'}


@product_api.route('/api/cookie/', methods=['GET'])
def get_cookie():
    data = request.args.to_dict()
    name = data['name']

    value = route_utils.get_cookie(name)
    return {'coockie': value}


@product_api.route('/api/products/lazy_load/', methods=['GET'])
def lazy_load():
    data = request.args.to_dict()
    product_id = data['id']
    type = data['category']

    if product_id == '0':
        if type:
            return jsonify(Product.query.filter(Product.type == type).
                    order_by(desc(text('id'))).limit(20).all())

        return jsonify(Product.query.order_by(desc(text('id'))).
                        limit(20).all())
    
    if type:
        return jsonify(Product.query.filter(
            and_(Product.id < product_id, Product.type == type)).
                order_by(desc(text('id'))).limit(20).all())

    return jsonify(Product.query.filter(Product.id < product_id).
                order_by(desc(text('id'))).limit(20).all())


@product_api.route('/api/user/cart/', methods=['POST'])
def add_to_cart():
    data = request.args.to_dict()
    user = current_user
    product_id = data['product_id']
    count = data['count']

    db.session.execute(update(
        User
    ).filter(User.id==user.id).values(cart=text(f'array_append({User.cart.name}, :tag)')),
    {'tag': f'{product_id}_{count}'})

    db.session.commit()

    return {'status': 'ok'}


@product_api.route('/api/user/cart/', methods=['DELETE'])
def checkout_cart():
    user = current_user

    db.session.execute(update(
        User
    ).filter(User.id==user.id).values(cart=text('null')))

    db.session.commit()

    return {'status': 'ok'}
