
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "thisisasecretkey"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                               'sqlite:///' + os.path.join(base_dir,'app.db')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://microblog:microblog123@mysql/microblog"
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

