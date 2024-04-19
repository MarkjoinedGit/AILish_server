from models.search_history import SearchHistory
from utils.config import db

class SearchHistoryService:
    def __init__(self):
        pass
    
    @staticmethod
    def create_search_history(user_id, searched_words):
        search_history = SearchHistory(userId=user_id, searchedWords=searched_words)
        db.session.add(search_history)
        db.session.commit()
        return search_history
    
    @staticmethod
    def load_all_search_history_with_user_id(user_id):
        search_histories = SearchHistory.query.filter_by(userId=user_id).all()
        return search_histories
    
    @staticmethod
    def delete_search_history(search_history_id):
        search_history = SearchHistory.query.get(search_history_id)
        if search_history:
            db.session.delete(search_history)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def delete_all_search_history_with_user_id(user_id):
        search_histories = SearchHistory.query.filter_by(userId=user_id).all()
        for search_history in search_histories:
            db.session.delete(search_history)
        db.session.commit()
    