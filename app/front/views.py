from flask import render_template, redirect

from . import front as front_bp
from flask.ext.security import SQLAlchemyUserDatastore
from app import db, User, Role


@front_bp.route("/")
def index():
    return render_template('front/index.html')


@front_bp.route("/landing")
def landing():
    return render_template('front/landing.html')


@front_bp.route("/details")
def blogpost():
    return render_template('front/blogpost.html')

@front_bp.route("/about")
def about():
    return redirect("/", code=302)

@front_bp.route("/contact")
def contact():
    return render_template("front/contact.html")

@front_bp.route("/data")
def data():
    db.drop_all()
    db.create_all()
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    from flask_security.utils import encrypt_password
    role = user_datastore.create_role(name="root", description="Site administrator")
    user_datastore.create_user(email='root@site.com', password=encrypt_password('pwd'), roles=[role])
    user_datastore.create_user(email='user@site.com', password=encrypt_password('pwd'))
    db.session.commit()
    return "OK"
