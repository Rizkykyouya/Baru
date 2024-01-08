import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pemweblanjut_visitmail:09690ec15c2165c3e88ad995a1966b52ad7bca54@k4k.h.filess.io:3307/pemweblanjut_visitmail'

SQLALCHEMY_TRACK_MODIFICATIONS = False