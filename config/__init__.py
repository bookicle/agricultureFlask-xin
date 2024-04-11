class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:517517@localhost/arg?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 3600
