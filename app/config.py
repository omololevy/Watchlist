class Config:
  '''
  General configuration parent class
  '''
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