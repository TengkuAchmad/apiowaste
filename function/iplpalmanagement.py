# UTILITY IMPORT
from utility.utils import *


def updateIPLPAL(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_ID     = data['UUID_ID']
            Title_ID    = data['Title_ID']
            Price_ID    = data['Price_ID']
            Desc_ID     = data['Desc_ID']
            timenow     = datetime.now()

            cursor.execute("UPDATE IPLPAL_Data SET Title_ID = %s, Price_ID = %s, Desc_ID = %s, UpdatedAt_ID = %s WHERE UUID_ID = %s", (Title_ID, Price_ID, Desc_ID, timenow, UUID_ID))
            conn.commit()
            return jsonify({"status" : "Berhasil update data IPL/PAL"}), 200
        
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400

def getIPLPAL():
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM IPLPAL_Data")
            result = cursor.fetchall()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"status" : "Data not found!"}), 200
            
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400
 