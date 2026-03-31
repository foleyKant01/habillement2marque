import json
import os
from flask import jsonify, request
import uuid
from config.db import db
from config.constant import *
from sqlalchemy import case, func

import re
from werkzeug.utils import secure_filename

from model.tt import *

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



# def CreateProducts():
#     response = {}
#     try:
#         name = request.form.get('name').strip()
#         type = request.form.get('type')
#         description = request.form.get('description')
#         price = request.form.get('price')
#         image_file = request.files.getlist('image_file')
#         print('here', image_file)  
#         image_paths = []
#         image_urls = upload_to_s3(image_file)  # ⚡ renommer pour plus de clarté
#         print('here', image_urls)    
#         inventory_level = request.form.get('inventory_level')
#         price_received = request.form.get('price_received')
#         color = request.form.get('color')
#         model = request.form.get('model')
#         style = request.form.get('style')
#         pointure = request.form.get('pointure')
#         material = request.form.get('material')
#         pr_uid = generate_product_id(name)

#         new_products = Products()
#         new_products.name = name
#         new_products.type = type
#         new_products.description = description
#         new_products.price = price
#         new_products.image_file = json.dumps(image_urls)        
#         new_products.inventory_level = inventory_level
#         new_products.price_received = price_received
#         new_products.color = color
#         new_products.model = model
#         new_products.style = style
#         new_products.pointure = pointure
#         new_products.material = material
#         new_products.pr_uid = pr_uid
#         db.session.add(new_products)
#         db.session.commit()

#         response['satus'] = 'success'

#     except Exception as e:
#         response['error_description'] = str(e)
#         response['status'] = 'error'

#     return response


def CreateProducts():
    response = {}

    try:
        name = request.form.get('name').strip()
        type = request.form.get('type')
        description = request.form.get('description')
        price = request.form.get('price')
        price_received = request.form.get('price_received')
        model = request.form.get('model')
        talon_cm = request.form.get('talon_cm')
        style = request.form.get('style')
        material = request.form.get('material') 

        pr_uid = generate_product_id(name)
        image_files = request.files.getlist('image_file')
        image_urls = upload_to_s3(image_files)  # retourne liste
        new_product = Products(
            name=name,
            type=type,
            description=description,
            price=price,
            price_received=price_received,
            material=material,
            model=model,
            image_file=image_urls,
            talon_cm=talon_cm,
            style=style,
            pr_uid=pr_uid
        )
        db.session.add(new_product)
        db.session.commit()  # ⚠️ important pour avoir product_id
        variants_data = request.form.get('variants')
        if variants_data:
            variants = json.loads(variants_data)
            for variant in variants:
                color = variant.get('color')
                pointures = variant.get('pointures', [])
                for size in pointures:
                    pointure = size.get('size')
                    stock = size.get('stock')
                    new_variant = ProductVariants(
                        product_id=new_product.pr_uid,
                        color=color,
                        pointure=pointure,
                        inventory_level=stock,
                    )
                    db.session.add(new_variant)
        db.session.commit()

        response['status'] = 'success'
        response['message'] = 'Produit créé avec variantes'

    except Exception as e:
        db.session.rollback()
        response['status'] = 'error'
        response['error_description'] = str(e)

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
            update_products.image_file = request.form.get('image_file', upload_to_s3())
            update_products.inventory_level = request.form.get('inventory_level', update_products.inventory_level)
            update_products.price_received = request.form.get('price_received', update_products.price_received)
            update_products.color = request.form.get('color', update_products.color)
            update_products.model = request.form.get('model', update_products.model)
            update_products.style = request.form.get('style', update_products.style)
            update_products.pointure = request.form.get('pointure', update_products.pointure)
            update_products.material = request.form.get('material', update_products.material)
     
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

        for product in all_products:

            variants_dict = {}

            for variant in product.variants:
                color = variant.color

                if color not in variants_dict:
                    variants_dict[color] = {
                        "color": color,
                        "pointures": []
                    }

                variants_dict[color]["pointures"].append({
                    "size": variant.pointure,
                    "stock": variant.inventory_level
                })

            products_info.append({
                'pr_uid': product.pr_uid,
                'name': product.name,
                'type': product.type,
                'description': product.description,
                'price': product.price,
                'price_received': product.price_received,
                'model': product.model,
                'image_file': product.image_file,
                'style': product.style,
                'talon_cm': product.talon_cm,
                'material': product.material,

                # 🔥 structure propre frontend
                'variants': list(variants_dict.values()),

                'creation_date': str(product.creation_date),
                'update_date': str(product.update_date),
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

        product = Products.query.filter_by(pr_uid=uid).first()

        if not product:
            return {
                "status": "error",
                "error_description": "Produit non trouvé"
            }

        variants_dict = {}

        for variant in product.variants:
            color = variant.color

            if color not in variants_dict:
                variants_dict[color] = {
                    "color": color,
                    "pointures": []
                }

            variants_dict[color]["pointures"].append({
                "size": variant.pointure,
                "stock": variant.inventory_level
            })

        products_infos = {
            'pr_uid': product.pr_uid,
            'name': product.name,
            'type': product.type,
            'description': product.description,
            'price': product.price,
            'price_received': product.price_received,
            'model': product.model,
            'image_file': product.image_file,
            'style': product.style,
            'talon_cm': product.talon_cm,
            'material': product.material,

            # ✅ variantes propres
            'variants': list(variants_dict.values()),

            'creation_date': str(product.creation_date),
            'update_date': str(product.update_date),
        }

        response['status'] = 'success'
        response['product'] = products_infos  # ✅ renommé (pas "user")

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
                Products.pr_uid != uid,  # exclut le produit actuel
                Products.name == product_name
            )
            .all()
        )

        products_info = []

        for product in all_products:
            variants_dict = {}

            for variant in product.variants:
                color = variant.color

                if color not in variants_dict:
                    variants_dict[color] = {
                        "color": color,
                        "pointures": []
                    }

                variants_dict[color]["pointures"].append({
                    "size": variant.pointure,
                    "stock": variant.inventory_level
                })

            products_info.append({
                'pr_uid': product.pr_uid,
                'name': product.name,
                'type': product.type,
                'price': product.price,
                'price_received': product.price_received,
                'model': product.model,
                'image_file': product.image_file,
                'style': product.style,
                'talon_cm': product.talon_cm,
                'material': product.material,

                # 🔥 variantes groupées
                'variants': list(variants_dict.values()),

                'creation_date': str(product.creation_date),
                'update_date': str(product.update_date),
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

        # 🔹 Subquery : dernier produit par nom (hors produit actuel et même type)
        subquery = (
            db.session.query(
                Products.name,
                func.max(Products.id).label("max_id")
            )
            .filter(
                Products.pr_uid != uid,
                Products.type == product_type,
                Products.name != product_name
            )
            .group_by(Products.name)
            .subquery()
        )

        # 🔹 Join avec Products
        all_products = (
            Products.query
            .join(subquery, Products.id == subquery.c.max_id)
            .all()
        )

        products_info = []

        for product in all_products:
            # 🔹 grouper les variantes par couleur
            variants_dict = {}
            for variant in product.variants:
                color = variant.color

                if color not in variants_dict:
                    variants_dict[color] = {
                        "color": color,
                        "pointures": []
                    }

                variants_dict[color]["pointures"].append({
                    "size": variant.pointure,
                    "stock": variant.inventory_level
                })

            products_info.append({
                'pr_uid': product.pr_uid,
                'name': product.name,
                'type': product.type,
                'description': product.description,
                'price': product.price,
                'price_received': product.price_received,
                'model': product.model,
                'image_file': product.image_file,
                'style': product.style,
                'talon_cm': product.talon_cm,
                'material': product.material,

                # 🔥 variantes groupées
                'variants': list(variants_dict.values()),

                'creation_date': str(product.creation_date),
                'update_date': str(product.update_date),
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
        'type': product.type,
        'description': product.description,  # ✅ pas de json.loads si JSON
        'price': product.price,
        'image_file': product.image_file,
        'inventory_level': product.inventory_level,
        'price_received': product.price_received,
        'pointure': product.pointure,
        'color': product.color,
        'model': product.model,
        'style': product.style,
        'material': product.material,
        'pr_uid': product.pr_uid,
        'creation_date': str(product.creation_date),          
    }
    

def AllSimilarTypeProducts():
    response = {}
    try:
        product_type = request.json.get('type')
        all_products = Products.query.filter_by(type=product_type).all()
        products_info = []

        for product in all_products:
            # 🔹 Grouper les variantes par couleur
            variants_dict = {}
            for variant in product.variants:
                color = variant.color

                if color not in variants_dict:
                    variants_dict[color] = {
                        "color": color,
                        "pointures": []
                    }

                variants_dict[color]["pointures"].append({
                    "size": variant.pointure,
                    "stock": variant.inventory_level
                })

            products_info.append({
                'pr_uid': product.pr_uid,
                'name': product.name,
                'type': product.type,
                'description': product.description,
                'price': product.price,
                'price_received': product.price_received,
                'model': product.model,
                'image_file': product.image_file,
                'style': product.style,
                'talon_cm': product.talon_cm,
                'material': product.material,

                # 🔥 Variantes groupées
                'variants': list(variants_dict.values()),

                'creation_date': str(product.creation_date),
                'update_date': str(product.update_date),
            })

        response['status'] = 'success'
        response['products'] = products_info

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)

    return jsonify(response)