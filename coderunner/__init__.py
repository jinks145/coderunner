from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
coderunner = Flask(__name__)


#config class
import os
basedir = os.path.curdir(__file__)
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


#routes
@coderunner.route('/')
@coderunner.route('/index')
def main():
    return render_template("index.html")