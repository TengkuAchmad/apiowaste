# UTILITY IMPORT
from utility.utils import *

# CONNECTION CONFIGURATION
DB_USERNAME     = os.environ.get('DB_USERNAME_CONFIG')
DB_PASSWORD     = os.environ.get('DB_PASSWORD_CONFIG')
DB_DATABASE     = os.environ.get('DB_DATABASE_NAME_CONFIG')
DB_CONNECTION   = os.environ.get('DB_CONNECTION_NAME_CONFIG')

def open_connection():
    try:
        conn = pymysql.connect(
            host=DB_CONNECTION,
            port=3306,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            db=DB_DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
