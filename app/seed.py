from __future__ import print_function

import random
from app import db
from app.models import User, Stage, Candidate, Question, Choice

def seed_data():
    
    db.drop_all()
    db.create_all()

    users = {
        "mindyj"     : "mindyj@gmail.com",
        "vlad33"     : "vlad33@hotmail.com",
        "pcdope"     : "pancho@yahoo.com",
        "farhad"     : "fh_bok@gmail.com",
        "infinize12" : "infinize12@gmail.com"
    }

    stages = {
        "Capitol Hill"   : "static/img/capitol.png",
        "Texas"          : "static/img/texas.png",
        "South Carolina" : "static/img/sc.png",
        "New York"       : "static/img/nyc.png",
        "Cupertino"      : "static/img/cuper.png"
    }
    
    """
    candidates = {
        "Donald Trump"    : "http://wapo.st/1nmMFBa",
        "Hillary Clinton" : "http://bit.ly/1p6mH70",
        "Ted Cruz"        : "http://bit.ly/1BvBqWY",
        "Bernie Sanders"  : "http://bit.ly/1prbq0Q",
        "Marco Rubio"     : "http://bit.ly/1QYXOWG"
    }
    """

    candidates = {
        "Donald Trump"    : "static/img/candidates/trump.jpg",
        "Hillary Clinton" : "static/img/candidates/clinton.jpg",
        "Ted Cruz"        : "static/img/candidates/cruz.jpg",
        "Bernie Sanders"  : "static/img/candidates/sanders.jpg",
        "Marco Rubio"     : "static/img/candidates/rubio.jpg"
    }

    questions = [
        "How will you tackle the problems and overfunding in US education?",
        "How will you tackle the immigration issues?",
        "What is your opinion toward North Korea?"
    ]

    choices = [
        [
            "Reduce funding.",
            "Fast-forward education with more funding!",
            "Shift the fund to STEAM programs",
            "No comment."
        ],
        [
            "Build a wall around our country!",
            "Impose higher taxes on foreigners.",
            "Increase H1-B fees.",
            "No comment."
        ],
        [
            "We will ban them, for sure.",
            "They are definitely a threat.",
            "It is unique.",
            "No comment."
        ]
    ]

    """List-comprehension/map-lambda Hell ahead!"""
    
    # Add users
    [db.session.add(user) for user in map(lambda u, e: User(u, e),
        [username for username in users],
        [users[username] for username in users])
    ]

    # Add stages
    [db.session.add(stage) for stage in map(lambda n, u: Stage(n, u),
        [stage_name for stage_name in stages],
        [stages[stage_name] for stage_name in stages])
    ]

    # Add questions
    [db.session.add(question) for question in map(lambda b, s: Question(b, s),
        [body for body in questions],
        [random.choice(Stage.query.all()) for i in range(len(questions))])
    ]

    # Add choices
    for i, group in enumerate(choices):
        for choice in group:
            xp = random.randint(-5, 5)
            hp = random.randint(1, 10)
            q = Question.query.all()[i]
            Choice(choice, xp, hp, q)

    # Add candidates
    [db.session.add(cd) for cd in map(lambda n, u: Candidate(n, u),
        [name for name in candidates],
        [candidates[name] for name in candidates])
    ]
    
    try:
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        raise
    
