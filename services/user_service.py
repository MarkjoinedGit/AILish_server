from models.user import User
class UserService:
    def __init__(self):
        pass
    def find_user_by_advertising_id(self,advertising_id):
        user = User.query.filter_by(advertisingID=advertising_id).first()
        if user:
            return user
        else:
            return False