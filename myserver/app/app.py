from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User (db.Model):
    __tablename__ = 'user'

    name = db.Column('name', db.Unicode, primary_key=True)
    password = db.Column('password', db.Unicode)

    def __repr__(self):
        return '<User %r>' % self.name
