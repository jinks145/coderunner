import time
import logging
import sys
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for
import subprocess
import os
import docker


# for debugging
logging.basicConfig(level=logging.DEBUG)

coderunner = Flask(__name__)

# for running subprocess to compile to emscriptenjs


# config class
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Configuration for the database
    # if there is a database to connect, os.environ.get('DATABASE_URL')
    # if not it will default to the sqllite3 version
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # to turn off the unwanted notification
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "b'\xae\xfe<\xf63.\xdam\xf6l\x05\x93]\xbd\xffb=\xc1\xb6u\xc7}(\x13'"


coderunner.config.from_object(Config)
# databases
db = SQLAlchemy(coderunner)
# for the migrations
migrate = Migrate(coderunner, db)

# Models
from coderunner.models import User, FileContents
# routes
@coderunner.route('/')
def main():
    coderunner.logger.info('Debug info: coderunner.logger.info')
    return render_template("index.html")


@coderunner.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']

        if '.cpp' not in file.filename:
            return render_template('500.html'), 500

        # converts the input to the record
        newFile = FileContents(filename=file.filename, data=file.read())
        db.session.add(newFile)
        db.session.commit()
        flash('uploaded and running')
        return redirect('/result')
    else:
        return render_template('upload.html')


@coderunner.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@coderunner.errorhandler(500)
def runtime_error(error):
    return render_template('500.html'), 500


# Comile classes and display result
@coderunner.route('/result', methods=['GET'])
def compileRun():
    files = FileContents.query.all()

    with open('./coderunner/fileStorage/runner.cpp', 'wb') as file:
        file.write(files[-1].data)
    # the cpp file is copied into a container
    # client = docker.from_env()

    start = time.time()
    output = subprocess.check_output(
        ['sudo', 'docker-compose', 'run', '--rm', 'sandbox']).decode("utf-8")
    end = time.time()

    return render_template('result.html', filename=files[-1].filename, filecontents=files[-1].data.decode('ascii'), runtime='%3.2f seconds' % (end - start), output=output)

# TODO: display the results
