
from coderunner.config import Config
from flask import Flask
import logging
import sys
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# for debugging
logging.basicConfig(level=logging.DEBUG)

coderunner = Flask(__name__)

# for running subprocess to compile to emscriptenjs

# config class

coderunner.config.from_object(Config)
# databases
db = SQLAlchemy(coderunner)
# for the migrations
migrate = Migrate(coderunner, db)
from coderunner import errors, routes 