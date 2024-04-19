from datetime import datetime
from utils.config import db
class Album(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
        return f"Album('{self.id}','{self.name}','{self.userId}', '{self.createdAt}', '{self.updatedAt}')"
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'userId': self.userId,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }