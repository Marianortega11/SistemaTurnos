import os
class Config:
    DEBUG = True
    SESSION_TYPE = "filesystem"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    db_user = os.environ.get("db_user")
    db_password = os.environ.get("db_password")
    db_host = os.environ.get("db_host")
    db_name = os.environ.get("db_name")
    

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    print(f"Database URI: {SQLALCHEMY_DATABASE_URI}")