# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/user-management/get', methods=['GET'])
@cross_origin()
def getUser():
    if request.method == "GET":
        return usermanagement.user_list()
    
@user_blueprint.route('/user-management/update', methods=['POST'])
@cross_origin()
def editUser():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return usermanagement.user_edit(data)

@user_blueprint.route('/user-management/get/detail/<string:id>', methods=['GET'])
@cross_origin()
def getUserDetail(id):
    if request.method == "GET":
        return usermanagement.user_details(id)

@user_blueprint.route('/user-management/delete/<string:id>', methods=['POST'])
@cross_origin()
def deleteUser(id):
    if request.method == "POST":
        return usermanagement.delete_user(id)

@user_blueprint.route('/user-management/create', methods=['POST'])
@cross_origin()
def setUser():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return accountmanagement.reg_account(data, role="user")