from flask_jwt_extended import JWTManager
from flask import Flask, render_template, jsonify
import os
from flask_restful import Resource, Api
from config.db import db
from config.constant import *
from model.tt import *
from resources.admin import AdminApi
from resources.products import ProductsApi
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')  # Assure toi que tes dossiers sont corrects
CORS(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

@app.route('/a')    
def page_a():
    print('FullShop Officiel')
    return render_template('index.html')

# Routes Flask-RESTful
api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_user', methods=['GET','POST', 'DELETE', 'PATCH'])
api.add_resource(ProductsApi, '/api/products/<string:route>', endpoint='all_products', methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
