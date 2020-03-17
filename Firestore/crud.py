# this file provides the actual api endpoints for front-end to hit
from flask import Blueprint, request, jsonify, make_response, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, InternalServerError
from . import cloudFireStore    
import datetime 
crud = Blueprint('crud', __name__)

@crud.route('/create/<type>/<id>', methods = ['PUT'])
def create(type: str, id: str):
    """gets the json object and creates the document from the provided type and id. returns 200 if ok else 500"""
    data = request.get_json
    try: 
        cloudFireStore.create(type, id, data)
        resp = jsonify(success=True)
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/read/<type>/<id>', methods = ['GET'])
def read(type: str, id: str):
    """reads data from db and returns it as a json object else raises 404"""
    if id != "":
        data = cloudFireStore.read(type, id)
    else:
        data = cloudFireStore.readAll(type)
    if data == None:
        raise NotFound("The document you are requesting could not be found in the database")
    resp = make_response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*' # do this for everything 
    return resp 

@crud.route('/update/<type>/<id>', methods = ['POST'])
def update(type:str, id: str):
    """parses a json dict and creates an object in db; returns 200 if ok else 500"""
    data = request.get_json
    try:
        cloudFireStore.update(data, type, id) 
        resp = jsonify(success=True)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        raise InternalServerError("The requested operation could not be performed")

@crud.route('/delete/<type>/<id>', methods = ['GET'])
def delete(type:str, id: str):
    """deletes the given document under collection"""
    cloudFireStore.delete(type, id)
    resp = jsonify(success=True)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp 