from flask import Flask
from flask.sqlalchemy import SQLAlchemy
from flask.restless import APIManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])

if __name__ == '__main__':
    app.run()
