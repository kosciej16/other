import subprocess
from flask import Flask
from flask import request

from flask.helpers import url_for
from flask.templating import render_template

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

# from admin.admin import setup_admin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # db = SQLAlchemy(app)
# setup_admin(app, db)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    # form = LoginForm()
    return redirect(url_for("RetrieveList"))
    # return render_template("login.html", title="Login")

    # if form.validate_on_submit():

    #     if form.loginname.data == 'admin' and form.loginpassword.data == 'password':
    #         flash('Logged in!', 'success')
    #         return redirect(url_for('RetrieveList'))
    #     else:
    #         flash('Coulnd't log in!', 'danger')
    # return render_template('login.html', title='Login', form=form)


@app.route("/data")
def RetrieveList():
    employees = []
    return render_template("login.html", employees=employees)


def generateMetrics():
    return "hello world"


@app.route("/ip")
def ip():
    return subprocess.check_output("ls")
