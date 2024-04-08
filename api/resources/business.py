from flask_restful import Resource
import json
from helpers.business import *
from flask import request


class BusinessApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateBusiness()
    
    def get(self, route):
        if route == "readall":
            return ReadAllBusiness()

        if route == "readsingle":
            return ReadSingleBusiness()
    
    def delete(self, route):
         if route == "delete":
            return DeleteBusiness()
         
    def patch(self, route):
        if route == "update":
            return UpdateBusiness()
        