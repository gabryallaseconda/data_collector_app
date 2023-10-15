import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@localhost:5432/my_database"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://user:password@localhost:5432/my_database"
    CELERY_BROKER_URL = "amqp://rabbitmq:rabbitmq@localhost//"
    CELERY_RESULT_BACKEND = "db+postgresql://user:password@localhost:5432/my_database"
    CELERY_IMPORTS = [
        'webapp.blog.tasks'
    ]

    CELERYBEAT_SCHEDULE = {
        'log-every-30-seconds': {
            'task': 'webapp.blog.tasks.log',
            'schedule': datetime.timedelta(seconds=30),
            'args': ("Message",)
        }, }

