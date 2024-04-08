from flask import request
import uuid
from config.db import db
from model.tt import Business




def CreateBusiness():
    
    response = {}   

    try:
        bu_title = request.json.get('title')
        bu_name = request.json.get('name')
        bu_email = request.json.get('email')
        bu_categories = request.json.get('categories')
        bu_description = request.json.get('description')
        bu_mobile = request.json.get('mobile')
        bu_address = request.json.get('address')
        bu_city = request.json.get('city')
        bu_pic1 = request.json.get('pic1')
        bu_pic2 = request.json.get('pic2')
        bu_uid = str(uuid.uuid4())

        new_business = Business()
        new_business.bu_title = bu_title
        new_business.bu_name = bu_name
        new_business.bu_email = bu_email
        new_business.bu_categories = bu_categories
        new_business.bu_description = bu_description
        new_business.bu_mobile = bu_mobile
        new_business.bu_address = bu_address
        new_business.bu_city = bu_city
        new_business.bu_pic1 = bu_pic1
        new_business.bu_pic2 = bu_pic2
        new_business.bu_uid = bu_uid
        
        db.session.add(new_business)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateBusiness():
    response = {}

    try:
        update_business = Business.query.filter_by(bu_uid="efa34482-9325-48be-9cac-9875e7fc8991").first()
        
        if update_business:
            update_business.bu_title = request.json.get('title', update_business.bu_title)
            update_business.bu_name = request.json.get('name', update_business.bu_name)
            update_business.bu_email = request.json.get('email', update_business.bu_email)
            update_business.bu_categories = request.json.get('categories', update_business.bu_categories)
            update_business.bu_description = request.json.get('description', update_business.bu_description)            
            update_business.bu_mobile = request.json.get('mobile', update_business.bu_mobile)
            update_business.bu_address = request.json.get('address', update_business.bu_address)
            update_business.bu_city = request.json.get('address', update_business.bu_city)
            update_business.bu_pic1 = request.json.get('address', update_business.bu_pic1)
            update_business.bu_pic2 = request.json.get('address', update_business.bu_pic2)
        

        db.session.add(update_business)
        db.session.commit() 
        
        response['status'] = 'success'
        response['message'] = "the business has been updated!"



    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeleteBusiness():
    response = {}

    try:
        uid = request.json.get('bu_uid')

        deletebusiness = Business.query.filter_by(bu_uid=uid).first()

        if deletebusiness:
            db.session.delete(deletebusiness)
            db.session.commit()

            response['status'] = 'success'

        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllBusiness():
    response = {}
    
    try:
        all_business = Business.query.all()

        business_infos = []

        for advertisement in all_business:
            business_info = {
                'bu_uid': advertisement.bu_uid,
                'name': advertisement.bu_name,              
            }
            business_infos.append(business_info)

        response['status'] = 'success'
        response ['busi'] = business_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def ReadSingleBusiness():
    response = {}

    try:
        business_uid = request.json.get('bu_uid')


        single_business = Business.query.filter_by(bu_uid=business_uid).first()

        business_info = {
            'bu_uid': single_business.bu_uid,
            'name': single_business.bu_name,
            'email': single_business.bu_email,
            'categories': single_business.bu_categories,
            'description': single_business.bu_description,
            'mobile': single_business.bu_mobile,
            'address': single_business.bu_address,                
        }

        response['status'] = 'success'
        response['user'] = business_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response
