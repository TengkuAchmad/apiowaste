# UTILITY IMPORT
from utility.utils import *

def getRequestCategory():
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Waste_Category")
            result = cursor.fetchall()

            return jsonify(result), 200
    except Exception as e:
        return jsonify({"Error :": str(e)})
