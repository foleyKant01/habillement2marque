from flask_restful import Resource
import json
from helpers.users import *
from flask import request


class UsersApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateUser()
        if route == "login":
            return LoginUser()
    
    def get(self, route):
        if route == "readall":
            return ReadAllUser()
        if route == "readsingle":
            return ReadSingleUser()
            
    
    def delete(self, route):
         if route == "delete":
            return DeleteUser()
         
    def patch(self, route):
        if route == "update":
            return UpdateUser()
        