#!/usr/bin/python3
from models.category import Category
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """
    Retrieves the list of all categories objects
    """
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return jsonify(list_categories)


@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category_id(category_id):
    """
    Retrieves the list of all categories objects
    """
    category = storage.get(Category, category_id)
    
    if not category:
        return abort(404, description="CAtegory not found")
    else:
        return jsonify(category.to_dict())


@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category_id(category_id):
    """
    Retrieves the list of all categories objects
    """
    category = storage.get(Category, category_id)
    
    if not category:
        return abort(404, description="CAtegory not found")
    else:
        storage.delete(category)
        return make_response(jsonify({}), 200)
    
@app_views.route('/categories', methods=['POST', 'GET'], strict_slashes=False)
def create_categories():
    """
    Creates a Category
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    
    data = request.get_json()
    instance = Category(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)

def update_category(category_id):
    """
    Updates a State
    """
    instance = storage.get(Category, category_id)

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