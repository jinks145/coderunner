from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#for debugging
import sys
import logging
import time
logging.basicConfig(level=logging.DEBUG)

coderunner = Flask(__name__)

#for running subprocess to compile to emscriptenjs

import subprocess

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
        SECRET_KEY = "b'\xae\xfe<\xf63.\xdam\xf6l\x05\x93]\xbd\xffb=\xc1\xb6u\xc7}(\x13'"


coderunner.config.from_object(Config)
#databases
db = SQLAlchemy(coderunner)
# for the migrations
migrate = Migrate(coderunner, db)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    
class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True)
    data = db.Column(db.LargeBinary)


#routes
@coderunner.route('/')
def main():
    coderunner.logger.info('Debug info: coderunner.logger.info')
    return render_template("index.html")

@coderunner.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']
        # converts the input to the record
        newFile = FileContents(filename=file.filename, data= file.read())
        db.session.add(newFile)
        db.session.commit()
        flash('uploaded and running')
        return redirect('/result')
    else:
        return render_template('upload.html')



#Comile classes and display result
@coderunner.route('/result', methods = ['GET'])
def compileRun():
    files = FileContents.query.all()
    
    with open('coderunner/fileStorage/runner.cpp', 'wb') as file:
        file.write(files[-1].data)
    # the cpp file is copied into a container
    # client = docker.from_env()
    
    subprocess.run(['docker', 'build', '-t', 'cis22acontainer', '.'])
    start = time.time()
    subprocess.run(['docker','run','--rm','cis22acontainer' ])
    end = time.time()
    subprocess.run(['docker', 'rmi', 'cis22acontainer'])
    
    return render_template('result.html',filename= files[-1].filename,filecontents= files[-1].data.decode('ascii'), runtime= '%3.2f seconds' % (end - start))

#TODO: display the results
    