from flask_login import UserMixin
from datetime import datetime
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # customer, driver, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='pending')
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
