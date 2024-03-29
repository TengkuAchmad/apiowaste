# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

transaction_blueprint = Blueprint('transaction_blueprint', __name__)

@transaction_blueprint.route('/transaction-management/get/<string:id>', methods=['GET'])
@jwt_required()
def getBalance(id):
    if request.method == "GET":
        return transactionmanagement.getBalance(id)

@transaction_blueprint.route('/transaction-management/balance/add', methods=['POST'])
@jwt_required()
def addBalance():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return transactionmanagement.addBalance(data)

@transaction_blueprint.route('/transaction-management/buy/voucher', methods=['POST'])
@jwt_required()
def buyVoucher():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return transactionmanagement.buyVoucher(data)

@transaction_blueprint.route('/transaction-management/buy/iplpal', methods=['POST'])
@jwt_required()
def buyIPLPAL():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return transactionmanagement.buyIPLPAL(data)

@transaction_blueprint.route('/transaction-management/buy/sedekah', methods=['POST'])
@jwt_required()
def buySedekah():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            return transactionmanagement.buySedekah(data)