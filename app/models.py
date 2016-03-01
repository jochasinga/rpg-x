from app import db

class User(db.Model):
    __tablename__ = 'user_auth'

    # User's credentials
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    #password = db.Column(db.String(192), nullable=False)
    #is_admin = db.Column(db.Boolean(), default=True)

    # Authorisation Data
    #role = db.Column(db.SmallInteger, nullable=False)
    #status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        #self.password = password
        #self.is_admin = is_admin

    def add(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.username
