# this file provides the actual api endpoints for front-end to hit

from flask import Blueprint, request, jsonify, make_response, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, InternalServerError
import cloudFireStore
import datetime 

crud = Blueprint('crud', __name__)

@crud.route('/create/<type>/<id>', methods = ['PUT'])
def create(type: str, id: str):
    """gets the json object and creates the document from the provided type and id. returns 200 if ok else 500"""
    data = request.get_json
    try: 
        result = cloudFireStore.create(type, id, data)
        resp = jsonify(success=True)
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/read/<type>/<id>', methods = ['GET'])
def read(type: str, id: str):
    """reads data from db and returns it as a json object else raises 404"""
    data = cloudFireStore.read(type, id)
    if data == None:
        raise NotFound("The document you are requesting could not be found in the database")
    return jsonify(data.to_dict())

@crud.route('/update/<type>/<id>', methods = ['PUT'])
def update(type:str, id: str):
    """parses a json dict and creates an object in db; returns 200 if ok else 500"""
    data = request.get_json
    x = getattr(cloudFireStore, type) # x is the constructor for the class 
    try:
        result = cloudFireStore.update(data, type, id) 
        resp = jsonify(success=True)
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/delete/<type>/<id>', methods = ['GET'])
def delete(type:str, id: str):
    cloudFireStore.delete(type, id)
    return jsonify(success=True)
