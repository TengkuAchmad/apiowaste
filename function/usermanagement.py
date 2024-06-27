# UTILITY IMPORT
from utility.utils import *

def user_list():
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM User_Data JOIN User_Account ON User_Data.UUID_UA = User_Account.UUID_UA WHERE User_Account.RoleAccess_UA = %s", ("User",))
            result = cursor.fetchall()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"status" : "Data not found!"}), 200
        
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400

def user_edit(data):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            # GET DATA
            UUID_UA         = data['UUID_UA']
            Email_UA        = data['Email_UA']
            Password_UA     = generate_password_hash(data['Password_UA'])
            RoleAccess_UA   = data['RoleAccess_UA']
            Name_UD         = data['Name_UD']
            Birthplace_UD   = data['Birthplace_UD']
            Birthdate_UD    = data['Birthdate_UD']
            Address_UD      = data['Address_UD']
            Balance_UD      = data['Balance_UD']
            timenow         = datetime.now()
            # DATA CHECK
            cursor.execute("SELECT * FROM User_Data WHERE UUID_UA = %s", (UUID_UA,))
            result = cursor.fetchone()

            if result:
                cursor.execute("UPDATE User_Account SET Email_UA = %s, Password_UA = %s, RoleAccess_UA = %s, UpdatedAt_UA = %s WHERE UUID_UA = %s", (Email_UA, Password_UA, RoleAccess_UA, timenow, UUID_UA))
                conn.commit()

                cursor.execute("UPDATE User_Data SET Name_UD = %s, Birthplace_UD = %s, Birthdate_UD = %s, Address_UD = %s, Balance_UD = %s, UpdatedAt_UD = %s WHERE UUID_UA = %s", (Name_UD, Birthplace_UD, Birthdate_UD, Address_UD, Balance_UD, timenow, UUID_UA))
                conn.commit()
                return jsonify({"status" : "Update user success!"}), 200
            else:
                return jsonify({"status" : "Update user failed, user not found"}), 400
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400

def user_details(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM User_Data JOIN User_Account ON User_Data.UUID_UA = User_Account.UUID_UA WHERE User_Account.RoleAccess_UA = %s AND User_Account.UUID_UA = %s", ("User", id,))
            result = cursor.fetchone()

            if result:
                return jsonify(result), 200
            else:
                return jsonify({"status" : "Data not found!"}), 200
            
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400

def delete_user(id):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM User_Data JOIN User_Account ON User_Data.UUID_UA = User_Account.UUID_UA WHERE User_Account.UUID_UA = %s", (id,))
            result = cursor.fetchone()

            if result:
                cursor.execute("DELETE FROM User_Data WHERE User_Data.UUID_UA = %s", (id,))
                conn.commit()

                cursor.execute("DELETE FROM User_Account WHERE User_Account.UUID_UA = %s", (id,))
                conn.commit()
                return jsonify({"status" : "Data user deleted succesfully!"}), 200
            else:
                return jsonify({"status" : "Data not found!"}), 200
            
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400

    
