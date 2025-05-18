# admin.py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

admin = Admin(name='Token Aggregator', template_mode='bootstrap3')
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Offer, db.session))
admin.add_view(AdminModelView(Payment, db.session))

# In app.py
admin.init_app(app)
