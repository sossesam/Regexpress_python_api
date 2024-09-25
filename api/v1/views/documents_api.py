#!/usr/bin/python3
from models.category import Category
from models.car_document import Document
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/documents/<document_id>', methods=['GET'], strict_slashes=False)
def get_documents(document_id):
    """
    Retrieves the list of all document objects
    """
    document = storage.get(Document, document_id)
    if not document:
        abort(404)
    return make_response(jsonify(document.to_dict()), 200)


@app_views.route('/categories/<category_id>/documents', methods=['GET'], strict_slashes=False)
def get_category_documents(category_id):
    """
    Retrieves the list of all document objects
    """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    all_document = storage.all(Document)
    list_document = []
    for document in all_document.values():
        if document.category_id == category_id:
            list_document.append(document.to_dict())
    return make_response(jsonify(list_document), 200)


@app_views.route('/documents/<document_id>', methods=['DELETE', 'GET'], strict_slashes=False)

def delete_city(document_id):
    """
    Deletes a city based on id provided
    """
    document = storage.get(Document, document_id)

    if not document:
        abort(404)
    storage.delete(document)
    storage.save()

    return make_response(jsonify({}), 200)



@app_views.route('/categories/<category_id>/documents', methods=['POST'],
                 strict_slashes=False)

def create_document(category_id):
    """
    Creates a Document
    """
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Document(**data)
    instance.category_id= category.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/documents/<document_id>', methods=['PUT'], strict_slashes=False)
def update_document(document_id):
    """
    Updates a City
    """
    document = storage.get(Document, document_id)
    if not document:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(document, key, value)
    storage.save()
    return make_response(jsonify(document.to_dict()), 200)