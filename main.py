from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AILISH_DB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    avatarSrc = db.Column(db.String(200))

    def __repr__(self):
        return f"User('{self.userName}', '{self.phoneNumber}', '{self.password}', '{self.avatarSrc}')"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(User.query.all())
    ##app.run()

 
