class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c7e9b8ab46ba4a1abfac01ee184ab7fb'
    SOURCES_API_BASE_URL = "https://newsapi.org/v2/sources?apiKey=c7e9b8ab46ba4a1abfac01ee184ab7fb"
    pass



class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    

    DEBUG = True