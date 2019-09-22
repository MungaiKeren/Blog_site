import os

class Config:
    # QUOTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://keren:kayren@localhost/bloggy'
    SECRET_KEY = 'cd48e1c22de0961d5d1bfb14f8a66e006cfb1cfbf3f0c0f3'

    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}