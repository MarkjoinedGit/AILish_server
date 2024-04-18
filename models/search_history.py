from datetime import datetime
from utils.config import db
class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    searchTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    searchedWords = db.Column(db.String(255), nullable=False)