# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

request_blueprint = Blueprint('request_blueprint', __name__)

@request_blueprint.route('/request-management/create', methods=['POST'])
@jwt_required()
def createrequest():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return requestmanagement.setRequest(data)

@request_blueprint.route('/request-management/get/<string:role>/<string:param>', methods=['GET'])
@jwt_required()
def getrequest(role, param):
    if request.method == "GET":
        if role == "driver":
            return requestmanagement.getListRequest(param)

@request_blueprint.route('/request-management/get/detail/<string:id>', methods=['GET'])
@jwt_required()
def getdetails(id):
    if request.method == "GET":
        return requestmanagement.getRequestDetails(id)
    
    
@request_blueprint.route('/request-management/cancel/<string:id>', methods=['GET'])
@jwt_required()
def cancelrequest(id):
    if request.method == "GET":
        return requestmanagement.cancelRequest(id)

@request_blueprint.route('/request-management/approve-driver/<string:id>', methods=['GET'])
@jwt_required()
def approvedriverrequest(id):
    if request.method == "GET":
        return requestmanagement.approveDriverRequest(id)
    
@request_blueprint.route('/request-management/done/<string:id>', methods=['GET'])
@jwt_required()
def donerequest(id):
    if request.method == "GET":
        return requestmanagement.doneRequest(id)

@request_blueprint.route('/request-management/get-status', methods=['GET'])
@jwt_required()
def getStatus():
    if request.method == "GET":
        return wastemanagement.getRequestCategory()
    
@request_blueprint.route("/request-management/get-list/<string:id>", methods=['GET'])
@jwt_required()
def getListReq(id):
    if request.method == "GET":
        return requestmanagement.getUserRequest(id)