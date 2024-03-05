# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

driver_blueprint = Blueprint('driver_blueprint', __name__)

@driver_blueprint.route('/driver-management/get', methods=['GET'])
@jwt_required()
def getUser():
    if request.method == "GET":
        return drivermanagement.driver_list()
    
@driver_blueprint.route('/driver-management/update', methods=['POST'])
@jwt_required()
def editUser():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return drivermanagement.driver_edit(data)

@driver_blueprint.route('/driver-management/get/detail/<string:id>', methods=['GET'])
@jwt_required()
def getUserDetail(id):
    if request.method == "GET":
        return drivermanagement.driver_details(id)

@driver_blueprint.route('/driver-management/delete/<string:id>', methods=['POST'])
@jwt_required()
def deleteUser(id):
    if request.method == "POST":
        return drivermanagement.delete_driver(id)
