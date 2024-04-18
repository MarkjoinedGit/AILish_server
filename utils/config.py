from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sock import Sock
from flask_cors import CORS
# from models.user import User
# from models.vocabulary import Vocabulary
# from models.album import Album
# from models.album_vocabulary import AlbumVocabulary
# from models.search_history import SearchHistory
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AILISH_DB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
sock = Sock(app)
db = SQLAlchemy(app)
# User
# Vocabulary
# Album
# AlbumVocabulary
# SearchHistory