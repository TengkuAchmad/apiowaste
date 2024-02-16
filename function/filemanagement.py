# UTILITY IMPORT
from utility.utils import *
    
def getWasteImage(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT Image_WI FROM Waste_Image WHERE UUID_PR = %s", id,)
            results = cursor.fetchall()
            if results:
                image_links = []
                for result in results:
                    image_links.append(result) 
                return jsonify({"image_links": image_links}), 200
            else:
                return jsonify({"message": "Data not found!"}), 404
        
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400