# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

voucher_blueprint = Blueprint('voucher_blueprint', __name__)

@voucher_blueprint.route('/voucher-management/get', methods=['GET'])
@jwt_required()
def getVoucher():
    if request.method == 'GET':
        return vouchermanagement.getVoucher()

@voucher_blueprint.route('/voucher-management/delete/<string:id>', methods=['POST'])
@jwt_required()
def addVoucher(id):
    if request.method == "POST":
        return vouchermanagement.deleteVoucher(id)
