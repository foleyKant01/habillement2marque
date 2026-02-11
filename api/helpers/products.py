import os
from flask import jsonify, request
import uuid
from config.db import db
from config.constant import *
from sqlalchemy import case, func

import re
from werkzeug.utils import secure_filename

from model.tt import Products



# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def upload_file():
#     if request.method == 'PATCH' or request.method == 'POST':
#         print('is post')
#         if 'image_file' not in request.files:
#             return None  # Champ de fichier manquant
#         file = request.files['image_file']
#         print(file.filename)
#         if file.filename == '':
#             return None  # Nom de fichier vide
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)  # Nettoyer le nom de fichier
#             file.save(os.path.join(UPLOAD_FOLDER, filename))
#             return filename
        
        


def upload_to_s3(files):
    urls = []

    for file in files:
        print('file', file)    
        
        # 🔹 nom original
        original_name = file.filename
        print('original_name', original_name)    

        # 🔹 sécuriser le nom (supprime caractères dangereux)
        clean_name = secure_filename(original_name)
        print('clean_name', clean_name)    

        # 🔹 remplacer TOUS les espaces par +
        clean_name = re.sub(r"\s+", "+", clean_name)
        print('clean_name', clean_name)    

        filename = f"{uuid.uuid4().hex}_{clean_name}"

        S3_CLIENT.upload_fileobj(
            file,
            BUCKET_NAME,
            filename,
            ExtraArgs={"ACL": "public-read"}
        )

        url = URL + filename
        urls.append(url)

    return urls




def CreateProducts():
    response = {}
    try:
        name = request.form.get('name')
        type = request.form.get('type')
        description = request.form.get('description')
        price = request.form.get('price')
        image_file = request.files.getlist('image_file')
        print('here', image_file)    
        image_urls = upload_to_s3(image_file)  # ⚡ renommer pour plus de clarté
        print('here', image_urls)    
        inventory_level = request.form.get('inventory_level')
        price_received = request.form.get('price_received')
        color = request.form.get('color')
        tailleVe = request.form.get('tailleVe')
        tailleJe = request.form.get('tailleJe')
        taille1 = request.form.get('taille1')
        taille2 = request.form.get('taille2')
        taille3 = request.form.get('taille3')
        taille4 = request.form.get('taille4')
        pr_uid = generate_product_id(name)

        new_products = Products()
        new_products.name = name
        new_products.type = type
        new_products.description = description
        new_products.price = price
        new_products.image_file = image_urls
        new_products.inventory_level = inventory_level
        new_products.price_received = price_received
        new_products.color = color
        new_products.tailleVe = tailleVe
        new_products.tailleJe = tailleJe
        new_products.taille1 = taille1
        new_products.taille2 = taille2
        new_products.taille3 = taille3
        new_products.taille4 = taille4
        new_products.pr_uid = pr_uid
        db.session.add(new_products)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def generate_product_id(name):
    prefix = name[:3].upper()
    unique_id = str(uuid.uuid4().hex)[:6].upper()  # Utilisation des 6 premiers caractères de l'UUID généré
    product_id = prefix + unique_id
    return product_id


def test():
    product_name = "Landry Roland"
    return generate_product_id(product_name)


def UpdateProducts():
    response = {}

    try:

        pr_uid = request.json.get('pr_uid')

        update_products = Products.query.filter_by(pr_uid = pr_uid).first()
        
        if update_products:
            update_products.name = request.form.get('name', update_products.name)
            update_products.type = request.form.get('type', update_products.type)
            update_products.description = request.form.get('description', update_products.description)
            update_products.price = request.form.get('price', update_products.price)
            update_products.image_file = request.form.get('image_file', upload_file())
            update_products.inventory_level = request.form.get('inventory_level', update_products.inventory_level)
            update_products.price_received = request.form.get('price_received', update_products.price_received)
            update_products.color = request.form.get('color', update_products.color)
            update_products.tailleVe = request.form.get('tailleVe', update_products.tailleVe)
            update_products.tailleJe = request.form.get('tailleJe', update_products.tailleJe)
            update_products.taille1 = request.form.get('taille1', update_products.taille1)
            update_products.taille2 = request.form.get('taille2', update_products.taille2)
            update_products.taille3 = request.form.get('taille3', update_products.taille3)
            update_products.taille4 = request.form.get('taille4', update_products.taille4) 
     
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
        subquery = (
            db.session.query(
                Products.name,
                func.max(Products.id).label("max_id")
            )
            .group_by(Products.name)
            .subquery()
        )

        all_products = (
            Products.query
            .join(subquery, Products.id == subquery.c.max_id)
            .all()
        )

        products_info = []

        for product in all_products:
            products_info.append({
                'name': product.name,
                'price': product.price,
                'image_file': product.image_file,
                'pr_uid': product.pr_uid,
                'type': product.type,
            })

        response['status'] = 'success'
        response['products'] = products_info

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
            'type': single_products.type,  
            'description': single_products.description,              
            'price': single_products.price,              
            'image_file': single_products.image_file,              
            'inventory_level': single_products.inventory_level,              
            'price_received': single_products.price_received,              
            'color': single_products.color,              
            'tailleVe': single_products.tailleVe,              
            'tailleJe': single_products.tailleJe,              
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



def AllSimilarColorProducts():
    response = {}
    try:
        uid = request.json.get('pr_uid')
        product_name = request.json.get('name')

        all_products = (
            Products.query
            .filter(
                Products.pr_uid != uid,
                Products.name == product_name
            )
            .all()
        )

        products_info = []
        for product in all_products:
            products_info.append({
                'name': product.name,
                'price': product.price,
                'image_file': product.image_file,
                'pr_uid': product.pr_uid,
                'type': product.type,
            })

        response['status'] = 'success'
        response['products_color'] = products_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def AllSimilarProducts():
    response = {}
    try:
        product_type = request.json.get('type')
        uid = request.json.get('pr_uid')
        product_name = request.json.get('name')

        all_products = (
            Products.query
            .filter(
                Products.pr_uid != uid,
                Products.type == product_type,
                Products.name != product_name
            )
            .group_by(Products.name)  # empêche les doublons de nom
            .all()
        )

        products_info = []
        for product in all_products:
            products_info.append({
                'name': product.name,
                'price': product.price,
                'image_file': product.image_file,
                'pr_uid': product.pr_uid,
                'type': product.type,
            })

        response['status'] = 'success'
        response['products'] = products_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response





def serialize_product(product):
    return {
        'name': product.name,              
        'price': product.price,  
        'image_file': product.image_file,              
        'pr_uid': product.pr_uid,          
        'type': product.type,          
    }

def AllSimilarTypeProducts():
    response = {}
    product_list = []
    
    try:
        product_type = request.json.get('type')
        all_products = Products.query.filter_by(type=product_type).all()
        
        for product in all_products:
            product_data = serialize_product(product)
            product_list.append(product_data)
        
        response['products'] = product_list
        response['status'] = 'success'
        
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
    
    return jsonify(response)