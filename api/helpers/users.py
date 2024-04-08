from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.tt import User
import bcrypt, jwt
from werkzeug.security import check_password_hash


# liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        u_fullname = (request.json.get('fullname'))
        u_username = (request.json.get('username'))
        u_mobile = (request.json.get('mobile'))      
        u_address = (request.json.get('address'))
        u_email = (request.json.get('email'))
        u_password = (request.json.get('password'))
        u_city = (request.json.get('city'))
        u_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(u_password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = User()
        new_user.u_fullname = u_fullname
        new_user.u_username = u_username
        new_user.u_mobile = u_mobile
        new_user.u_address = u_address
        new_user.u_email = u_email
        new_user.u_password = hashed_password
        new_user.u_city = u_city
        new_user.u_uid = u_uid
        
        db.session.add(new_user)
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



def ReadAllUser():
    reponse = {}

    try:
        readAllUser = User.query.all()

        if readAllUser:
            user_informations = []

            for user in readAllUser:
                user_infos = {
                    'u_uid': user.u_uid,
                    'fullname': user.u_fullname,
                    'username': user.u_username,
                    'mobile': user.u_mobile,
                    'address': user.u_address,
                    'email': user.u_email,                    
                    'city': user.u_city, 
                }

                user_informations.append(user_infos)

            reponse['status'] = 'success'
            reponse ['users'] = user_informations
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse

def ReadSingleUser():
    reponse = {}

    try:
        uid = request.json.get('u_uid')

        readSingleUser = User.query.filter_by(u_uid = uid).first()

        if readSingleUser:
            user_infos = {
                'u_uid': readSingleUser.u_uid,
                'fullname': readSingleUser.u_fullname,
                'username': readSingleUser.u_username,
                'mobile': readSingleUser.u_mobile,
                'address': readSingleUser.u_address,
                'email': readSingleUser.u_email,                    
                'city': readSingleUser.u_city, 
            }

            reponse['status'] = 'success'
            reponse['user'] = user_infos
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def UpdateUser  ():
    reponse = {}

    try:
        uid = request.json.get('u_uid')
        
        updateuser = User.query.filter_by(u_uid = uid).first()

        if updateuser:
            updateuser.u_fullname = request.json.get('fullname', updateuser.u_fullname)
            updateuser.u_username = request.json.get('username', updateuser.u_username)            
            updateuser.u_mobile = request.json.get('mobile', updateuser.u_mobile)
            updateuser.u_address = request.json.get('address', updateuser.u_address)
            updateuser.u_email = request.json.get('email', updateuser.u_email)
            updateuser.u_password = request.json.get('password', updateuser.u_password)
            updateuser.u_city = request.json.get('city', updateuser.u_city)

            db.session.add(updateuser)
            db.session.commit()

            reponse['status'] = 'Succes'
        else:
            reponse['status'] = 'User not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteUser():
    reponse = {}

    try:
        uid = request.json.get('u_uid')

        deleteuser = User.query.filter_by(u_uid=uid).first()

        if deleteuser:
            db.session.delete(deleteuser)
            db.session.commit()
            reponse['status'] = 'success'
        else:
            reponse['status'] = 'error'
            reponse['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def LoginUser():
    reponse = {}
    reponses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_user = User.query.filter_by(u_username=username).first()

        if login_user and bcrypt.checkpw(password.encode('utf-8'), login_user.u_password.encode('utf-8')):
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
