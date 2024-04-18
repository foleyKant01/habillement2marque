from flask import request
import uuid
from config.db import db

from model.tt import Products



def CreateProducts():
    
    response = {}

    try:
        name = request.json.get('name')
        description = request.json.get('description')
        price = request.json.get('price')
        image = request.json.get('image')
        taille1 = request.json.get('taille1')
        taille2 = request.json.get('taille2')
        taille3 = request.json.get('taille3')
        taille4 = request.json.get('taille4')
        pr_uid = str(uuid.uuid4())

        new_products = Products()
        new_products.name = name
        new_products.description = description
        new_products.price = price
        new_products.image = image
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
            'image': single_products.image,              
            'taille1': single_products.taille1,              
            'taille2': single_products.taille2,              
            'taille3': single_products.taille3,              
            'taille4': single_products.description,              
        }
        response['status'] = 'success'
        response['user'] = products_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

