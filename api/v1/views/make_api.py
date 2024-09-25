#!/usr/bin/python3
from models.car_make import CarMake
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/makes', methods=['GET'], strict_slashes=False)
def get_make():
    """
    Retrieves the list of all categories objects
    """
    all_makes = storage.all(CarMake).values()
    list_makes = []
    for make in all_makes:
        list_makes.append(make.to_dict())
    return jsonify(list_makes)

@app_views.route('/makes/<make_id>', methods=['GET'], strict_slashes=False)
def get_make_id(make_id):
    """
    Retrieves the list of all categories objects
    """
    make = storage.get(CarMake, make_id)
    
    if not make:
        return abort(404, description="Make not found")
    else:
        return jsonify(make.to_dict())
    
@app_views.route('/makes', methods=['POST', 'GET'], strict_slashes=False)
def create_make():
    """
    Creates a make
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    
    data = request.get_json()
    instance = CarMake(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/makes/<make_id>', methods=['PUT'], strict_slashes=False)

def update_make(make_id):
    """
    Updates a Make
    """
    instance = storage.get(CarMake, make_id)

    if not instance:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(instance, key, value)
    storage.save()
    return make_response(jsonify(instance.to_dict()), 200)

@app_views.route('/makes/<make_id>', methods=['DELETE'], strict_slashes=False)
def delete_make_id(make_id):
    """
    Retrieves the list of all categories objects
    """
    make = storage.get(CarMake, make_id)
    
    if not make:
        return abort(404, description="CAtegory not found")
    else:
        storage.delete(make)
        return make_response(jsonify({}), 200)