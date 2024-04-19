from sqlalchemy import Enum
from datetime import datetime
from utils.config import db
class Vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String(255), nullable=False)
    pronunciation = db.Column(db.String(255))
    category = db.Column(Enum('NOUN', 'VERB', 'ADJECTIVE', 'ADVERB', 'PRONOUN', 'PREPOSITION', 'CONJUNCTION', 'INTERJECTION'), nullable=False)
    audioSrc = db.Column(db.String(255))
    example = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Vocabulary('{self.id}','{self.word}', '{self.pronunciation}', '{self.category}', '{self.audioSrc}', '{self.example}', '{self.createdAt}')"
    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'pronunciation': self.pronunciation,
            'category': self.category,
            'audioSrc': self.audioSrc,
            'example':self.example,
            'createdAt':self.createdAt
        }