from flask_login import UserMixin
from sqlalchemy import func
from .extensions import db, bcrypt


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    phone_nums = db.relationship("Phone", cascade="all, delete")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext, 12)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phonenumber = db.Column(db.String(24), nullable=False)
    country_code = db.Column(db.String(5), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    data = db.relationship("Data", cascade="all, delete")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.String(10000))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    phone_num_id = db.Column(db.Integer, db.ForeignKey("phone.id"))
