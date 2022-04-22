from crypt import methods
import os
from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from app.forms.edit_profile import EditProfile, AddProduct
from app.models import db, User, Product
from app import ALLOWED_EXTENSIONS, upload_folder
from werkzeug.utils import secure_filename
from .routes_utils import get_cart

main_route = Blueprint("main_route", __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main_route.route("/")
@main_route.route('/main')
@login_required
def index():
    products = Product.query.all()
    print(products)
    return render_template('index.html', products=products)


@main_route.route("/profile", methods=["POST"])
@login_required
def edit_rofile():
    form = EditProfile()
    product = AddProduct()
    data = form.data
    product_data = product.data
    product_data['seller_id'] = current_user.id

    file = product.photo.data

    if not file:
        flash('No selected file', 'upload_error')
        return redirect(url_for('main_route.profile'))
    print(product.data)
    print(file)
    filename = secure_filename(file.filename)
    file.save(os.path.join(upload_folder, f'{product.name.data}_{filename}'))


    data.pop('csrf_token', None)
    data.pop('save', None)
    product_data.pop('csrf_token', None)

    product_data['photo'] = f'../static/img/{product.name.data}_{filename}'

    db.session.query(User).\
       filter(User.login == data['login']).\
       update(data)
    
    new_product = Product(**product_data)
    db.session.add(new_product)

    db.session.commit()

    cols = current_user.__mapper__.attrs.keys()
    return render_template("profile.html", cols=cols, user=current_user,
                                              form=form,
                                              product=product)

@main_route.route('/profile')
@login_required
def profile():
    product = AddProduct()
    form = EditProfile()
    cols = current_user.__mapper__.attrs.keys()
    return render_template('profile.html', user=current_user, cols=cols,
                                           form=form,
                                           product=product)


@main_route.route('/product')
@login_required
def product():
    data = request.args.to_dict()
    id = data['id']
    product = Product.query.filter_by(id=id).first()
    cols = product.__mapper__.attrs.keys()
    return render_template('product.html', product=product, cols=cols)


@main_route.route('/cart', methods=['GET'])
@login_required
def cart():
    cart_products, total = get_cart()
    return render_template('cart.html', cart_products=cart_products, 
                                        total=total)
