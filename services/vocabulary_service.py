from models.vocabulary import Vocabulary
from utils.config import db

class VocabularyService:
    def __init__(self):
        pass
    
    @staticmethod
    def create_vocabulary(user_id, word, pronunciation, category, audioSrc=None, example=None):
        vocabulary = Vocabulary(user_id=user_id, word=word, pronunciation=pronunciation, category=category, audioSrc=audioSrc, example=example)
        db.session.add(vocabulary)
        db.session.commit()
        return vocabulary

    @staticmethod
    def delete_vocabulary(vocabulary_id):
        vocabulary = Vocabulary.query.get(vocabulary_id)
        if vocabulary:
            db.session.delete(vocabulary)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_all_with_user_id(user_id):
        vocabularies = Vocabulary.query.filter_by(userId=user_id).all()
        return vocabularies