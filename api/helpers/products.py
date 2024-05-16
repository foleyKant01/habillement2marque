import csv
import os
from flask import request
from werkzeug.utils import secure_filename
import uuid
from config.db import db
from config.constant import *

from model.tt import Products

UPLOAD_FOLDER = 'static/assets/uploads/'
IMGHOSTNAME = 'http://127.0.0.1:5000/static/assets/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'PATCH' or request.method == 'POST':
        print('is post')
        # Vérifier si la partie de la requête contient le fichier
        if 'image_file' not in request.files:
            return None  # Champ de fichier manquant
        file = request.files['image_file']
        # Si l'utilisateur ne sélectionne pas de fichier, le navigateur envoie un fichier vide sans nom de fichier.
        print(file.filename)
        if file.filename == '':
            return None  # Nom de fichier vide
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Nettoyer le nom de fichier
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return filename
    # return None
    



def CreateProducts():
    
    response = {}

    try:
        name = request.form.get('name')
        type = request.form.get('type')
        description = request.form.get('description')
        price = request.form.get('price')
        image_file = upload_file()  # Appelez directement la fonction sans argument
        print('here', image_file)    
        inventory_level = request.form.get('inventory_level')
        price_received = request.form.get('price_received')
        weight = request.form.get('weight')
        color = request.form.get('color')
        taille1 = request.form.get('taille1')
        taille2 = request.form.get('taille2')
        taille3 = request.form.get('taille3')
        taille4 = request.form.get('taille4')
        # taille5 = request.form.get('taille5')
        pr_uid = generate_product_id(name)

        new_products = Products()
        new_products.name = name
        new_products.type = type
        new_products.description = description
        new_products.price = price
        new_products.image_file = image_file
        new_products.inventory_level = inventory_level
        new_products.price_received = price_received
        new_products.weight = weight
        new_products.color = color
        new_products.taille1 = taille1
        new_products.taille2 = taille2
        new_products.taille3 = taille3
        new_products.taille4 = taille4
        # new_products.taille5 = taille5
        new_products.pr_uid = pr_uid
        
        db.session.add(new_products)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response

def generate_product_id(name):
    # Extraire les trois premières lettres du nom du produit
    prefix = name[:3].upper()
    # Générer un identifiant unique
    unique_id = str(uuid.uuid4().hex)[:6].upper()  # Utilisation des 6 premiers caractères de l'UUID généré
    # Concaténer les trois premières lettres du nom du produit avec l'identifiant unique
    product_id = prefix + unique_id
    return product_id

# # Exemple d'utilisation
# product_name = "T-shirt"
# product_id = generate_product_id(product_name)
# print("Identifiant unique du produit:", product_id)

# ID: comment par 3 premières lettres du nom du produit

def test():
    product_name = "Landry Roland"
    return generate_product_id(product_name)


def UpdateProducts():
    response = {}

    try:

        pr_uid = request.json.get('pr_uid')

        update_products = Products.query.filter_by(pr_uid = pr_uid).first()
        
        if update_products:
            update_products.name = request.json.get('name', update_products.name)
            update_products.description = request.json.get('description', update_products.description)
            update_products.price = request.json.get('price', update_products.price)
            update_products.image = request.json.get('image', update_products.image)
            update_products.taille1 = request.json.get('taille1', update_products.taille1)
            update_products.taille2 = request.json.get('taille2', update_products.taille2)
            update_products.taille3 = request.json.get('taille3', update_products.taille3)
            update_products.taille4 = request.json.get('taille4', update_products.taille4)
     
        db.session.add(update_products)
        db.session.commit() 
        
        response['status'] = 'success'
        response['message'] = "the products has been updated!"

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def DeleteProducts():
    response = {}

    try:
        pr_uid = request.json.get('pr_uid')
        delete_products = Products.query.filter_by(pr_uid=pr_uid).first()

        if delete_products:
            db.session.delete(delete_products)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'Product non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllProducts():
    response = {}
    
    try:
        all_products = Products.query.all()

        products_info = []

        for products  in all_products:
            products_infos = {
                'name': products.name,              
                'price': products.price,  
                'image_file': str(IMGHOSTNAME)+str(products.image_file),              
                'pr_uid': products.pr_uid,          
            }
            products_info.append(products_infos)

        response['status'] = 'success'
        response ['products'] = products_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def ReadSingleProducts():
    response = {}

    try:
        uid = request.json.get('pr_uid')
        single_products = Products.query.filter_by(pr_uid=uid).first()

        products_infos = {
            'pr_uid': single_products.pr_uid,
            'name': single_products.name,  
            'description': single_products.description,              
            'price': single_products.price,              
            'color': single_products.color,              
            'type': single_products.type,              
            'inventory_level': single_products.inventory_level,              
            'image_file': str(IMGHOSTNAME) + str(single_products.image_file),              
            'taille1': single_products.taille1,              
            'taille2': single_products.taille2,              
            'taille3': single_products.taille3,              
            'taille4': single_products.taille4,              
        }
        response['status'] = 'success'
        response['user'] = products_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response 

# IMGHOSTNAME





