from dataclasses import dataclass
from datetime import datetime
from flask_login import LoginManager, UserMixin
from sqlalchemy.dialects.postgresql import ARRAY
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

@dataclass
class User(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String(120), nullable=False)
    last_name: str = db.Column(db.String(120), nullable=False)
    login: str = db.Column(db.String(120), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(255), nullable=False)
    is_seller: bool = db.Column(db.Boolean, default=False)
    desription: str = db.Column(db.String(255), default=None)
    gender: str = db.Column(db.String(80))
    payment_type: str = db.Column(db.String(120), default=None)
    total_spending: int = db.Column(db.Integer, default=0)
    cart: list = db.Column(ARRAY(db.String(255)), nullable=True)
    registered_datetime: datetime = db.Column(db.DateTime(timezone=True),
                                              nullable=False)
    last_enter: datetime = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self, first_name, last_name, login, password, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password_hash = self.set_password(password)
        self.gender = gender
        self.registered_datetime = datetime.now()
        self.last_enter = datetime.now()

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        return generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


@dataclass
class Seller(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'),
                                         nullable=False)
    selled_count: int = db.Column(db.Integer, default=0)
    active_products: int = db.Column(db.Integer, default=0)
    total_income: int = db.Column(db.Integer, default=0)
    open_datetime: datetime = db.Column(db.DateTime(timezone=True))

    def __init__(self, user_id):
        self.user_id = user_id
        self.open_datetime = datetime.now()


@dataclass
class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    seller_id: int = db.Column(db.Integer, db.ForeignKey('user.id'),
                                         nullable=False)
    name: str = db.Column(db.String(180), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    type: str = db.Column(db.String(180), nullable=False)
    cost: int = db.Column(db.Integer, nullable=False)
    open_datetime: datetime = db.Column(db.DateTime, nullable=False)
    sold_datetime: datetime = db.Column(db.DateTime, default=None)
    is_sold: bool = db.Column(db.Boolean, default=False)
    photo: str = db.Column(db.String(255), default='./static/img/default-product-image.png',
                           nullable=False)

    def __init__(self, seller_id, name, description, type, cost, photo=None):
        self.seller_id = seller_id
        self.name = name
        self.description = description
        self.type = type
        self.cost = cost
        self.open_datetime = datetime.now()
        if photo:
            self.photo = photo


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
