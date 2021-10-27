class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
  pass

class ProdConfig(Config):
  '''
  Production, Config class child

  Args:
    Config: The parent configuration classwith the general cofiguration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development Configuration child class
  Args:
    Config: the parent Configuration class with settings
  '''

  DEBUG =True