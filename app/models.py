import datetime
from app import db

class User(db.Model):
    
    __tablename__ = 'user_auth'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    hp = db.Column(db.Integer)
    xp = db.Column(db.Integer)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.hp = 100
        self.xp = 0

    def add(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    def list_all_users(self):
        return User.query.all()

    def __repr__(self):
        return '<User %r>' % self.username

class Stage(db.Model):

    __tablename__ = 'stage'
    
    id = db.Column(db.Integer, primary_key=True)
    stage_name = db.Column(db.String(120), unique=True)
    # uri to image for the background
    background_url = db.Column(db.String(240))

    def __init__(self, stage_name, background_url):
        self.stage_name = stage_name
        self.background_url = background_url

    def __repr__(self):
        return '<Stage %r>' % self.stage_name

class Question(db.Model):
    
    __tablename__ = 'question'
    
    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'))
    stage = db.relationship('Stage', backref=db.backref('questions', lazy='dynamic'))
    body = db.Column(db.Text)

    def __init__(self, body, stage):
        self.body = body
        self.stage = stage

    def __repr__(self):
        return '<Question %r>' % self.body

class Choice(db.Model):

    __tablename__ = 'choice'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(240))
    # Points for candidate's hp and xp
    hp_point = db.Column(db.Integer)
    xp_point = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question', backref=db.backref('choices', lazy='dynamic'))

    def __init__(self, question, body, hp_point, xp_point):
        self.question = question
        self.body = body
        self.hp_point = hp_point
        self.xp_point = xp_point

    def __repr__(self):
        return '<Choice %r>' % self.body

class Candidate(db.Model):
    
    __tablename__ = 'candidate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    # URI to candidate's avatar
    avatar_url = db.Column(db.String(240), unique=True)

    def __init__(self, name, avatar):
        self.name = name
        self.avatar_url = avatar_url

    def __repr__(self):
        return '<Candidate %r>' % self.name

    
