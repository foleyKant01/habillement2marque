from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import request, jsonify
import uuid
import requests
from config.db import db
from model.tt import Admin


   
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
        # hashed_password = bcrypt.hashpw(ad_password.encode('utf-8'), bcrypt.gensalt())
        new_admin = Admin()
        new_admin.ad_fullname = ad_fullname
        new_admin.ad_username = ad_username
        new_admin.ad_mobile = ad_mobile
        new_admin.ad_address = ad_address
        new_admin.ad_email = ad_email
        new_admin.ad_password = ad_password
        new_admin.ad_uid = ad_uid
        
        db.session.add(new_admin)
        db.session.commit()
        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'
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

    try:
        data = request.get_json()

        ad_email = data.get('ad_email')
        ad_password = data.get('ad_password')

        # Recherche de l'admin
        login_admin = Admin.query.filter_by(ad_email=ad_email).first()

        if login_admin and login_admin.ad_password == ad_password:
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=ad_email, expires_delta=expires)

            reponse['status'] = 'success'
            reponse['message'] = 'Login successful'
            reponse['access_token'] = access_token
            reponse['admin'] = {
                'ad_uid': login_admin.ad_uid,
                'ad_email': login_admin.ad_email,
                'ad_username': login_admin.ad_username
            }

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid email or password'

    except Exception as e:
        reponse['status'] = 'error'
        reponse['error_description'] = str(e)

    return jsonify(reponse)



def send_lien():

    sites_pub = {
    'Reddit': 'https://oauth.reddit.com/api/submit',
    'Reddits': 'https://www.reddit.com/submit',
    'Facebook': 'https://www.facebook.com/post_api',     
    }

    lien_youtube = 'https://www.youtube.com/@foleykant01'
    print("OKOK")

    envoyer_pub_vers_sites(lien_youtube, sites_pub)

    return True


def envoyer_pub_vers_sites(lien_youtube, sites_pub):
    """
    Envoie un lien publicitaire vers plusieurs sites web via leurs formulaires ou API.
    
    Args:
    - lien_youtube (str): Lien vers votre chaîne YouTube ou vidéo.
    - sites (dict): Un dictionnaire où les clés sont les noms des sites et les valeurs sont les URLs des formulaires ou API.
    
    Returns:
    - dict: Un dictionnaire avec les résultats des requêtes pour chaque site.
    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Python script)',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    resultats = {}
    print("OKOK")
    for site, url in sites_pub.items():
        try:
            data = {
                'message': f"Découvrez ma chaîne YouTube ici: {lien_youtube}"
            }
            
            response = requests.post(url, data=data, headers=headers)
            print(url)
            
            if response.status_code == 200:
                resultats[site] = "Lien envoyé avec succès"
                print("Lien envoyé avec succès")
            else:
                resultats[site] = f"Erreur {response.status_code}"
                print(resultats[site])
        
        except Exception as e:
            resultats[site] = f"Erreur: {str(e)}"
            print(e)
    
    return resultats



def pubs_fb():

    access_token = 'VOTRE_TOKEN_D_ACCESS'

    group_fb = {
        "178525406910683",
        "3744198125865926",
        # "1576497582652492",
        # "1135253890245986",
        # "1057596134329359",
        # "modafrim",
        # "957295754348220",
        # "949293285965041",
        # "femmechicfemmein",
        # "817401145659251",
        # "524179897793231",
        # "503014463122174",
        # "lesdealeursetleskenneursdunet",
        # "484623975441245",
        # "435185080018144",
        # "Ivoirshoppingci",
        # "344057022384574",
        # "298910780304589",
        # "296966586996664",
        # "253137518122885",
        # "243935093191923",
        # "audjassaquoicom",
        # "10GITAL",
        # "178525406910683",
        # "175313929190441",
        # "djassavirtuelofficiel"
    }

    # Contenu du message
    message_data = {
        'message': 'Votre message automatique ici',
        'access_token': access_token
    }

    for group_id in group_fb:
        print(group_id)
        response = requests.post(f'https://graph.facebook.com/{group_id}/feed', data=message_data)
        if response.status_code == 200:
            print("Publication réussie !")
        else:
            print("Erreur :", response.json())

    return True


# Clé secrete = "e7cbbe9100850714115fed5412ed97a9"
# Identifiant = "1573355863575113"



def code():
    try:
        # Obtenez l'adresse IP de l'utilisateur
        response = requests.get('https://ipinfo.io')
        data = response.json()
        print(data)
        country = data.get('country', 'Unknown')  # Récupérez le code pays, par exemple 'FR' pour la France
        return country
    except Exception as e:
        print(f"Erreur lors de la récupération du pays : {e}")
        return 'Unknown'
