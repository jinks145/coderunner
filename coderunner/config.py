import os
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
