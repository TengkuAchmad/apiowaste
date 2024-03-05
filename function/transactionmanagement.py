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

                # SET DATA
                UUID_TD = uuid.uuid4()
                Status_TD = "Topup"
                
                cursor.execute("INSERT INTO Transaction_Data (UUID_TD, UUID_UA, Balance_TD, Status_TD, CreatedAt_TD, UpdatedAt_TD) VALUES (%s, %s, %s, %s, %s, %s)", (UUID_TD, UUID_UA, Balance_UA, Status_TD, timenow, timenow))
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
            else:
                return jsonify({"data": "Data not found!"}), 404
            
    except Exception as e:
        return jsonify({"Error :", str(e)}), 400
    
def buyVoucher(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_TD     = uuid.uuid4()
            UUID_VT     = uuid.uuid4()
            UUID_UA     = data['UUID_UA']
            UUID_VD     = data['UUID_VD']
            Status_TD   = "Pembelian Voucher"
            Code_VT     = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            Status_VT   = "Active"
            timenow     = datetime.now()


            # GET PRICE
            cursor.execute("SELECT Voucher_Data.Price_VD FROM Voucher_Data WHERE UUID_VD = %s", (UUID_VD,))
            result = cursor.fetchone()

            if result:
                Price_Voucher = float(result['Price_VD'])

                cursor.execute("SELECT Balance_UD FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
                result = cursor.fetchone()

                if result:
                    Balance_User = float(result['Balance_UD'])
                    
                    if (Balance_User >= Price_Voucher):

                        TotalBalance = Balance_User - Price_Voucher

                        # BALANCE UPDATE
                        cursor.execute("UPDATE User_Data SET Balance_UD = %s WHERE UUID_UA = %s", (TotalBalance, UUID_UA))
                        conn.commit()

                        cursor.execute("INSERT INTO Transaction_Data (UUID_TD, UUID_UA, Balance_TD, Status_TD, CreatedAt_TD, UpdatedAt_TD) VALUES (%s, %s, %s, %s, %s, %s)", (UUID_TD, UUID_UA, Price_Voucher, Status_TD, timenow, timenow))
                        conn.commit()

                        cursor.execute("INSERT INTO Voucher_Transaction (UUID_VT, UUID_VD, UUID_UA, UUID_TD, Code_VT, Status_VT, CreatedAt_VT, UpdatedAt_VT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (UUID_VT, UUID_VD, UUID_UA, UUID_TD, Code_VT, Status_VT, timenow, timenow))
                        conn.commit()

                        cursor.close()
                        conn.close()

                        return jsonify({"status" : "Transaksi pembelian voucher berhasil!"}), 200
                    else:
                        return jsonify({"status" : "Insufficient balance to carry out transactions"}), 400
    except Exception as e:
        return jsonify({"Error :", str(e)}), 400

def buyIPLPAL(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_TD             = uuid.uuid4()
            UUID_IT             = uuid.uuid4()
            UUID_UA             = data['UUID_UA']
            UUID_ID             = data['UUID_ID']
            PaymentBalance_IT   = float(data['PaymentBalance_IT'])
            Status_TD           = "Pembayaran IPL/PAL"
            CodePayment_IT      = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            Status_IT          = "Valid"
            timenow             = datetime.now()

            cursor.execute("SELECT Balance_UD FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()

            if result:
                Balance_User = float(result['Balance_UD'])
                
                if (Balance_User >= PaymentBalance_IT):

                    TotalBalance = Balance_User - PaymentBalance_IT

                    # BALANCE UPDATE
                    cursor.execute("UPDATE User_Data SET Balance_UD = %s WHERE UUID_UA = %s", (TotalBalance, UUID_UA))
                    conn.commit()

                    cursor.execute("INSERT INTO Transaction_Data (UUID_TD, UUID_UA, Balance_TD, Status_TD, CreatedAt_TD, UpdatedAt_TD) VALUES (%s, %s, %s, %s, %s, %s)", (UUID_TD, UUID_UA, PaymentBalance_IT, Status_TD, timenow, timenow))
                    conn.commit()

                    cursor.execute("INSERT INTO IPLPAL_Transaction (UUID_IT, UUID_ID, UUID_UA, UUID_TD, CodePayment_IT, Status_IT, CreatedAt_IT, UpdatedAt_IT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (UUID_IT, UUID_ID, UUID_UA, UUID_TD, CodePayment_IT,Status_IT, timenow, timenow))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return jsonify({"status" : "Transaksi pembayaran IPL/PAL berhasil!"}), 200
                else:
                    return jsonify({"status" : "Insufficient balance to carry out transactions"}), 400
    except Exception as e:
        return jsonify({"Error :", str(e)}), 400

def buySedekah(data):
    try :
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_TD             = uuid.uuid4()
            UUID_ST             = uuid.uuid4()
            UUID_UA             = data['UUID_UA']   
            UUID_SD             = data['UUID_SD']
            PaymentBalance_ST   = float(data['PaymentBalance_ST'])
            Status_TD           = "Sumbangan Sedekah"
            CodePayment_ST      = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            Status_ST          = "Valid"
            timenow             = datetime.now()

            cursor.execute("SELECT Balance_UD FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()
            if result:
                Balance_User = float(result['Balance_UD'])
                
                if (Balance_User >= PaymentBalance_ST):

                    TotalBalance = Balance_User - PaymentBalance_ST

                    # BALANCE UPDATE
                    cursor.execute("UPDATE User_Data SET Balance_UD = %s WHERE UUID_UA = %s", (TotalBalance, UUID_UA))
                    conn.commit()

                    cursor.execute("INSERT INTO Transaction_Data (UUID_TD, UUID_UA, Balance_TD, Status_TD, CreatedAt_TD, UpdatedAt_TD) VALUES (%s, %s, %s, %s, %s, %s)", (UUID_TD, UUID_UA, PaymentBalance_ST, Status_TD, timenow, timenow))
                    conn.commit()

                    cursor.execute("INSERT INTO Sedekah_Transaction (UUID_ST, UUID_SD, UUID_UA, UUID_TD, CodePayment_ST, Status_ST, CreatedAt_ST, UpdatedAt_ST) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (UUID_ST, UUID_SD, UUID_UA, UUID_TD, CodePayment_ST,Status_ST, timenow, timenow))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return jsonify({"status" : "Transaksi sedekah berhasil!"}), 200
                else:
                    return jsonify({"status" : "Insufficient balance to carry out transactions"}), 400
            else:
                return jsonify({"status" : "Insufficient balance to carry out transactions, please topup"}), 400
    except Exception as e:
        return jsonify({"Error :", str(e)}), 400

