# UTILITY IMPORT
from utility.utils import *

# APP DECLARATOR
app = Flask(__name__)

# CORS DECLARATOR
CORS(app)

# JWT MANAGER
app.config['JWT_SECRET_KEY'] = 'maribersihkanindonesia'
jwt = JWTManager(app)

# LOGIN ACCOUNT ENDPOINT
@app.route('/account-management/auth', methods=['POST'])
def auth():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status':'Missing form-data in request'}), 400
        else:
            data = request.form.to_dict()
            return accountmanagement.auth_account(data)

# REGISTER ACCOUNT ENDPOINT
@app.route('/account-management/reg/<string:role>', methods=['POST'])
def reg(role):
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status' : 'Missing form-datta in request'}), 400
        else:
            data = request.form.to_dict()
            return accountmanagement.reg_account(data, role)

# FORGOT PASSWORD ENDPOINT
@app.route('/password-management/update', methods=['POST'])
def updatepass():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status' : 'Missing form-data in request'}), 400
        else:
            data = request.form.to_dict()
            return passwordmanagement.update_pass(data) # BUILDING (NOT TO USE)

@app.route('/request-management/create', methods=['POST'])
@jwt_required()
def createrequest():
    if request.method == "POST":
        if 'multipart/form-data' not in request.content_type:
            return jsonify({'status': 'Missing form-data in request' }), 400
        else:
            data = request.form.to_dict()
            files = request.files
            return requestmanagement.setRequest(data, files)

@app.route('/request-management/get/<string:role>', methods=['GET'])
@jwt_required()
def getrequest(role):
    if request.method == "GET":
        if role == "driver":
            return requestmanagement.getListRequest()

@app.route('/request-management/get/detail/<string:id>', methods=['GET'])
@jwt_required()
def getdetails(id):
    if request.method == "GET":
        return requestmanagement.getRequestDetails(id)
    
    
@app.route('/request-management/cancel/<string:id>', methods=['GET'])
@jwt_required()
def cancelrequest(id):
    if request.method == "GET":
        return requestmanagement.cancelRequest(id)

@app.route('/request-management/approve-driver/<string:id>', methods=['GET'])
@jwt_required()
def approvedriverrequest(id):
    if request.method == "GET":
        return requestmanagement.approveDriverRequest(id)
    
@app.route('/request-management/done/<string:id>', methods=['GET'])
@jwt_required()
def donerequest(id):
    if request.method == "GET":
        return requestmanagement.doneRequest(id)


@app.route('/file-management/get/<string:id>', methods=['GET'])
@jwt_required()
def getWasteImage(id):
    if request.method == "GET":
        return filemanagement.getWasteImage(id)
    
@app.route('/request-management/get-status', methods=['GET'])
@jwt_required()
def getStatus():
    if request.method == "GET":
        return wastemanagement.getRequestCategory()
    
if __name__ == '__main__':
    app.run(debug=True)