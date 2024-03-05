# LIBRARY IMPORT
from flask import Blueprint
from utility.utils import *

files_blueprint = Blueprint('files_blueprint', __name__)

@files_blueprint.route('/file-management/get/<string:id>', methods=['GET'])
@jwt_required()
def getWasteImage(id):
    if request.method == "GET":
        return filemanagement.getWasteImage(id)