# UTILITY IMPORT
from utility.utils import *

def auth_account(data):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            Email_UA_Input      = data['Email_UA_Input']
            Password_UA_Input   = data['Password_UA_Input']

            # EMAIL CHECKING AVAILABILITY
            cursor.execute("SELECT * FROM User_Account WHERE Email_UA = %s", Email_UA_Input,)
            result = cursor.fetchone()

            if result:
                # PASSWORD CHECKING
                UUID_UA         = result['UUID_UA']
                Password_UA     = result['Password_UA']
                RoleAccess_UA   = result['RoleAccess_UA']
                
                if check_password_hash(Password_UA, Password_UA_Input):
                    access_token = create_access_token(identity=UUID_UA)
                    refresh_token = create_refresh_token(identity=UUID_UA)

                    cursor.execute("SELECT * FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
                    result = cursor.fetchone()

                    if result:
                        name_user = result['Name_UD']
                        return jsonify({"access_token":access_token, "refresh_token":refresh_token, "UUID_UA":UUID_UA, "Role":RoleAccess_UA, "Name": name_user}), 200
        
                else:
                    return jsonify({"status" : "Password invalid!"}), 400
            else:
                return jsonify("status", "Email not registered!"), 404
            
    except Exception as e:
        return jsonify({"Error: " : str(e)}), 400

def reg_account(data, role):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            Email_UA_Input      = data['Email_UA_Input']
            Password_UA_Input   = generate_password_hash(data['Password_UA_Input'])
            Name_UD_Input       = data['Name_UD_Input']
            Birthplace_UD_Input = data['Birthplace_UD_Input']
            Birthdate_UD_Input  = data['Birthdate_UD_Input']
            Address_UD_Input    = data['Address_UD_Input']

            # SET DATA
            UUID_UA             = uuid.uuid4()
            UUID_UD             = uuid.uuid4()
            Balance_UD          = 0
            timenow             = datetime.now()

            if role == "user":
                RoleAccess_UA_Input = "User"
            elif role == "admin":
                RoleAccess_UA_Input = "Admin"
            elif role == "driver":
                RoleAccess_UA_Input = "Driver"

            # EMAIL CHECKING
            cursor.execute("SELECT * FROM User_Account WHERE Email_UA = %s", (Email_UA_Input)) 
            result = cursor.fetchone()

            if result:
                return jsonify({"status":"Email is already registered!"}),400
            elif not result:
                cursor.execute("INSERT INTO User_Account (UUID_UA, Email_UA, Password_UA, RoleAccess_UA, CreatedAt_UA, UpdatedAt_UA) VALUES (%s, %s, %s, %s, %s, %s)", (UUID_UA, Email_UA_Input, Password_UA_Input, RoleAccess_UA_Input, timenow, timenow))

                cursor.execute("INSERT INTO User_Data (UUID_UD, UUID_UA, Name_UD, Birthplace_UD, Birthdate_UD, Address_UD, Balance_UD, CreatedAt_UD, UpdatedAt_UD) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (UUID_UD, UUID_UA, Name_UD_Input, Birthplace_UD_Input, Birthdate_UD_Input, Address_UD_Input, Balance_UD, timenow, timenow))

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"status" : "Account success registered!"}), 200

    except Exception as e:
        return jsonify({"Error: " : str(e)}), 400
    

def current_user(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            UUID_UA = id
            cursor.execute("SELECT * FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()

            if result:
                return jsonify(result), 200
            
    except Exception as e:
        return jsonify({"Error :" : str(e)})