from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Stage, Question, Candidate

admin = Admin(app, name="Presidential-X", template_mode="bootstrap3")

class StageAdmin(ModelView):
        inline_models = (Question,)                                                                                                       
admin.add_view(ModelView(User, db.session))
admin.add_view(StageAdmin(Stage, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Candidate, db.session))

# Add admin views here


