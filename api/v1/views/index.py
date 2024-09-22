from models.car_document import Document
from models.car_make import CarMake
from models.car_model import CarModel
from models.category import Category
from models.vehicle import Vehicle
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify

classes ={"Document": Document, "Vehicle": Vehicle, "User": User, "CarMake": CarMake, "CarModel": CarModel, "Category": Category}

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Stats of API """
    obj_stats = {}

    for key, value in classes.items():
        obj_stats[key] = storage.count(value)
    return jsonify(obj_stats)
