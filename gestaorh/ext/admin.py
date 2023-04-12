from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from gestaorh.ext.database import db
from gestaorh.blueprints.models.user import User
from gestaorh.blueprints.models.employee import Employee
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash


# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()

class UserView(sqla.ModelView):
    column_list = ['name', 'email','description']
    column_searchable_list = ['name', 'email']
    create_modal = True
    edit_modal = True
    can_export = True
    page_size = 2
    can_edit = False


    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)



class EmployeeView(sqla.ModelView):
    create_modal = True
    edit_modal = True
    can_export = True
    page_size = 2


admin.add_view(EmployeeView(Employee, db.session))
admin.add_view(UserView(User, db.session, category='users'))

def init_app(app):
	admin.name = app.config.TITLE
	admin.init_app(app)