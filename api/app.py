from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, render_template
import os
from flask_restful import Resource, Api
from config.db import db
from config.constant import *
from model.tt import *
from resources.admin import AdminApi
from resources.products import ProductsApi
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "https://tt_officiel.com"}})

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)



@app.route('/a')    
def home():
    print('Trouvez Tous Officiel')
    return render_template('index.html')

api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(ProductsApi, '/api/products/<string:route>', endpoint='all_products', methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0")  