from flask import Flask
from routes.forms import forms
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(forms)