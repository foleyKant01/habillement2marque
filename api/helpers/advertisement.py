from flask import request
import uuid
from config.db import db
from model.tt import Advertisement



def CreateAdvertisement():
    
    response = {}

    try:
        ad_name = request.json.get('name')
        ad_email = request.json.get('email')
        ad_description = request.json.get('description')
        ad_mobile = request.json.get('mobile')
        ad_address = request.json.get('address')
        ad_uid = str(uuid.uuid4())

        
        new_advertisement = Advertisement()

        new_advertisement.ad_name = ad_name
        new_advertisement.ad_email = ad_email
        new_advertisement.ad_description = ad_description
        new_advertisement.ad_mobile = ad_mobile
        new_advertisement.ad_address = ad_address
        new_advertisement.ad_uid = ad_uid
        


        
        db.session.add(new_advertisement)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateAdvertisement():
    response = {}

    try:

        update_advertisement = Advertisement.query.filter_by(ad_uid="efa34482-9325-48be-9cac-9875e7fc8991").first()
        
        if update_advertisement:
            update_advertisement.ad_name = request.json.get('name', update_advertisement.ad_name)
            update_advertisement.ad_email = request.json.get('email', update_advertisement.ad_email)
            update_advertisement.ad_description = request.json.get('description', update_advertisement.ad_description)            
            update_advertisement.ad_mobile = request.json.get('mobile', update_advertisement.ad_mobile)
            update_advertisement.ad_address = request.json.get('address', update_advertisement.ad_address)
        

        db.session.add(update_advertisement)
        db.session.commit() 
        
        response['status'] = 'success'
        response['message'] = "the ad has been updated!"



    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeleteAdvertisement():
    response = {}

    try:
        uid = request.json.get('ad_uid')

        deleteAdvertisement = Advertisement.query.filter_by(ad_uid=uid).first()

        if deleteAdvertisement:
            db.session.delete(deleteAdvertisement)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllAdvertisement():
    response = {}
    
    try:
        all_advertisement = Advertisement.query.all()

        advertisement_infos = []

        for advertisement in all_advertisement:
            advertisement_info = {
                'ad_uid': advertisement.ad_uid,
                'name': advertisement.ad_name,              
            }
            advertisement_infos.append(advertisement_info)

        response['status'] = 'success'
        response ['users'] = advertisement_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def ReadSingleAdvertisement():
    response = {}

    try:
        advertisement_uid = request.json.get('ad_uid')


        single_advertisement = Advertisement.query.filter_by(ad_uid=advertisement_uid).first()

        advertisement_info = {
            'ad_uid': single_advertisement.ad_uid,
            'name': single_advertisement.ad_name,
            'email': single_advertisement.ad_email,
            'description': single_advertisement.ad_description,
            'mobile': single_advertisement.ad_mobile,
            'address': single_advertisement.ad_address,                
        }

        response['status'] = 'success'
        response['user'] = advertisement_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

