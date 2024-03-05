# UTILITY IMPORT
from utility.utils import *

def getSedekah():
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Sedekah_Data")
            result = cursor.fetchall()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"status" : "Data not found!"}), 200
            
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400

def updateSedekah(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_SD     = data['UUID_SD']
            Title_SD    = data['Title_SD']
            Desc_SD     = data['Desc_SD']
            timenow     = datetime.now()

            cursor.execute("UPDATE Sedekah_Data SET Title_SD = %s, Desc_SD = %s, UpdatedAt_SD = %s WHERE UUID_SD = %s", (Title_SD, Desc_SD, timenow, UUID_SD))
            conn.commit()
            return jsonify({"status" : "Berhasil update data IPL/PAL"}), 200
        
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400
 