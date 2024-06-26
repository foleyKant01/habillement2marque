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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.String(128), nullable=False)
    image_file = db.Column(db.String(255), nullable=False)
    inventory_level = db.Column(db.String(128), nullable=False)
    price_received = db.Column(db.String(128), nullable=False)
    color = db.Column(db.String(128), nullable=True)
    tailleVe = db.Column(db.String(128), nullable=True)
    tailleJe = db.Column(db.String(128), nullable=True)
    taille1 = db.Column(db.String(128), nullable=True)
    taille2 = db.Column(db.String(128), nullable=True)
    taille3 = db.Column(db.String(128), nullable=True)
    taille4 = db.Column(db.String(128), nullable=True)
    pr_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)