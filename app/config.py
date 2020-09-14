class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c7e9b8ab46ba4a1abfac01ee184ab7fb'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True