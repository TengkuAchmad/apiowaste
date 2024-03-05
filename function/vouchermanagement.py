# UTILITY IMPORT
from utility.utils import *

def addVoucher(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_VD     = uuid.uuid4()
            Title_VD    = data['Title_VD']
            Price_VD    = data['Price_VD']
            Amount_VD   = data['Amount_VD']
            Desc_VD     = data['Desc_VD']
            timenow     = datetime.now()

            cursor.execute("INSERT INTO Voucher_Data (UUID_VD, Title_VD, Price_VD, Amount_VD, Desc_VD, CreatedAt_VD, UpdatedAt_VD) VALUES (%s, %s, %s, %s, %s, %s, %s)", (UUID_VD, Title_VD, Price_VD, Amount_VD, Desc_VD, timenow, timenow))
            conn.commit()
            return jsonify({"status" : "Berhasil menambahkan voucher baru!"}), 200
        
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400

def getVoucher():
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Voucher_Data")
            result = cursor.fetchall()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"status" : "Data not found!"}), 404
            
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400

def deleteVoucher(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Voucher_Data WHERE UUID_VD = %s", (id,))
            conn.commit()

            return jsonify({"status" : "Delete voucher success!"}), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400    