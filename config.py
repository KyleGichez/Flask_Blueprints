class Config(object):
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_PATH = '/'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    SESSION_COOKIE_SECURE = False