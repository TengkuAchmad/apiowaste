# UTILITY IMPORT
from utility.utils import *

def getListRequest(param):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT Pickup_Address.Address_PA, Pickup_Request.UUID_PR, Pickup_Request.Pickup_Date_PR, User_Data.Name_UD FROM Pickup_Request INNER JOIN Pickup_Address ON Pickup_Request.UUID_PA = Pickup_Address.UUID_PA INNER JOIN User_Account ON Pickup_Address.UUID_UA = User_Account.UUID_UA INNER JOIN User_Data ON User_Account.UUID_UA = User_Data.UUID_UA WHERE Pickup_Request.ID_RS = 2 ORDER BY Pickup_Request.CreatedAt_PR " + param)
            result = cursor.fetchall()
            result = list(result)
            return jsonify(result), 200
        
    except Exception as e:
        return jsonify({"Error :": str(e)}), 400

def getRequestDetails(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT Request_Status.Status_RS, Pickup_Request.UpdatedAt_PR, Pickup_Request.GPS_PR, Pickup_Address.Address_PA, GROUP_CONCAT( Waste_Image.Image_WI SEPARATOR ' || ' ) AS Image_WI_LIST, GROUP_CONCAT( Waste_Category.Category_WC SEPARATOR ' || ') AS ID_WC_LIST, Pickup_Request.Pickup_Date_PR, User_Account.Email_UA, User_Account.UUID_UA, User_Data.Name_UD FROM Pickup_Request INNER JOIN Request_Status ON Pickup_Request.ID_RS = Request_Status.ID_RS INNER JOIN Pickup_Address ON Pickup_Request.UUID_PA = Pickup_Address.UUID_PA INNER JOIN User_Account ON Pickup_Request.UUID_UA = User_Account.UUID_UA INNER JOIN User_Data ON User_Account.UUID_UA = User_Data.UUID_UA INNER JOIN Waste_Image ON Pickup_Request.UUID_PR = Waste_Image.UUID_PR INNER JOIN Pickup_Waste ON Pickup_Request.UUID_PR = Pickup_Waste.UUID_PR INNER JOIN Waste_Category ON Waste_Category.ID_WC = Pickup_Waste.ID_WC WHERE Pickup_Request.UUID_PR = %s", id,)
            result = cursor.fetchone()
            return jsonify({"data": result}), 200
    except Exception as e:
        return jsonify({"Error :":str(e)}), 400
    
def setRequest(data):
    try:
        conn = open_connection()
        
        with conn.cursor() as cursor:
            # GET DATA
            UUID_UA_Input               = data['UUID_UA_Input']
            Address_PA_Input            = data['Address_PA_Input']   
            AddressName_PA_Input        = data['AddressName_PA_Input']
            AddressFavorite_PA_Input    = data['AddressFavorite_PA_Input']
            timenow                     = datetime.now()

            GPS_PR_Input                = data['GPS_PR_Input']
            Pickup_Date_PR_Input        = data['Pickup_Date_PR_Input']
            # ID_RS                       = "1"
            ID_RS                       = "2" 
            ID_WC_Input               = data['ID_WC_Input']

            Image_WI_Input_Array      = data['Image_WI_Input'].split(',')

            # SET DATA
            UUID_PA_Input           = uuid.uuid4()
            UUID_PR_Input           = uuid.uuid4()

            # UPDATING PICKUP ADDRESS FAVORITE
            if AddressFavorite_PA_Input == "1":
                cursor.execute("UPDATE Pickup_Address SET AddressFavorite_PA = 0 WHERE UUID_UA = %s", UUID_UA_Input,)

            #  SAVING PICKUP ADDRESS
            cursor.execute("INSERT INTO Pickup_Address (UUID_PA, UUID_UA, Address_PA, AddressName_PA, AddressFavorite_PA, CreatedAt_PA, UpdatedAt_PA) VALUES (%s, %s, %s, %s, %s, %s, %s)", (UUID_PA_Input, UUID_UA_Input, Address_PA_Input, AddressName_PA_Input, AddressFavorite_PA_Input, timenow, timenow))

            # SAVING PICKUP REQUEST
            cursor.execute("INSERT INTO Pickup_Request (UUID_PR, UUID_PA, UUID_UA, ID_RS, GPS_PR, Pickup_Date_PR, CreatedAt_PR, UpdatedAt_PR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (UUID_PR_Input, UUID_PA_Input, UUID_UA_Input, ID_RS, GPS_PR_Input, Pickup_Date_PR_Input, timenow, timenow))

            # SAVING PICKUP WASTE CATEGORY DATA
            # MULTI ANSWER HANDLING
            UUID_WC_Input_Array = ID_WC_Input.split(",")
            for ID_WC_Input_Data in UUID_WC_Input_Array:
                UUID_PW_Input = uuid.uuid4()
                cursor.execute("INSERT INTO Pickup_Waste (UUID_PW, ID_WC, UUID_PR, CreatedAt_PW, UpdatedAt_PW) VALUES (%s, %s, %s, %s, %s)", (UUID_PW_Input, ID_WC_Input_Data, UUID_PR_Input, timenow, timenow)) 

            # SAVING PICKUP WASTE IMAGE DATA
            # MULTI ANSWER HANDLING
            for data in Image_WI_Input_Array:
                UUID_WI_Input = uuid.uuid4()
                cursor.execute("INSERT INTO Waste_Image (UUID_WI, UUID_PR, Image_WI, CreatedAt_WI, UpdatedAt_WI) VALUES (%s, %s, %s, %s, %s)", (UUID_WI_Input, UUID_PR_Input, data, timenow, timenow))
            conn.commit()
            cursor.close()
            conn.close()

            response = {
                "status" : "Create request success!",
                "UUID_PR" : UUID_PR_Input
            }

            return jsonify(response), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400
    
def cancelRequest(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            timenow = datetime.now()
            cursor.execute("UPDATE Pickup_Request SET ID_RS = 7, UpdatedAt_PR = %s WHERE UUID_PR = %s", (timenow, id))
            conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"msg" : f"Request Pickup with ID : {id} successfully canceled!"}), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)})

def approveDriverRequest(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            timenow = datetime.now()
            cursor.execute("UPDATE Pickup_Request SET ID_RS = 6, UpdatedAt_PR = %s WHERE UUID_PR = %s", (timenow, id))
            conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"msg" : f"Request Pickup with ID : {id} successfully approved by driver!"}), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)})

def doneRequest(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            timenow = datetime.now()
            cursor.execute("UPDATE Pickup_Request SET ID_RS = 4, UpdatedAt_PR = %s WHERE UUID_PR = %s", (timenow, id))
            conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"msg" : f"Request Pickup with ID : {id} successfully finished!"}), 200

    except Exception as e:
        return jsonify({"Error :" : str(e)})
    

def getUserRequest(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            UUID_UA = id
            cursor.execute("SELECT Pickup_Request.UUID_PR, Pickup_Address.Address_PA, Pickup_Request.Pickup_Date_PR, Request_Status.Status_RS FROM Pickup_Request JOIN Pickup_Address ON Pickup_Request.UUID_PA = Pickup_Address.UUID_PA JOIN Request_Status ON Pickup_Request.ID_RS = Request_Status.ID_RS WHERE Pickup_Request.UUID_UA = %s", (UUID_UA,))
            results = cursor.fetchall()
            if results:
                data = []
                for result in results:
                    data.append(result) 
                return jsonify({"data": data}), 200
            else:
                return jsonify({"message": "Data not found!"}), 404
    
    except Exception as e:
        return jsonify({"Error :" : str(e)}), 400