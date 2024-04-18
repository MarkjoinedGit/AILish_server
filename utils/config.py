from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_sock import Sock
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AILISH_DB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
sock = Sock(app)
db = SQLAlchemy(app)
wses = []
ws_clients = {}


