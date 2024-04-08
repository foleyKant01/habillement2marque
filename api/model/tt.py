import datetime
import pymysql
from config.db import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_fullname = db.Column(db.String(128), nullable=False)
    u_username = db.Column(db.String(128), nullable=False)
    u_mobile = db.Column(db.String(128), nullable=False)
    u_address = db.Column(db.String(128), nullable=False)
    u_email = db.Column(db.String(128), nullable=False)
    u_password = db.Column(db.String(128), nullable=False)
    u_city = db.Column(db.String(128), nullable=False)
    u_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class Teller(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_fullname = db.Column(db.String(128), nullable=False)
    t_username = db.Column(db.String(128), nullable=False)
    t_mobile = db.Column(db.String(128), nullable=False)
    t_address = db.Column(db.String(128), nullable=False)
    t_email = db.Column(db.String(128), nullable=False)
    t_password = db.Column(db.String(128), nullable=False)
    t_city = db.Column(db.String(128), nullable=False)
    t_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_name = db.Column(db.String(128), nullable=False)
    ad_email = db.Column(db.String(128), nullable=False)
    ad_description = db.Column(db.String(128), nullable=False)
    ad_mobile = db.Column(db.String(128), nullable=False)
    ad_address = db.Column(db.String(128), nullable=False)
    ad_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bu_title = db.Column(db.String(128), nullable=False)
    bu_name = db.Column(db.String(128), nullable=False)
    bu_email = db.Column(db.String(128), nullable=False)
    bu_categories = db.Column(db.String(128), nullable=False)
    bu_description = db.Column(db.String(128), nullable=False)
    bu_mobile = db.Column(db.String(128), nullable=False)
    bu_address = db.Column(db.String(128), nullable=False)
    bu_city = db.Column(db.String(128), nullable=False)
    bu_pic1 = db.Column(db.String(128), nullable=False)
    bu_pic2 = db.Column(db.String(128), nullable=False)
    bu_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ca_name = db.Column(db.String(128), nullable=False)
    ca_description = db.Column(db.String(250), nullable=False)
    ca_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
