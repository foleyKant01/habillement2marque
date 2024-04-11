from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.tt import Admin
import bcrypt, jwt
from werkzeug.security import check_password_hash


# liste_admin = []
   
def CreateAdmin():
    reponse = {}

    try:
        ad_fullname = (request.json.get('fullname'))
        ad_username = (request.json.get('username'))
        ad_mobile = (request.json.get('mobile'))      
        ad_address = (request.json.get('address'))
        ad_email = (request.json.get('email'))
        ad_password = (request.json.get('password'))
        ad_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(ad_password.encode('utf-8'), bcrypt.gensalt())
        
        new_admin = Admin()
        new_admin.ad_fullname = ad_fullname
        new_admin.ad_username = ad_username
        new_admin.ad_mobile = ad_mobile
        new_admin.ad_address = ad_address
        new_admin.ad_email = ad_email
        new_admin.ad_password = hashed_password
        new_admin.ad_uid = ad_uid
        
        db.session.add(new_admin)
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



# def ReadAllUser():
#     reponse = {}

#     try:
#         readAllUser = User.query.all()

#         if readAllUser:
#             user_informations = []

#             for user in readAllUser:
#                 user_infos = {
#                     'ad_uid': user.ad_uid,
#                     'fullname': user.ad_fullname,
#                     'username': user.ad_username,
#                     'mobile': user.ad_mobile,
#                     'address': user.ad_address,
#                     'email': user.ad_email,                    
#                     'city': user.ad_city, 
#                 }

#                 user_informations.append(user_infos)

#             reponse['status'] = 'success'
#             reponse ['users'] = user_informations
#         else:
#             reponse['status'] = 'erreur'
#             reponse['motif'] = 'aucun'

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse

# def ReadSingleUser():
#     reponse = {}

#     try:
#         uid = request.json.get('ad_uid')

#         readSingleUser = User.query.filter_by(ad_uid = uid).first()

#         if readSingleUser:
#             user_infos = {
#                 'ad_uid': readSingleUser.ad_uid,
#                 'fullname': readSingleUser.ad_fullname,
#                 'username': readSingleUser.ad_username,
#                 'mobile': readSingleUser.ad_mobile,
#                 'address': readSingleUser.ad_address,
#                 'email': readSingleUser.ad_email,                    
#                 'city': readSingleUser.ad_city, 
#             }

#             reponse['status'] = 'success'
#             reponse['user'] = user_infos
#         else:
#             reponse['status'] = 'erreur'
#             reponse['motif'] = 'aucun'

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse



# def UpdateUser  ():
#     reponse = {}

#     try:
#         uid = request.json.get('ad_uid')
        
#         updateuser = User.query.filter_by(ad_uid = uid).first()

#         if updateuser:
#             updateuser.ad_fullname = request.json.get('fullname', updateuser.ad_fullname)
#             updateuser.ad_username = request.json.get('username', updateuser.ad_username)            
#             updateuser.ad_mobile = request.json.get('mobile', updateuser.ad_mobile)
#             updateuser.ad_address = request.json.get('address', updateuser.ad_address)
#             updateuser.ad_email = request.json.get('email', updateuser.ad_email)
#             updateuser.ad_password = request.json.get('password', updateuser.ad_password)
#             updateuser.ad_city = request.json.get('city', updateuser.ad_city)

#             db.session.add(updateuser)
#             db.session.commit()

#             reponse['status'] = 'Succes'
#         else:
#             reponse['status'] = 'User not found'

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse


# def DeleteUser():
#     reponse = {}

#     try:
#         uid = request.json.get('ad_uid')

#         deleteuser = User.query.filter_by(ad_uid=uid).first()

#         if deleteuser:
#             db.session.delete(deleteuser)
#             db.session.commit()
#             reponse['status'] = 'success'
#         else:
#             reponse['status'] = 'error'
#             reponse['motif'] = 'utilisateur non trouvé'

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse



def LoginAdmin():
    reponse = {}
    reponses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_admin = Admin.query.filter_by(ad_username=username).first()

        if login_admin and bcrypt.checkpw(password.encode('utf-8'), login_admin.ad_password.encode('utf-8')):
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
