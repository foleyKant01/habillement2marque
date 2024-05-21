from flask_restful import Resource
import json
from helpers.products import *
from flask import request


class ProductsApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateProducts()
        
        if route == "readsingle":
            return ReadSingleProducts()
        
        if route == "readsimilar":
            return AllSimilarProducts()
        
        if route == "readsimilartype":
            return AllSimilarTypeProducts()
        
            
    def get(self, route):
        if route == "readall":
            return ReadAllProducts()
        
        if route == "test":
            return test()
        
        
    
    def delete(self, route):
         if route == "delete":
            return DeleteProducts()
         
    def patch(self, route):
        if route == "update":
            return UpdateProducts()
        