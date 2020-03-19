class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET_KEY = 'harryporter123'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    PASSWORD = 'annet'
    HOST = 'localhost'
    USER = 'postgres'


class ProductionConfig(Config):
    DEBUG = False
    USER = 'slndpxxqrfafpv'
    PASSWORD = '027c4fd2db4013cf3db100796cd324edf4f9ec3ae7ea8a3f24e4edb94ba632e7'
    HOST = 'ec2-50-19-86-139.compute-1.amazonaws.com'
    DATABASE_NAME = 'd2jkfa8tso1bgi'
    # postgres://slndpxxqrfafpv:027c4fd2db4013cf3db100796cd324edf4f9ec3ae7ea8a3f24e4edb94ba632e7@ec2-50-19-86-139.compute-1.amazonaws.com:5432/d2jkfa8tso1bgi


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_NAME = 'diary'


class TestingConfig(Config):
    TESTING = False
    DEBUG = True
    DATABASE_NAME = 'test_one'


configuration = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
