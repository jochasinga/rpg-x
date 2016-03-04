from __future__ import print_function

import pytest
import os

from app import app as _app
from app import db as _db
from app.models import User, Question, Stage, Candidate, Choice

TEST_DB = 'test.db'
TEST_DB_PATH = "../{}".format(TEST_DB)
TEST_DATABASE_URI = 'sqlite:///' + TEST_DB_PATH

_db.drop_all()

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test Flask app"""

    _app.config['TESTING'] = True
    _app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DATABASE_URI

    # Create app context
    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)

    request.addfinalizer(teardown)
    return _app

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database"""
    if os.path.exists(TEST_DB_PATH):
        os.unlink(TEST_DB_PATH)
        os.remove(TEST_DB_PATH)

    def teardown():
        _db.drop_all()

    _db.app = _app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture(scope='function')
def session(db, request):
    """Create database session for test"""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session

def test_user_model(session):
    user = User(username="joel34", email="joel@example.com")

    session.add(user)
    session.commit()

    assert user.id > 0
    assert user.username == "joel34"
    assert user.email == "joel@example.com"
    assert len(User.query.all()) > 0
    assert User.query.filter(User.username=="joel34") != None
    assert User.query.filter(User.email=="joel@example.com") != None

def test_stage_model(session):

    stage = Stage(stage_name="Capitol Hill", background_url="static/img/capitol.png")

    q1 = Question(body="Howdy?", stage=stage)
    q2 = Question(body="What's ur name?", stage=stage)
    q3 = Question(body="Where do you go?", stage=stage)

    session.add(stage)
    session.add(q1)
    session.add(q2)
    session.add(q3)
    session.commit()

    assert stage.id > 0
    assert stage.stage_name == "Capitol Hill"
    assert stage.background_url == "static/img/capitol.png"
    assert len(Stage.query.all()) > 0
    assert len(stage.questions.all()) == 3
    assert Stage.query.filter(Stage.stage_name=="Capitol Hill") != None

def test_question_model(session):
    stage = Stage(stage_name="Nevada", background_url="static/img/nevada.png")
    question = Question(body="How are you?", stage=stage)

    session.add(stage)
    session.add(question)
    session.commit()

    assert question.id > 0
    assert question.stage.stage_name == 'Nevada'
    assert question.body == "How are you?"
    assert len(Question.query.all()) > 0
    assert Question.query.filter(Question.body=="How are you?") != None

def test_choice_model(session):
    stage = Stage(stage_name="New York", background_url="static/img/nyc.png")
    question = Question(body="How is the weather today?", stage=stage)
    
    choice_1 = Choice(body="It's damn cold.", hp_point=0, xp_point=10, question=question)
    choice_2 = Choice(body="I don't know.", hp_point=0, xp_point=-10, question=question)
    choice_3 = Choice(body="Check Yahoo!", hp_point=10, xp_point=0, question=question)
    choice_4 = Choice(body="It's 46 degree out!", hp_point=20, xp_point=30, question=question)

    choices = [choice_1, choice_2, choice_3, choice_4]

    session.add(stage)
    session.add(question)
    [session.add(choice) for choice in choices]

    session.commit()

    for choice in choices:
        assert choice.id > 0
        assert choice.question.body == "How is the weather today?"
        assert len(choice.body) > 0
        
    assert len(Choice.query.all()) > 0
    assert Choice.query.filter(Choice.body=="I don't know.") != None


    

    
