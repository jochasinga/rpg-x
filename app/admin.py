from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Stage, Question, Choice, Candidate

admin = Admin(app, name="Presidential-X", template_mode="bootstrap3")

class StageAdmin(ModelView):
    inline_models = (Question,)
    column_list = ('stage_name', 'background_url')
    form_choices = {'questions': [
        ('choice',)
    ]}


class QuestionView(ModelView):
    
    inline_models = (Choice,)
    column_list = ('body', 'stage')

    def __init__(self, session, **kwargs):
        super(QuestionView, self).__init__(Question, session)

admin.add_view(ModelView(User, db.session))
admin.add_view(StageAdmin(Stage, db.session))
admin.add_view(QuestionView(db.session))
admin.add_view(ModelView(Candidate, db.session))

# Add admin views here


