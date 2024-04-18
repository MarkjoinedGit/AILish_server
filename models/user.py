from utils.config import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatarSrc = db.Column(db.String(200))
    advertisingID = db.Column(db.String(200))

    def __repr__(self):
        return f"User('{self.id}','{self.advertisingID}','{self.userName}', '{self.phoneNumber}', '{self.password}', '{self.avatarSrc}')"
    
    def to_dict(self):
        return {
            'id': self.id,
            'userName': self.userName,
            'phoneNumber': self.phoneNumber,
            'avatarSrc': self.avatarSrc,
            'advertisingID': self.advertisingID
        }