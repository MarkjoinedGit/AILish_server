from datetime import datetime
from utils.config import db
class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    searchTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    searchedWords = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f"SearchHistory('{self.id}','{self.userId}','{self.searchTime}', '{self.searchedWords}')"
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'searchTime': self.searchTime,
            'searchedWords': self.searchedWords,
        }