from environs import Env
import hashlib

env = Env()
env.read_env()


class Config:
    """App configuration"""
    TESTING = False
    SECRET_KEY = hashlib.sha512(bytes(env.str('S_K'), 'utf-8')).hexdigest()
    MOVIE_API_KEY = env.str('MOVIE_API_KEY')
    MOVIE_API_VERSION = env.int('MOVIE_API_VERSION')
    MOVIE_API_PAYLOAD = f'?api_key={MOVIE_API_KEY}&language=en-US'
    MOVIE_API_BASE_URL = f'https://api.themoviedb.org/{MOVIE_API_VERSION}/movie'
    # MOVIE_API_BASE_URL = f'https://api.themoviedb.org/3/movie/{}?api_key={MOVIE_API_KEY}'


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
