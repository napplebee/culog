from app.core import db

from flask_security import UserMixin, RoleMixin

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

    active = db.Column(db.Boolean())
    registered_at = db.Column(db.DateTime())
    confirmed_at = db.Column(db.DateTime())

    current_login_at = db.Column(db.DateTime())
    current_login_ip = db.Column(db.String(100))
    last_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def is_authenticated(self):
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return self.is_authenticated

    def __repr__(self):
        return '<User %r>' % self.email


class Role(RoleMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __eq__(self, other):
        return (self.name == other or
                self.name == getattr(other, 'name', None))

    def __ne__(self, other):
        return (self.name != other and
                self.name != getattr(other, 'name', None))

    def __repr__(self):
        return '<Role %r>' % self.name