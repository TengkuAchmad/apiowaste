# UTILITY IMPORT
from utility.utils import *

# ROUTES IMPORT
from utility.routes import *

# PROJECT CONFIG
import sys
sys.dont_write_bytecode = True

# APP DECLARATOR
app = Flask(__name__)

# CORS DECLARATOR
CORS(app)

# JWT MANAGER
app.config['JWT_SECRET_KEY'] = 'maribersihkanindonesia'
jwt = JWTManager(app)

# ROUTES REGISTER INDEX
app.register_blueprint(security_blueprint)
app.register_blueprint(accounts_blueprint)
app.register_blueprint(request_blueprint)
app.register_blueprint(files_blueprint)
app.register_blueprint(transaction_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(voucher_blueprint)
app.register_blueprint(iplpal_blueprint)
app.register_blueprint(sedekah_blueprint)
app.register_blueprint(driver_blueprint)

if __name__ == '__main__':
    app.run(debug=True)