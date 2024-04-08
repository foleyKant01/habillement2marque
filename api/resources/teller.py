from flask_restful import Resource
import json
from helpers.teller import *
from flask import request


class TellerApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateTeller()
        if route == "login":
            return LoginTeller()
    
    # def get(self, route):
    #     if route == "readall":
    #         return ReadAllTeller()
    #     if route == "readsingle":
    #         return ReadSingleTeller()
            
    
    # def delete(self, route):
    #      if route == "delete":
    #         return DeleteTeller()
         
    # def patch(self, route):
    #     if route == "update":
    #         return UpdateTeller()
        