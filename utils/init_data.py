import hashlib
from datetime import datetime
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def drop_all_tables(db,User,Vocabulary,Album,AlbumVocabulary,SearchHistory):
    all_tables = [User.__table__, Vocabulary.__table__, Album.__table__, AlbumVocabulary.__table__, SearchHistory.__table__]
    for table in all_tables:
        table.drop(db.engine)
        print(f"Đã drop bảng {table.name}")
        
def init(db,User,Vocabulary,Album,AlbumVocabulary,SearchHistory):
    new_user = User(userName='aKhoa123',advertisingID='FFAHH-BV251-0000-1957', phoneNumber='0315522568', password=hash_password("123456"), avatarSrc='')
    db.session.add(new_user)

    new_vocabulary = Vocabulary(word='apple',definitions='trái táo', userId=1, pronunciation='ˈæpəl', category='NOUN', audioSrc='apple.mp3', example='I ate an apple.', createdAt=datetime.utcnow())
    db.session.add(new_vocabulary)

    new_album = Album(name='Food', userId=1)
    
    db.session.add(new_album)
     
    new_album_vocabulary = AlbumVocabulary(albumId=1, vocabularyId=1)
    db.session.add(new_album_vocabulary)

    new_search_history = SearchHistory(userId=1, searchedWords='apple, banana, orange', searchTime=datetime.utcnow())
    db.session.add(new_search_history)

    db.session.commit()
    