import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, pw):
        self.username = username
        self.password = pw

    @classmethod
    def find_user_by_name(cls, _username):
        return UserModel.query.filter_by(username=_username).first()
    
    @classmethod
    def find_user_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id': self.id, 'username': self.username, 'password': self.password}
