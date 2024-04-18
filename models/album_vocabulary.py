from utils.config import db
class AlbumVocabulary(db.Model):
    albumId = db.Column(db.Integer, db.ForeignKey('album.id'), primary_key=True)
    vocabularyId = db.Column(db.Integer, db.ForeignKey('vocabulary.id'), primary_key=True)