from flask_restful import Resource
import json
from helpers.products import *
from helpers.transformater import *
from flask import request


class ProductsApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateProducts()
        
        if route == "readsingle":
            return ReadSingleProducts() 
        
        if route == "readsimilar":
            return AllSimilarProducts()
        
        if route == "readsimilarcolor":
            return AllSimilarColorProducts()
        
        if route == "readsimilartype":
            return AllSimilarTypeProducts()
        
        if route == "delete":
                return DeleteProducts()
            
        if route == "update":
            return UpdateProducts()
        
        if route == "transformater":
            return transformater()
        
            
    def get(self, route):
        if route == "readall":
            return ReadAllProducts()
        
        if route == "test":
            return test()