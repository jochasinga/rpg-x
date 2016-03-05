import datetime
from app import app, db
from wtforms import validators
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters

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

    def __init__(self, body, hp_point, xp_point, question):
        self.question = question
        self.body = body
        self.hp_point = hp_point
        self.xp_point = xp_point

    def __str__(self):
        return self.body

    def __repr__(self):
        return '<Choice %r>' % self.body

class Candidate(db.Model):
    
    __tablename__ = 'candidate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    # URI to candidate's avatar
    avatar_url = db.Column(db.String(240), unique=True)

    def __init__(self, name, avatar_url):
        self.name = name
        self.avatar_url = avatar_url

    def __repr__(self):
        return '<Candidate %r>' % self.name

# Admin

"""
class UserAdmin(sqla.ModelView):
    inline_models = (User,)

class StageAdmin(sqla.ModelView):
    column_sortable_list = ('stage_name',)
    column_labels = dict(stagename='Stage Name')
    column_searchable_list = ('stage_name',)

    # Pass arguments to WTForms
    form_args = dict(
                     text=dict(label='Big Text', validators=[validators.required()])
        )

    def __init__(self, session):
        # Call parent class with predefined model.
        super(StageAdmin, self).__init__(Stage, session)


class CandidateAdmin(sqla.ModelView):
    column_sortable_list = ('name')
    column_labels = dict(name='Candidate')
    column_searchable_list = ('name',)


class QuestionView(sqla.ModelView):
    form_excluded_columns = ['stage_id',]

class ChoiceView(sqla.ModelView):
    from_excluded_columns = ['question_id',]

# Create admin
admin = admin.Admin(app, name='Presidential-X', template_mode='bootstrap3')

# Add views
#admin.add_view(UserAdmin(User, db.session))
#admin.add_view(StageAdmin(db.session))
admin.add_view(QuestionView(Question, db.session))
admin.add_view(ChoiceView(Choice, db.session))
#admin.add_view(CandidateAdmin(Candidate, db.session))

"""
    
    

    
