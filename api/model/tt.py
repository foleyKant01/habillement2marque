import datetime
import pymysql
from config.db import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression



class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_fullname = db.Column(db.String(128), nullable=False)
    ad_username = db.Column(db.String(128), nullable=False)
    ad_mobile = db.Column(db.String(128), nullable=False)
    ad_address = db.Column(db.String(128), nullable=False)
    ad_email = db.Column(db.String(128), nullable=False)
    ad_password = db.Column(db.String(128), nullable=False)
    ad_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.String(128), nullable=False)
    price_received = db.Column(db.String(128), nullable=False)

    model = db.Column(db.String(128))
    style = db.Column(db.String(128))
    talon_cm = db.Column(db.String(128))
    material = db.Column(db.String(128))
    image_file = db.Column(db.JSON, nullable=False)
    

    pr_uid = db.Column(db.String(128), nullable=False, unique=True, index=True)

    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    variants = db.relationship('ProductVariants', backref='product', cascade="all, delete-orphan")


class ProductVariants(db.Model):
    __tablename__ = 'product_variants'

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.String(128),
        db.ForeignKey('products.pr_uid', ondelete="CASCADE"),
        nullable=False
    )

    color = db.Column(db.String(128), nullable=False)
    pointure = db.Column(db.String(128))
    inventory_level = db.Column(db.String(128), nullable=False)

    creation_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)