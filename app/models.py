from .import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin,db.Model):
    __tablename__= 'users'

    

    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    # password_hash = db.Column(db.String(255))
   
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User{self.username}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
class Comment(db.Model):
    __tablename___ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    
    def __repr__(self):
        return f'Comment{self.name}'
    
class Pitch(db.Model):
    __tablename___ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    author = db.Column(db.String(255))
    # users = db.relationship('User',backref = 'comment',lazy='dynamic')
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_user_pitch(cls,name):
        pitches = Pitch.query.filter_by(user = name).all()

        return pitches





    @classmethod
    def get_pitch_category(cls,categoryName):
        pitch_cat_list = Pitch.query.filter_by(category = categoryName)

        return pitch_cat_list

    @classmethod
    def get_all_pitch(cls):
        pitch_list = Pitch.query.all()

        return pitch_list
    
    def __repr__(self):
        return f'Pitch{self.name}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer,primary_key= True)
    downvote = db.Column(db.Integer())
    
    def __repr__(self):
        return f'Downvote{self.downvote}'
        
class Upvote(db.Model):
    __tablename__ = 'upvotes'
    
    id = db.Column(db.Integer,primary_key= True)
    upvote = db.Column(db.Integer())
    
    def __repr__(self):
        return f'Upvote{self.upvote}'
        

    