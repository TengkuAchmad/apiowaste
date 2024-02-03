# UTILITY IMPORT
from utility.utils import *

def getWasteImage(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT Image_WI FROM Waste_Image WHERE UUID_WI = %s", id,)
            result = cursor.fetchone()
            if result:
                image_blob = result['Image_WI']
                base64_data = base64.b64encode(image_blob).decode('utf-8')
                return jsonify({"image_data": base64_data}), 200
            else:
                return jsonify({"message": "Image not found"}), 404
        
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400