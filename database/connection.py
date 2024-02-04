# UTILITY IMPORT
from utility.utils import *

# CONNECTION CONFIGURATION
DB_USERNAME_CONFIG          = "technoelectrainc"
DB_PASSWORD_CONFIG          = "owastebandung"
DB_DATABASE_NAME_CONFIG     = "technoelectrainc$db_owaste"
DB_CONNECTION_NAME_CONFIG   = "technoelectrainc.mysql.pythonanywhere-services.com"
JWT_SECRET_KEY_CONFIG       = "menujuindonesiabersih"

def open_connection():
    try:
        conn = pymysql.connect(
            host=DB_CONNECTION_NAME_CONFIG,
            port=3306,
            user=DB_USERNAME_CONFIG,
            password=DB_PASSWORD_CONFIG,
            db=DB_DATABASE_NAME_CONFIG,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
