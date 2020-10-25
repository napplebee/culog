# -*- coding: utf-8 -*-

from flask.ext.security import SQLAlchemyUserDatastore

from app import create_app
from app.core import db
from app.data.users import User, Role

app = create_app("dev")
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

# Create a user to test with
# db.drop_all()
# db.create_all()
role = user_datastore.create_role(name="root", description="Site administrator")
user_datastore.create_user(email='root_email', password='admin_pwd', roles=[role])
user_datastore.create_user(email='user_email', password='user_pwd')

db.session.commit()

