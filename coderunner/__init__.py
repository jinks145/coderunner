from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#for debugging
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

coderunner = Flask(__name__)


#config class
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    #Configuration for the database
        # if there is a database to connect, os.environ.get('DATABASE_URL')
        # if not it will default to the sqllite3 version
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        # to turn off the unwanted notification
        SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    

#routes
@coderunner.route('/')
def main():
    coderunner.logger.info('Debug info: coderunner.logger.info')
    return render_template("index.html")

@coderunner.route('/upload', methods = ['GET'])
def upload():
    file = request.files['inputFile']
    return file.filename