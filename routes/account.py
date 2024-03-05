# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

accounts_blueprint = Blueprint('accounts_blueprint', __name__)

@accounts_blueprint.route('/account-management/auth', methods=['POST'])
def auth():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status':'Missing form-data in request'}), 400
        else:
            data = request.form.to_dict()
            return accountmanagement.auth_account(data)

# REGISTER ACCOUNT ENDPOINT
@accounts_blueprint.route('/account-management/reg/<string:role>', methods=['POST'])
def reg(role):
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status' : 'Missing form-data in request'}), 400
        else:
            data = request.form.to_dict()
            return accountmanagement.reg_account(data, role)
        
# FORGOT PASSWORD ENDPOINT
@accounts_blueprint.route('/account-management/update/password', methods=['POST'])
def updatepass():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status' : 'Missing form-data in request'}), 400
        else:
            data = request.form.to_dict()
            return passwordmanagement.update_pass(data)