from utils import init_data
from models.user import User
from models.vocabulary import Vocabulary
from models.album import Album
from models.album_vocabulary import AlbumVocabulary
from models.search_history import SearchHistory
from utils.config import *

wses = []
ws_clients = {}
User
Vocabulary
Album
AlbumVocabulary
SearchHistory

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #init_data.drop_all_tables(db,User,Vocabulary,Album,AlbumVocabulary,SearchHistory)
        #init_data.init(db,User,Vocabulary,Album,AlbumVocabulary,SearchHistory)
        #app.run()

 
