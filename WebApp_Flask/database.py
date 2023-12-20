from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# CONNECT TO DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone_number = db.Column(db.Integer())
    message = db.Column(db.String(500))

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

with app.app_context():
    db.create_all()

