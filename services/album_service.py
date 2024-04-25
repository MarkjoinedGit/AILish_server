from models.album import Album
from models.album_vocabulary import AlbumVocabulary
from utils.config import db

class AlbumService:
    def __init__(self):
        pass
    
    @staticmethod
    def create_album(user_id, name):
        album = Album(userId=user_id, name=name)
        db.session.add(album)
        db.session.commit()
        return album
    
    @staticmethod
    def delete_album(album_id):
        album = Album.query.get(album_id)
        if album:
            db.session.delete(album)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def add_vocabulary_in_album(album_id, vocabulary_id):
        album_vocabulary = AlbumVocabulary(albumId=album_id, vocabularyId=vocabulary_id)
        db.session.add(album_vocabulary)
        db.session.commit()
        return album_vocabulary
    
    @staticmethod
    def add_list_vocabulary_in_album(album_id, vocabulary_ids):
        album_vocabulary_list = []
        for vocabulary_id in vocabulary_ids:
            album_vocabulary = AlbumVocabulary(albumId=album_id, vocabularyId=vocabulary_id)
            album_vocabulary_list.append(album_vocabulary)
        db.session.add_all(album_vocabulary_list)
        db.session.commit()
        return album_vocabulary_list
    
    @staticmethod
    def load_all_album_with_user_id(user_id):
        albums = Album.query.filter_by(userId=user_id).all()
        return albums