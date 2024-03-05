# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

iplpal_blueprint = Blueprint('iplpal_blueprint', __name__)

@iplpal_blueprint.route('/iplpal-management/get', methods=['GET'])
@jwt_required()
def getIPLPAL():
    if request.method == "GET":
        return iplpalmanagement.getIPLPAL()
    
@iplpal_blueprint.route('/iplpal-management/update', methods=['POST'])
@jwt_required()
def updateIPLPAL():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return iplpalmanagement.updateIPLPAL(data)