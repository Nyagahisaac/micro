from .import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin,db.Model):
    __tablename___ = 'users'

    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.column(db.String(255))
    password_hash = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @property
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User{self.username}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
class Comment(db.Model):
    __tablename___ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'comment',lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.name}'
    
class Pitch(db.Model):
    __tablename___ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.column(db.String(255))
    
        

    