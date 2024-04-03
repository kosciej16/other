from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView


def setup_admin(app, db):
    from models.user import User

    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    admin = Admin(app, name="microblog", template_mode="bootstrap3")
    admin.add_view(ModelView(User, db.session))
