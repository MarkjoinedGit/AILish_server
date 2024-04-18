from models.user import User
from utils.config import db

class UserService:
    def __init__(self):
        pass
    @staticmethod
    def find_user_by_advertising_id(advertising_id):
        user = User.query.filter_by(advertisingID=advertising_id).first()
        if user:
            return user,True
        else:
            return None ,False
    @staticmethod
    def login_by_phone_number_and_password(phone_number, password):
        user = User.query.filter_by(phoneNumber=phone_number).first()
        if user and user.password == password:
            return user,True
        return None, False
    
    @staticmethod
    def update_advertising_id(user_id, new_advertising_id):
        user = User.query.get(user_id)
        if user:
            user.advertisingID = new_advertising_id
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_password(user_id,prev_password, new_password):
        user = User.query.get(user_id)
        if user and prev_password == user.password:
            user.password = new_password
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_user_name(user_id, password, new_user_name):
        user = User.query.get(user_id)
        if user and password == user.password:
            user.userName = new_user_name
            db.session.commit()
            return True
        return False

    @staticmethod
    def update_phone_number(user_id, password, new_phone_number):
        user = User.query.get(user_id)
        if user and password == user.password:
            user.phoneNumber = new_phone_number
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_avatar_src(user_id, password, new_avatar_src):
        user = User.query.get(user_id)
        if user and password == user.password:
            user.avatarSrc = new_avatar_src
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def create_user(userName, phoneNumber, password, avatarSrc=None, advertisingID=None):
        user = User(userName=userName, phoneNumber=phoneNumber, password=password, avatarSrc=avatarSrc, advertisingID=advertisingID)
        db.session.add(user)
        db.session.commit()
        return user

