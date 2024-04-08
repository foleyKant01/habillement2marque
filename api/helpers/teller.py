from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.tt import Teller
import bcrypt, jwt
from werkzeug.security import check_password_hash

def CreateTeller():
    reponse = {}

    try:
        t_fullname = (request.json.get('fullname'))
        t_username = (request.json.get('username'))
        t_mobile = (request.json.get('mobile'))      
        t_address = (request.json.get('address'))
        t_email = (request.json.get('email'))
        t_password = (request.json.get('password'))
        t_city = (request.json.get('city'))
        t_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(t_password.encode('utf-8'), bcrypt.gensalt())
        
        new_teller = Teller()
        new_teller.t_fullname = t_fullname
        new_teller.t_username = t_username
        new_teller.t_mobile = t_mobile
        new_teller.t_address = t_address
        new_teller.t_email = t_email
        new_teller.t_password = hashed_password
        new_teller.t_city = t_city
        new_teller.t_uid = t_uid
        
        db.session.add(new_teller)
        db.session.commit()

        # nouvel_hotel =(reponse)
        # liste_users.append(nouvel_hotel)

        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
    # except:
    #     reponse['error'] = 'Incorrect data, recheck it'

    return reponse


def LoginTeller():
    reponse = {}
    reponses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_teller = Teller.query.filter_by(t_username=username).first()

        if login_teller and bcrypt.checkpw(password.encode('utf-8'), login_teller.t_password.encode('utf-8')):
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=username)

            reponse['status'] = 'success'
            reponse['message'] = 'Login successful'
            reponse['access_token'] = access_token

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid username or password'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse