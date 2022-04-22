from sqlalchemy import desc, text, update, and_

from flask import Blueprint, jsonify, request
from flask_login import current_user
from app.models import Product, User, db
from app import route_utils

user_api = Blueprint('user_api', __name__)


@user_api.route('/api/user/cart/', methods=['POST'])
def add_to_cart():
    data = request.args.to_dict()
    user = current_user
    product_id = data['product_id']

    print(user)

    return {'ok': 'ok'}
