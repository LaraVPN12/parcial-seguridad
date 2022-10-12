from distutils.debug import DEBUG

class Config():
    SECRET_KEY = '5BX!Q3tM*bgRcY7aXo%G'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}