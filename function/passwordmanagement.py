# UTILITY IMPORT
from utility.utils import *

def update_pass(data):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            Email_UA_Input = data['Email_UA_Input']

    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400