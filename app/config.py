from environs import Env
import hashlib

env = Env()
env.read_env()


class Config:
    """app configuration"""
    TESTING = False
    SECRET_KEY = hashlib.sha512(bytes(env.str('S_K'), 'utf-8')).hexdigest()


class ProdConfig(Config):
    """Production configuration"""
    pass
    DEBUG = False


class DevConfig(Config):
    """Development configuration """
    DEBUG = True


class TestConfig(Config):
    """Test configuration"""
    DEBUG = True
    TESTING = True

"""config_options as a dictionary object"""
config_options = dict(
    dev_config = DevConfig(),
    prod_config = ProdConfig(),
    test_config = TestConfig()
)
