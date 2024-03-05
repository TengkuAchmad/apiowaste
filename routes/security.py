# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

security_blueprint = Blueprint('security_blueprint', __name__)

@security_blueprint.route('/current_user', methods=['GET'])
@jwt_required()
def current_user():
    current_user = get_jwt_identity()
    return accountmanagement.current_user(current_user)

@security_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True, locations=['json'])
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200 