# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

sedekah_blueprint = Blueprint('sedekah_blueprint', __name__)

@sedekah_blueprint.route('/sedekah-management/get', methods=['GET'])
@jwt_required()
def getSedekah():
    if request.method == "GET":
        return sedekahmanagement.getSedekah()
    
@sedekah_blueprint.route('/sedekah-management/update', methods=['POST'])
@jwt_required()
def updateSedekah():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return sedekahmanagement.updateSedekah(data)