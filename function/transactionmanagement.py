# UTILITY IMPORT
from utility.utils import *

def addBalance(data):
    try:
        conn = open_connection() 
        with conn.cursor() as cursor:
            # GET DATA
            UUID_UA     = data['ID_User']
            Balance_UA  = data['Balance_UD']

            # SET DATA
            timenow = datetime.now()

            # GET CURRENT BALANCE
            cursor.execute("SELECT UUID_UA, Balance_UD FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()

            if result:
                CurrentBalance = result['Balance_UD']

                TotalBalance = int(Balance_UA) + int(CurrentBalance)
                cursor.execute("UPDATE User_Data SET Balance_UD = %s, UpdatedAt_UD = %s WHERE UUID_UA = %s", (TotalBalance, timenow, UUID_UA))
                conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status" : "Update balance sukses!"}), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400
    
def getBalance(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_UA = id

            cursor.execute("SELECT UUID_UA, Balance_UD, UpdatedAt_UD FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()

            if result:
                return jsonify({"data" : result}), 200
    except Exception as e:
        return jsonify({"Error :", str(e)}), 400
    

    