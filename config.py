import os

class Config:
    QUOTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'

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