from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:
    def __init__(self,author,id,quote):
        self.id=id
        self.author = author
        self.quote = quote

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    #relationships
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__='bloggs'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String(255),index=True)
    author = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    # relationships will relate to the comment model
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')
    upvotes = db.relationship('Upvote', backref = 'blog', lazy = 'dynamic')


    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.order_by(blog_id=id).desc().all()
        return blogs

    def __repr__(self):
        return f'Blog {self.blog_content}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text)
    blog_id = db.Column(db.Integer,db.ForeignKey('bloggs.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    def __repr__(self):
        return f'Comment : id: {self.id} comment: {self.description}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    blog_id = db.Column(db.Integer,db.ForeignKey('bloggs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(cls,id):
        upvote_pitch = Upvote(user = current_user, blog_id=id)
        upvote_pitch.save_upvotes()

    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(blog_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,blog_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'
