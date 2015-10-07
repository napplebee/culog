from flask import render_template

from . import front as front_bp
from flask.ext.security import SQLAlchemyUserDatastore
from app import db, User, Role


@front_bp.route("/")
def index():
    return render_template('front/index.html')


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
