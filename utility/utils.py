# LIBRARY IMPORT
import os
import io
import pymysql
import uuid
import random
import base64
import string
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import  create_refresh_token, create_access_token, decode_token, JWTManager, jwt_required
from pymysql import *

# FUNCTION IMPORT
from database.connection import open_connection
from function import accountmanagement, passwordmanagement, requestmanagement, filemanagement, wastemanagement

from dotenv import load_dotenv
load_dotenv()