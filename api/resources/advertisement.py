from flask_restful import Resource, Api
import json
from helpers.advertisement import *
from flask import request


class AdvertisementApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateAdvertisement()
    
    def get(self, route):
        if route == "readall":
            return ReadAllAdvertisement()

        if route == "readsingle":
            return ReadSingleAdvertisement()
    
    def delete(self, route):
         if route == "delete":
            return DeleteAdvertisement()
         
    def patch(self, route):
        if route == "update":
            return UpdateAdvertisement()
        