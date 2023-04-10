from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from gestaorh.ext.database import db
from gestaorh.blueprints.models.user import User
from gestaorh.blueprints.models.employee import Employee


admin = Admin()

class UserView(ModelView):
    column_searchable_list = ['name', 'email']
    column_editable_list = ['name']
    create_modal = True
    edit_modal = True
    can_export = True
    page_size = 2


class EmployeeView(ModelView):
    create_modal = True
    edit_modal = True
    can_export = True
    page_size = 2


admin.add_view(EmployeeView(Employee, db.session))
admin.add_view(UserView(User, db.session, category='users'))

def init_app(app):
	admin.name = app.config.TITLE
	admin.init_app(app)